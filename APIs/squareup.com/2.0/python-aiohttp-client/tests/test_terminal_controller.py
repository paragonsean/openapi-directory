# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
from openapi_server.models.cancel_terminal_refund_response import CancelTerminalRefundResponse
from openapi_server.models.create_terminal_checkout_request import CreateTerminalCheckoutRequest
from openapi_server.models.create_terminal_checkout_response import CreateTerminalCheckoutResponse
from openapi_server.models.create_terminal_refund_request import CreateTerminalRefundRequest
from openapi_server.models.create_terminal_refund_response import CreateTerminalRefundResponse
from openapi_server.models.get_terminal_checkout_response import GetTerminalCheckoutResponse
from openapi_server.models.get_terminal_refund_response import GetTerminalRefundResponse
from openapi_server.models.search_terminal_checkouts_request import SearchTerminalCheckoutsRequest
from openapi_server.models.search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
from openapi_server.models.search_terminal_refunds_request import SearchTerminalRefundsRequest
from openapi_server.models.search_terminal_refunds_response import SearchTerminalRefundsResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_terminal_checkout(client):
    """Test case for cancel_terminal_checkout

    CancelTerminalCheckout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/checkouts/{checkout_id}/cancel'.format(checkout_id='checkout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_terminal_refund(client):
    """Test case for cancel_terminal_refund

    CancelTerminalRefund
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/refunds/{terminal_refund_id}/cancel'.format(terminal_refund_id='terminal_refund_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_terminal_checkout(client):
    """Test case for create_terminal_checkout

    CreateTerminalCheckout
    """
    body = {"request_body":{"checkout":{"amount_money":{"amount":2610,"currency":"USD"},"device_options":{"device_id":"dbb5d83a-7838-11ea-bc55-0242ac130003"},"note":"A brief note","reference_id":"id11572"},"idempotency_key":"28a0c3bc-7839-11ea-bc55-0242ac130003"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/checkouts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_terminal_refund(client):
    """Test case for create_terminal_refund

    CreateTerminalRefund
    """
    body = {"request_body":{"idempotency_key":"402a640b-b26f-401f-b406-46f839590c04","refund":{"amount_money":{"amount":111,"currency":"CAD"},"device_id":"f72dfb8e-4d65-4e56-aade-ec3fb8d33291","payment_id":"5O5OvgkcNUhl7JBuINflcjKqUzXZY","reason":"Returning items"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/refunds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_terminal_checkout(client):
    """Test case for get_terminal_checkout

    GetTerminalCheckout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/terminals/checkouts/{checkout_id}'.format(checkout_id='checkout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_terminal_refund(client):
    """Test case for get_terminal_refund

    GetTerminalRefund
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/terminals/refunds/{terminal_refund_id}'.format(terminal_refund_id='terminal_refund_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_terminal_checkouts(client):
    """Test case for search_terminal_checkouts

    SearchTerminalCheckouts
    """
    body = {"request_body":{"limit":2,"query":{"filter":{"status":"COMPLETED"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/checkouts/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_terminal_refunds(client):
    """Test case for search_terminal_refunds

    SearchTerminalRefunds
    """
    body = {"request_body":{"limit":1,"query":{"filter":{"status":"COMPLETED"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/terminals/refunds/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

