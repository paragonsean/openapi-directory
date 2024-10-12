# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_account_orders_customer_order_id_put200_response_inner import AccountsAccountOrdersCustomerOrderIdPut200ResponseInner
from openapi_server.models.accounts_account_orders_customer_order_id_put_request import AccountsAccountOrdersCustomerOrderIdPutRequest
from openapi_server.models.accounts_account_orders_post_request import AccountsAccountOrdersPostRequest
from openapi_server.models.order_state import OrderState


pytestmark = pytest.mark.asyncio

async def test_accounts_account_orders_customer_order_id_delete(client):
    """Test case for accounts_account_orders_customer_order_id_delete

    Cancel Order
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tradingapi/v1/accounts/{account}/orders/{customer_order_id}'.format(account='account_example', customer_order_id='customer_order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_orders_customer_order_id_get(client):
    """Test case for accounts_account_orders_customer_order_id_get

    Return specific order info
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts/{account}/orders/{customer_order_id}'.format(account='account_example', customer_order_id='customer_order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_orders_customer_order_id_put(client):
    """Test case for accounts_account_orders_customer_order_id_put

    Modify Order
    """
    body = openapi_server.AccountsAccountOrdersCustomerOrderIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tradingapi/v1/accounts/{account}/orders/{customer_order_id}'.format(account='account_example', customer_order_id='customer_order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_orders_get(client):
    """Test case for accounts_account_orders_get

    Open Orders
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/accounts/{account}/orders'.format(account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_account_orders_post(client):
    """Test case for accounts_account_orders_post

    Place Order
    """
    body = openapi_server.AccountsAccountOrdersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tradingapi/v1/accounts/{account}/orders'.format(account='account_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

