# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model1_createanewtransaction_request import Model1CreateanewtransactionRequest
from openapi_server.models.model2_send_payments_public_request import Model2SendPaymentsPublicRequest
from openapi_server.models.model2_send_payments_with_saved_credit_card_request import Model2SendPaymentsWithSavedCreditCardRequest
from openapi_server.models.model4_doauthorization_request import Model4DoauthorizationRequest
from openapi_server.models.payment_details_response import PaymentDetailsResponse
from openapi_server.models.start_transaction_response import StartTransactionResponse
from openapi_server.models.transaction_details_response import TransactionDetailsResponse
from openapi_server.models.transaction_settlement_details import TransactionSettlementDetails


pytestmark = pytest.mark.asyncio

async def test_call1_createanewtransaction(client):
    """Test case for call1_createanewtransaction

    1. Starts a new transaction
    """
    body = {"channel":"{{accountName}}","referenceId":"1234567","salesChannel":"1","urn":"","value":100}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call2_send_payments_public(client):
    """Test case for call2_send_payments_public

    2.1 Send Payments Information Public
    """
    body = [{"currencyCode":"BRL","fields":{"accountId":"","address":null,"callbackUrl":"","cardNumber":"5378244888889174","document":"8041734561","dueDate":"10/19","holderName":"UserTest","validationCode":"231"},"installments":1,"installmentsInterestRate":0,"installmentsValue":100,"paymentSystem":4,"referenceValue":100,"transaction":{"id":"{{transactionId}}","merchantName":"{{accountName}}"},"value":100}]
    params = [('orderId', '{{orderId}}')]
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pub/transactions/{transaction_id}/payments'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call2_send_payments_with_saved_credit_card(client):
    """Test case for call2_send_payments_with_saved_credit_card

    2.2 Send Payments With Saved Credit Card
    """
    body = [{"currencyCode":"BRL","fields":{"accountId":"44D964F2053642E888E3B23549937F87","address":null,"callbackUrl":"","firstDigits":"411111","validationCode":"231"},"installments":1,"installmentsInterestRate":0,"installmentsValue":100,"paymentSystem":2,"referenceValue":100,"transaction":{"id":"{{transactionId}}","merchantName":"{{accountName}}"},"value":100}]
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/payments'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call3_send_additional_data(client):
    """Test case for call3_send_additional_data

    3. Send Additional Data
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/additional-data'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4_doauthorization(client):
    """Test case for call4_doauthorization

    Do authorization
    """
    body = {"prepareForRecurrency":false,"softDescriptor":"{{accountName}}","transactionId":"{{transactionId}}"}
    headers = { 
        'Content-Type': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pvt/transactions/{transaction_id}/authorization-request'.format(transaction_id='transaction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_details(client):
    """Test case for payment_details

    Payment Details
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/transactions/{transaction_id}/payments/{payment_id}'.format(transaction_id='transaction_id_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_details(client):
    """Test case for transaction_details

    Transaction Details
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/transactions/{transaction_id}'.format(transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transaction_settlement_details(client):
    """Test case for transaction_settlement_details

    Transaction Settlement  Details
    """
    headers = { 
        'Accept': 'application/json',
        'x_provider_api_app_key': '{{X-PROVIDER-API-AppKey}}',
        'x_provider_api_app_token': '{{X-PROVIDER-API-AppToken}}',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pvt/transactions/{transaction_id}/settlements'.format(transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

