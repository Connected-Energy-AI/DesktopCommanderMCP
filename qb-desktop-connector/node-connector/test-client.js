/**
 * Test Client for QBWC Connector
 * Tests all 8 SOAP methods
 */

const soap = require('soap');
const axios = require('axios');

const BASE_URL = 'http://localhost:8443';
const WSDL_URL = `${BASE_URL}/qbwc?wsdl`;

async function testHealthCheck() {
  console.log('\n=== Testing Health Check ===');
  try {
    const response = await axios.get(`${BASE_URL}/health`);
    console.log('✅ Health check passed:', response.data);
    return true;
  } catch (error) {
    console.log('❌ Health check failed:', error.message);
    return false;
  }
}

async function testSOAPMethods() {
  console.log('\n=== Testing SOAP Methods ===');
  
  try {
    const client = await soap.createClientAsync(WSDL_URL);
    let ticket = null;

    // 1. serverVersion
    console.log('\n1. Testing serverVersion...');
    const versionResult = await client.serverVersionAsync({ strVersion: '2.3.0.100' });
    console.log('   Server version:', versionResult.serverVersion);

    // 2. clientVersion
    console.log('\n2. Testing clientVersion...');
    const clientVersionResult = await client.clientVersionAsync({ strVersion: '2.3.0.100' });
    console.log('   Client version response:', clientVersionResult.clientVersion || '(empty = accepted)');

    // 3. authenticate
    console.log('\n3. Testing authenticate...');
    const authResult = await client.authenticateAsync({
      strUserName: 'qbwc_user',
      strPassword: 'change_me_to_a_strong_password'
    });
    ticket = authResult.authenticateResult[0];
    const companyFile = authResult.authenticateResult[1];
    console.log('   Ticket:', ticket.substring(0, 8) + '...');
    console.log('   Company file:', companyFile || '(using current)');

    if (companyFile === 'nvu') {
      console.log('   ❌ Authentication failed!');
      return false;
    }

    // 4. sendRequestXML
    console.log('\n4. Testing sendRequestXML...');
    const sendResult = await client.sendRequestXMLAsync({
      ticket,
      strHCPResponse: '',
      strCompanyFileName: '',
      qbXMLCountry: 'US',
      qbXMLMajorVers: 16,
      qbXMLMinorVers: 0
    });
    const qbXML = sendResult.sendRequestXMLResult;
    console.log('   Request length:', qbXML ? qbXML.length : 0, 'chars');
    if (qbXML) {
      console.log('   First 100 chars:', qbXML.substring(0, 100) + '...');
    }

    // 5. receiveResponseXML (simulate progress)
    console.log('\n5. Testing receiveResponseXML...');
    const progressResult = await client.receiveResponseXMLAsync({
      ticket,
      response: qbXML || '',
      hresult: '',
      message: ''
    });
    console.log('   Progress:', progressResult.receiveResponseXMLResult + '%');

    // 6. getLastError
    console.log('\n6. Testing getLastError...');
    const errorResult = await client.getLastErrorAsync({ ticket });
    console.log('   Last error:', errorResult.getLastErrorResult || '(none)');

    // 7. closeConnection
    console.log('\n7. Testing closeConnection...');
    const closeResult = await client.closeConnectionAsync({ ticket });
    console.log('   Close result:', closeResult.closeConnectionResult);

    // 8. connectionError (test with fake ticket)
    console.log('\n8. Testing connectionError...');
    const connErrorResult = await client.connectionErrorAsync({
      ticket: 'fake-ticket',
      hresult: 'E_TEST_ERROR',
      message: 'Test error message'
    });
    console.log('   Connection error result:', connErrorResult.connectionErrorResult);

    console.log('\n✅ All SOAP methods working!\n');
    return true;

  } catch (error) {
    console.log('❌ SOAP test failed:', error.message);
    if (error.stack) {
      console.log(error.stack);
    }
    return false;
  }
}

async function runTests() {
  console.log('=================================');
  console.log('QBWC Connector Test Suite');
  console.log('=================================');
  console.log('Target:', BASE_URL);

  const healthOk = await testHealthCheck();
  if (!healthOk) {
    console.log('\n❌ Server not running. Start with: npm start');
    process.exit(1);
  }

  const soapOk = await testSOAPMethods();
  
  console.log('\n=================================');
  if (soapOk) {
    console.log('✅ All tests passed!');
    console.log('=================================\n');
    process.exit(0);
  } else {
    console.log('❌ Some tests failed');
    console.log('=================================\n');
    process.exit(1);
  }
}

runTests();
