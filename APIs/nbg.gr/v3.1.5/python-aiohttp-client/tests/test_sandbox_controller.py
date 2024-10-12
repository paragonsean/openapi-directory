# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sandbox import Sandbox
from openapi_server.models.sandbox_request import SandboxRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sandbox_post(client):
    """Test case for sandbox_post

    Create Sandbox
    """
    body = {"sandboxId":"sandboxId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/sandbox',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sandbox_put(client):
    """Test case for sandbox_put

    Import Sandbox
    """
    body = {"sandboxId":"sandboxId","users":[{"cards":[{"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"party":{"name":"name","id":"id"},"info":{"number":"number","holderName":"holderName","ledgerBalance":7.386281948385884,"creditLimit":4.145608029883936,"description":"description","expiration":"expiration","subType":"subType","type":"type","availableBalance":2.027123023002322}},{"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"party":{"name":"name","id":"id"},"info":{"number":"number","holderName":"holderName","ledgerBalance":7.386281948385884,"creditLimit":4.145608029883936,"description":"description","expiration":"expiration","subType":"subType","type":"type","availableBalance":2.027123023002322}}],"accounts":[{"scheduledPayments":[{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"},{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"}],"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"beneficiaries":[{"name":"name"},{"name":"name"}],"party":{"name":"name","id":"id"},"info":{"ledgerBalance":6.027456183070403,"accountSubType":"accountSubType","accountType":"accountType","iban":"iban","alias":"alias","description":"description","overdraftLimit":1.4658129805029452,"currency":"currency","openingDate":"2000-01-23T04:56:07.000+00:00","availableBalance":0.8008281904610115},"standingOrders":[{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"},{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"}]},{"scheduledPayments":[{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"},{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"}],"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"beneficiaries":[{"name":"name"},{"name":"name"}],"party":{"name":"name","id":"id"},"info":{"ledgerBalance":6.027456183070403,"accountSubType":"accountSubType","accountType":"accountType","iban":"iban","alias":"alias","description":"description","overdraftLimit":1.4658129805029452,"currency":"currency","openingDate":"2000-01-23T04:56:07.000+00:00","availableBalance":0.8008281904610115},"standingOrders":[{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"},{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"}]}],"retryCacheEntries":[{"cacheKey":"cacheKey","count":1,"expirationTimestamp":"2000-01-23T04:56:07.000+00:00"},{"cacheKey":"cacheKey","count":1,"expirationTimestamp":"2000-01-23T04:56:07.000+00:00"}],"userId":"userId"},{"cards":[{"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"party":{"name":"name","id":"id"},"info":{"number":"number","holderName":"holderName","ledgerBalance":7.386281948385884,"creditLimit":4.145608029883936,"description":"description","expiration":"expiration","subType":"subType","type":"type","availableBalance":2.027123023002322}},{"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"party":{"name":"name","id":"id"},"info":{"number":"number","holderName":"holderName","ledgerBalance":7.386281948385884,"creditLimit":4.145608029883936,"description":"description","expiration":"expiration","subType":"subType","type":"type","availableBalance":2.027123023002322}}],"accounts":[{"scheduledPayments":[{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"},{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"}],"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"beneficiaries":[{"name":"name"},{"name":"name"}],"party":{"name":"name","id":"id"},"info":{"ledgerBalance":6.027456183070403,"accountSubType":"accountSubType","accountType":"accountType","iban":"iban","alias":"alias","description":"description","overdraftLimit":1.4658129805029452,"currency":"currency","openingDate":"2000-01-23T04:56:07.000+00:00","availableBalance":0.8008281904610115},"standingOrders":[{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"},{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"}]},{"scheduledPayments":[{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"},{"amount":5.962133916683182,"executionDate":"2000-01-23T04:56:07.000+00:00","senderReference":"senderReference","description":"description"}],"statements":[{"number":"number","month":2,"year":7},{"number":"number","month":2,"year":7}],"transactions":[{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"},{"reference":"reference","amount":3.616076749251911,"relatedName":"relatedName","accountingBalance":9.301444243932576,"relatedAccount":"relatedAccount","bookingDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","currency":"currency","valueDateTime":"2000-01-23T04:56:07.000+00:00","creditDebit":"creditDebit","transactionCode":"transactionCode"}],"beneficiaries":[{"name":"name"},{"name":"name"}],"party":{"name":"name","id":"id"},"info":{"ledgerBalance":6.027456183070403,"accountSubType":"accountSubType","accountType":"accountType","iban":"iban","alias":"alias","description":"description","overdraftLimit":1.4658129805029452,"currency":"currency","openingDate":"2000-01-23T04:56:07.000+00:00","availableBalance":0.8008281904610115},"standingOrders":[{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"},{"amount":5.637376656633329,"nextPaymentDate":"2000-01-23T04:56:07.000+00:00","lastPaymentDate":"2000-01-23T04:56:07.000+00:00","description":"description","firstPaymentDate":"2000-01-23T04:56:07.000+00:00","finalPaymentDate":"2000-01-23T04:56:07.000+00:00","frequency":"frequency","status":"status"}]}],"retryCacheEntries":[{"cacheKey":"cacheKey","count":1,"expirationTimestamp":"2000-01-23T04:56:07.000+00:00"},{"cacheKey":"cacheKey","count":1,"expirationTimestamp":"2000-01-23T04:56:07.000+00:00"}],"userId":"userId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/sandbox',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sandbox_sandbox_id_delete(client):
    """Test case for sandbox_sandbox_id_delete

    Delete Sandbox
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/sandbox/{sandbox_id}'.format(sandbox_id='sandbox_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sandbox_sandbox_id_get(client):
    """Test case for sandbox_sandbox_id_get

    Export Sandbox
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Client-Id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5/sandbox/{sandbox_id}'.format(sandbox_id='sandbox_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

