"""
QuickBooks Desktop Enterprise Web Connector SOAP Server (Python)
Implements all 8 QBWC SOAP methods for AWS us-east-1 backend

For Talian Technologies - Oil & Gas Operations
"""

import os
import uuid
from datetime import datetime
from spyne import Application, ServiceBase, rpc, Unicode, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiServer
from flask import Flask, request, Response

# Configuration
CONFIG = {
    'username': os.environ.get('QBWC_USERNAME', 'qbwc_user'),
    'password': os.environ.get('QBWC_PASSWORD', 'change_me_to_a_strong_password'),
    'company_file': os.environ.get('QBWC_COMPANY_FILE', ''),
    'app_name': os.environ.get('QBWC_APP_NAME', 'Talian Technologies Connector'),
}

# Session storage
sessions = {}

# qbXML builders
def customer_query():
    return '''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
  <CustomerQueryRq>
    <MaxReturned>100</MaxReturned>
    <ActiveStatus>All</ActiveStatus>
    <IncludeRetElement>Name</IncludeRetElement>
    <IncludeRetElement>CompanyName</IncludeRetElement>
    <IncludeRetElement>Balance</IncludeRetElement>
  </CustomerQueryRq>
</QBXML>'''.strip()

def invoice_query():
    return '''<?xml version="1.0" encoding="utf-8"?>
<?qbxml version="16.0"?>
<QBXML>
  <InvoiceQueryRq>
    <MaxReturned>100</MaxReturned>
    <IncludeRetElement>RefNumber</IncludeRetElement>
    <IncludeRetElement>CustomerRef</IncludeRetElement>
    <IncludeRetElement>TotalAmount</IncludeRetElement>
    <IncludeRetElement>DueDate</IncludeRetElement>
  </InvoiceQueryRq>
</QBXML>'''.strip()

# Request queue
request_queue = [
    ('CustomerQuery', customer_query()),
    ('InvoiceQuery', invoice_query()),
]

class QBWebConnectorService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def serverVersion(ctx, strVersion):
        return 'Talian-QBWC-Connector-Python/1.0.0'

    @rpc(Unicode, _returns=Unicode)
    def clientVersion(ctx, strVersion):
        return ''  # Accept all versions

    @rpc(Unicode, Unicode, _returns=Array(Unicode))
    def authenticate(ctx, strUserName, strPassword):
        ticket = str(uuid.uuid4())
        
        if strUserName == CONFIG['username'] and strPassword == CONFIG['password']:
            sessions[ticket] = {
                'username': strUserName,
                'company_file': CONFIG['company_file'],
                'created_at': datetime.now(),
                'request_index': 0
            }
            return [ticket, CONFIG['company_file']]
        else:
            return [ticket, 'nvu']

    @rpc(Unicode, Unicode, Unicode, Unicode, Integer, Integer, _returns=Unicode)
    def sendRequestXML(ctx, ticket, strHCPResponse, strCompanyFileName, 
                       qbXMLCountry, qbXMLMajorVers, qbXMLMinorVers):
        session = sessions.get(ticket)
        if not session:
            return ''
        
        if session['request_index'] >= len(request_queue):
            return ''
        
        query_type, xml = request_queue[session['request_index']]
        # Encode for SOAP
        return xml.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=Integer)
    def receiveResponseXML(ctx, ticket, response, hresult, message):
        session = sessions.get(ticket)
        if not session:
            return 100
        
        session['request_index'] += 1
        progress = int((session['request_index'] / len(request_queue)) * 100)
        return min(progress, 100)

    @rpc(Unicode, _returns=Unicode)
    def getLastError(ctx, ticket):
        return ''

    @rpc(Unicode, _returns=Unicode)
    def closeConnection(ctx, ticket):
        sessions.pop(ticket, None)
        return 'OK'

    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def connectionError(ctx, ticket, hresult, message):
        return 'OK'

# Create Flask app
app = Flask(__name__)

# Create Spyne application
application = Application(
    [QBWebConnectorService],
    tns='http://developer.intuit.com/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

# Mount SOAP service
from spyne.server.wsgi import WsgiApplication
wsgi_app = WsgiApplication(application)

@app.route('/qbwc', methods=['POST'])
def soap_endpoint():
    return Response(wsgi_app(request.environ, request.start_response), 
                    content_type='text/xml')

@app.route('/qbwc', methods=['GET'])
def wsdl_endpoint():
    with open('../wsdl/qbwebconnectorsvc.wsdl', 'r') as f:
        return Response(f.read(), content_type='text/xml')

@app.route('/health')
def health():
    return {
        'status': 'healthy',
        'service': CONFIG['app_name'],
        'sessions': len(sessions),
        'timestamp': datetime.now().isoformat()
    }

if __name__ == '__main__':
    print(f"\n✅ Talian Technologies QBWC Connector (Python) running")
    print(f"   http://localhost:8443/health")
    print(f"   http://localhost:8443/qbwc?wsdl\n")
    
    from waitress import serve
    serve(app, host='0.0.0.0', port=8443)
