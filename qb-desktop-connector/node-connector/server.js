/**
 * QuickBooks Desktop Enterprise Web Connector SOAP Server
 * Implements all 8 QBWC SOAP methods for AWS us-east-1 backend
 * 
 * For Talian Technologies - Oil & Gas Operations
 */

require('dotenv').config();
const express = require('express');
const soap = require('soap');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.SERVER_PORT || 8443;

// Configuration
const config = {
  username: process.env.QBWC_USERNAME || 'qbwc_user',
  password: process.env.QBWC_PASSWORD || 'change_me_to_a_strong_password',
  companyFile: process.env.QBWC_COMPANY_FILE || '',
  appName: process.env.QBWC_APP_NAME || 'Talian Technologies Connector',
  appGUID: process.env.QBWC_APP_GUID || 'YOUR-GUID-HERE'
};

// Session storage (in production, use Redis or database)
const sessions = new Map();

// Logging helper
function log(level, method, message, data = null) {
  const timestamp = new Date().toISOString();
  const logEntry = {
    timestamp,
    level,
    method,
    message,
    ...(data && { data })
  };
  console.log(JSON.stringify(logEntry));
}

// qbXML builders for common queries
const qbXMLBuilders = {
  // Get all customers
  CustomerQuery: () => `
    <?xml version="1.0" encoding="utf-8"?>
    <?qbxml version="16.0"?>
    <QBXML>
      <CustomerQueryRq>
        <MaxReturned>100</MaxReturned>
        <ActiveStatus>All</ActiveStatus>
        <IncludeRetElement>Name</IncludeRetElement>
        <IncludeRetElement>CompanyName</IncludeRetElement>
        <IncludeRetElement>Balance</IncludeRetElement>
        <IncludeRetElement>TotalRevenue</IncludeRetElement>
      </CustomerQueryRq>
    </QBXML>
  `.trim(),

  // Get all invoices
  InvoiceQuery: () => `
    <?xml version="1.0" encoding="utf-8"?>
    <?qbxml version="16.0"?>
    <QBXML>
      <InvoiceQueryRq>
        <MaxReturned>100</MaxReturned>
        <IncludeRetElement>RefNumber</IncludeRetElement>
        <IncludeRetElement>CustomerRef</IncludeRetElement>
        <IncludeRetElement>TotalAmount</IncludeRetElement>
        <IncludeRetElement>DueDate</IncludeRetElement>
        <IncludeRetElement>TermsRef</IncludeRetElement>
      </InvoiceQueryRq>
    </QBXML>
  `.trim(),

  // Get vendor list (for oil & gas suppliers)
  VendorQuery: () => `
    <?xml version="1.0" encoding="utf-8"?>
    <?qbxml version="16.0"?>
    <QBXML>
      <VendorQueryRq>
        <MaxReturned>100</MaxReturned>
        <ActiveStatus>All</ActiveStatus>
        <IncludeRetElement>Name</IncludeRetElement>
        <IncludeRetElement>CompanyName</IncludeRetElement>
        <IncludeRetElement>Balance</IncludeRetElement>
      </VendorQueryRq>
    </QBXML>
  `.trim(),

  // Get items (for equipment/inventory tracking)
  ItemQuery: () => `
    <?xml version="1.0" encoding="utf-8"?>
    <?qbxml version="16.0"?>
    <QBXML>
      <ItemQueryRq>
        <MaxReturned>100</MaxReturned>
        <IncludeRetElement>Name</IncludeRetElement>
        <IncludeRetElement>Type</IncludeRetElement>
        <IncludeRetElement>QuantityOnHand</IncludeRetElement>
        <IncludeRetElement>PurchaseCost</IncludeRetElement>
      </ItemQueryRq>
    </QBXML>
  `.trim()
};

// Request queue management for Talian Technologies workflows
let requestQueue = [];
let currentRequestIndex = 0;

function getRequestQueue() {
  // Add queries based on your energy services workflows
  if (requestQueue.length === 0) {
    requestQueue = [
      { type: 'CustomerQuery', xml: qbXMLBuilders.CustomerQuery() },
      { type: 'InvoiceQuery', xml: qbXMLBuilders.InvoiceQuery() },
      { type: 'VendorQuery', xml: qbXMLBuilders.VendorQuery() },
      { type: 'ItemQuery', xml: qbXMLBuilders.ItemQuery() }
    ];
  }
  return requestQueue;
}

