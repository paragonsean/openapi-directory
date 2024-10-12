# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.stored_value_balance_check_request import StoredValueBalanceCheckRequest
from openapi_server.models.stored_value_balance_check_response import StoredValueBalanceCheckResponse
from openapi_server.models.stored_value_balance_merge_request import StoredValueBalanceMergeRequest
from openapi_server.models.stored_value_balance_merge_response import StoredValueBalanceMergeResponse
from openapi_server.models.stored_value_issue_request import StoredValueIssueRequest
from openapi_server.models.stored_value_issue_response import StoredValueIssueResponse
from openapi_server.models.stored_value_load_request import StoredValueLoadRequest
from openapi_server.models.stored_value_load_response import StoredValueLoadResponse
from openapi_server.models.stored_value_status_change_request import StoredValueStatusChangeRequest
from openapi_server.models.stored_value_status_change_response import StoredValueStatusChangeResponse
from openapi_server.models.stored_value_void_request import StoredValueVoidRequest
from openapi_server.models.stored_value_void_response import StoredValueVoidResponse


pytestmark = pytest.mark.asyncio

async def test_post_change_status(client):
    """Test case for post_change_status

    Changes the status of the payment method.
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","paymentMethod":{"key":"paymentMethod"},"recurringDetailReference":"recurringDetailReference","shopperInteraction":"Ecommerce","store":"store","shopperReference":"shopperReference","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/changeStatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_check_balance(client):
    """Test case for post_check_balance

    Checks the balance.
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","paymentMethod":{"key":"paymentMethod"},"recurringDetailReference":"recurringDetailReference","shopperInteraction":"Ecommerce","store":"store","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/checkBalance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_issue(client):
    """Test case for post_issue

    Issues a new card.
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","paymentMethod":{"key":"paymentMethod"},"recurringDetailReference":"recurringDetailReference","shopperInteraction":"Ecommerce","store":"store","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/issue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_load(client):
    """Test case for post_load

    Loads the payment method.
    """
    body = {"reference":"reference","loadType":"merchandiseReturn","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","paymentMethod":{"key":"paymentMethod"},"recurringDetailReference":"recurringDetailReference","shopperInteraction":"Ecommerce","store":"store","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/load',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merge_balance(client):
    """Test case for post_merge_balance

    Merge the balance of two cards.
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","sourcePaymentMethod":{"key":"sourcePaymentMethod"},"paymentMethod":{"key":"paymentMethod"},"recurringDetailReference":"recurringDetailReference","shopperInteraction":"Ecommerce","store":"store","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/mergeBalance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_void_transaction(client):
    """Test case for post_void_transaction

    Voids a transaction.
    """
    body = {"originalReference":"originalReference","reference":"reference","uniqueTerminalId":"uniqueTerminalId","merchantAccount":"merchantAccount","store":"store","tenderReference":"tenderReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/StoredValue/v46/voidTransaction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

