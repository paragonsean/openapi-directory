# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.core_ready_to_pay import CoreReadyToPay
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.patch_transaction_request import PatchTransactionRequest
from openapi_server.models.payout_request import PayoutRequest
from openapi_server.models.ready_to_pay_methods_inner import ReadyToPayMethodsInner
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_query import TransactionQuery
from openapi_server.models.transaction_refund import TransactionRefund
from openapi_server.models.transaction_request import TransactionRequest
from openapi_server.models.transaction_timeline import TransactionTimeline
from openapi_server.models.transaction_update import TransactionUpdate


pytestmark = pytest.mark.asyncio

async def test_delete_transaction_timeline(client):
    """Test case for delete_transaction_timeline

    Delete a Transaction Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/transactions/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction(client):
    """Test case for get_transaction

    Retrieve a Transaction
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_collection(client):
    """Test case for get_transaction_collection

    Retrieve a list of transactions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('sort', ['sort_example']),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_timeline(client):
    """Test case for get_transaction_timeline

    Retrieve a transaction Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction_timeline_collection(client):
    """Test case for get_transaction_timeline_collection

    Retrieve a list of transaction timeline messages
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/transactions/{id}/timeline'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_transaction(client):
    """Test case for patch_transaction

    Update a transaction
    """
    body = openapi_server.PatchTransactionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/transactions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payout(client):
    """Test case for post_payout

    Create a credit transaction
    """
    body = {"notificationUrl":"https://openapi-generator.tech","amount":97.97,"isMerchantInitiated":False,"redirectUrl":"https://openapi-generator.tech","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","paymentInstrument":"","processedTime":"2000-01-23T04:56:07.000+00:00","websiteId":"","paymentInstruction":"","requestId":"44433322-2c4y-483z-a0a9-158621f77a21","isProcessedOutside":False,"riskMetadata":{"country":"US","accuracyRadius":0,"distance":1,"city":"New York","isp":"isp","latitude":5.962133916683182,"postalCode":"postalCode","hasMismatchedHolderName":True,"httpHeaders":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Content-Type":"application/json"},"score":7,"vpnServiceName":"vpnServiceName","hasMismatchedBillingAddressCountry":True,"isVpn":True,"fingerprint":"pIUt3xbgX3l9g3YDiLbx","isHosting":True,"longitude":5.637376656633329,"hasMismatchedTimeZone":True,"deviceVelocity":6,"ipAddress":"93.92.91.90","timeZone":"America/New_York","paymentInstrumentVelocity":2,"isProxy":True,"isTor":True,"browserData":{"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":300,"isJavaEnabled":True,"language":"en-US","colorDepth":24},"hasMismatchedBankCountry":True,"region":"NY"},"customerId":"","currency":"","billingAddress":"","invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payouts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ready_to_pay(client):
    """Test case for post_ready_to_pay

    Ready to Pay
    """
    body = {"websiteId":"","riskMetadata":{"country":"US","accuracyRadius":0,"distance":1,"city":"New York","isp":"isp","latitude":5.962133916683182,"postalCode":"postalCode","hasMismatchedHolderName":True,"httpHeaders":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Content-Type":"application/json"},"score":7,"vpnServiceName":"vpnServiceName","hasMismatchedBillingAddressCountry":True,"isVpn":True,"fingerprint":"pIUt3xbgX3l9g3YDiLbx","isHosting":True,"longitude":5.637376656633329,"hasMismatchedTimeZone":True,"deviceVelocity":6,"ipAddress":"93.92.91.90","timeZone":"America/New_York","paymentInstrumentVelocity":2,"isProxy":True,"isTor":True,"browserData":{"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":300,"isJavaEnabled":True,"language":"en-US","colorDepth":24},"hasMismatchedBankCountry":True,"region":"NY"},"customerId":"","billingAddress":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ready-to-pay',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction(client):
    """Test case for post_transaction

    Create a transaction
    """
    body = {"notificationUrl":"https://openapi-generator.tech","amount":97.97,"isMerchantInitiated":False,"redirectUrl":"https://openapi-generator.tech","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","paymentInstrument":"","type":"3ds-authentication","processedTime":"2000-01-23T04:56:07.000+00:00","websiteId":"","paymentInstruction":"","requestId":"44433322-2c4y-483z-a0a9-158621f77a21","isProcessedOutside":False,"riskMetadata":{"country":"US","accuracyRadius":0,"distance":1,"city":"New York","isp":"isp","latitude":5.962133916683182,"postalCode":"postalCode","hasMismatchedHolderName":True,"httpHeaders":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Content-Type":"application/json"},"score":7,"vpnServiceName":"vpnServiceName","hasMismatchedBillingAddressCountry":True,"isVpn":True,"fingerprint":"pIUt3xbgX3l9g3YDiLbx","isHosting":True,"longitude":5.637376656633329,"hasMismatchedTimeZone":True,"deviceVelocity":6,"ipAddress":"93.92.91.90","timeZone":"America/New_York","paymentInstrumentVelocity":2,"isProxy":True,"isTor":True,"browserData":{"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":300,"isJavaEnabled":True,"language":"en-US","colorDepth":24},"hasMismatchedBankCountry":True,"region":"NY"},"customerId":"","currency":"","billingAddress":"","invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"]}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/transactions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction_query(client):
    """Test case for post_transaction_query

    Query a Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/transactions/{id}/query'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction_refund(client):
    """Test case for post_transaction_refund

    Refund a Transaction
    """
    body = {"amount":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/transactions/{id}/refund'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction_timeline(client):
    """Test case for post_transaction_timeline

    Create a transaction Timeline comment
    """
    body = {"_links":[{"rel":"self"},{"rel":"self"}],"extraData":{"tables":[{"footer":"footer","title":"title","type":"list"},{"footer":"footer","title":"title","type":"list"}],"author":{"userFullName":"userFullName","userId":"userId"},"mentions":{"key":"{\"@test@mail.com\":\"userId-1\"}"},"links":[{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"},{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"}],"actions":[{"action":"resend-email"},{"action":"resend-email"}]},"occurredTime":"","id":"","message":"message","type":"amount-adjusted","triggeredBy":"rebilly"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/transactions/{id}/timeline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transaction_update(client):
    """Test case for post_transaction_update

    Update a Transaction status
    """
    body = {"result":"abandoned","amount":0.8008281904610115,"currency":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/transactions/{id}/update'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