// SOAP service implementation
const qbwcService = {
  QBWebConnectorSvc: {
    QBWebConnectorSvcSoap: {
      // 1. Return server version
      serverVersion: (args, callback) => {
        log('info', 'serverVersion', 'Returning server version');
        callback(null, { serverVersion: 'Talian-QBWC-Connector/1.0.0' });
      },

      // 2. Validate client version
      clientVersion: (args, callback) => {
        const version = args.strVersion;
        log('info', 'clientVersion', `Client version: ${version}`);
        
        // Accept all QBWC versions 2.2+
        callback(null, { clientVersion: '' });
      },

      // 3. Authenticate user
      authenticate: (args, callback) => {
        const { strUserName, strPassword } = args;
        log('info', 'authenticate', `Auth attempt for user: ${strUserName}`);

        if (strUserName === config.username && strPassword === config.password) {
          const ticket = uuidv4();
          sessions.set(ticket, {
            username: strUserName,
            companyFile: config.companyFile,
            createdAt: new Date(),
            requestIndex: 0
          });
          
          log('info', 'authenticate', 'Authentication successful', { ticket });
          callback(null, {
            authenticateResult: [ticket, config.companyFile || '']
          });
        } else {
          log('warn', 'authenticate', 'Authentication failed', { username: strUserName });
          callback(null, {
            authenticateResult: [uuidv4(), 'nvu'] // nvu = not valid user
          });
        }
      },

      // 4. Send qbXML request to QuickBooks
      sendRequestXML: (args, callback) => {
        const { ticket } = args;
        log('info', 'sendRequestXML', 'Processing request', { ticket });

        const session = sessions.get(ticket);
        if (!session) {
          log('error', 'sendRequestXML', 'Invalid session');
          callback(null, { sendRequestXMLResult: '' });
          return;
        }

        const queue = getRequestQueue();
        if (session.requestIndex >= queue.length) {
          log('info', 'sendRequestXML', 'All requests completed');
          callback(null, { sendRequestXMLResult: '' });
          return;
        }

        const request = queue[session.requestIndex];
        log('info', 'sendRequestXML', `Sending ${request.type}`);
        
        // Encode XML for SOAP response
        const encodedXML = request.xml
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&apos;');

        callback(null, { sendRequestXMLResult: encodedXML });
      },

      // 5. Receive qbXML response from QuickBooks
      receiveResponseXML: (args, callback) => {
        const { ticket, response } = args;
        log('info', 'receiveResponseXML', 'Received response', { ticket });

        const session = sessions.get(ticket);
        if (!session) {
          callback(null, { receiveResponseXMLResult: 100 });
          return;
        }

        // Decode and process response
        if (response) {
          const decoded = response
            .replace(/&lt;/g, '<')
            .replace(/&gt;/g, '>')
            .replace(/&amp;/g, '&')
            .replace(/&quot;/g, '"')
            .replace(/&apos;/g, "'");
          
          log('info', 'receiveResponseXML', 'Response data', { xml: decoded.substring(0, 200) });
          
          // Here you would parse the qbXML and store in your database
          // For Talian Technologies: store customers, invoices, vendors, items
        }

        session.requestIndex++;
        const progress = Math.round((session.requestIndex / getRequestQueue().length) * 100);
        
        log('info', 'receiveResponseXML', `Progress: ${progress}%`);
        callback(null, { receiveResponseXMLResult: progress >= 100 ? 100 : progress });
      },

      // 6. Get last error
      getLastError: (args, callback) => {
        log('info', 'getLastError', 'Getting last error');
        callback(null, { getLastErrorResult: '' });
      },

      // 7. Close connection
      closeConnection: (args, callback) => {
        const { ticket } = args;
        log('info', 'closeConnection', 'Closing connection', { ticket });

        sessions.delete(ticket);
        callback(null, { closeConnectionResult: 'OK' });
      },

      // 8. Handle connection errors
      connectionError: (args, callback) => {
        const { ticket, hresult, message } = args;
        log('error', 'connectionError', 'Connection error', { ticket, hresult, message });
        callback(null, { connectionErrorResult: 'OK' });
      }
    }
  }
};

// Start server
async function startServer() {
  try {
    // Load WSDL
    const wsdlPath = `${__dirname}/../wsdl/qbwebconnectorsvc.wsdl`;
    
    const server = await soap.createServerAsync({
      services: qbwcService,
      xml: require('fs').readFileSync(wsdlPath, 'utf8'),
      uri: 'http://localhost:8443/qbwc',
      path: '/qbwc'
    });

    server.app = app;
    
    // Health check endpoint
    app.get('/health', (req, res) => {
      res.json({ 
        status: 'healthy', 
        service: config.appName,
        sessions: sessions.size,
        timestamp: new Date().toISOString()
      });
    });

    // WSDL endpoint
    app.get('/qbwc', (req, res) => {
      res.type('application/xml');
      res.send(require('fs').readFileSync(wsdlPath, 'utf8'));
    });

    await new Promise((resolve) => {
      server.listen(PORT, resolve);
    });

    log('info', 'start', `QBWC SOAP server started on port ${PORT}`);
    console.log(`\n✅ Talian Technologies QBWC Connector running on http://localhost:${PORT}`);
    console.log(`   Health: http://localhost:${PORT}/health`);
    console.log(`   WSDL:   http://localhost:${PORT}/qbwc?wsdl\n`);

  } catch (error) {
    log('error', 'start', 'Failed to start server', { error: error.message });
    process.exit(1);
  }
}

startServer();
