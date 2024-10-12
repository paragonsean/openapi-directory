# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.customer_token_creation_request import CustomerTokenCreationRequest
from openapi_server.models.customer_token_creation_response import CustomerTokenCreationResponse
from openapi_server.models.error_v2 import ErrorV2
from openapi_server.models.order import Order


pytestmark = pytest.mark.asyncio

async def test_cancel_authorization(client):
    """Test case for cancel_authorization

    Cancel an existing authorization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/payments/v1/authorizations/{authorization_token}'.format(authorization_token='authorization_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_order(client):
    """Test case for create_order

    Create a new order
    """
    body = openapi_server.CreateOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/payments/v1/authorizations/{authorization_token}/order'.format(authorization_token='authorization_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchase_token(client):
    """Test case for purchase_token

    Generate a consumer token
    """
    body = openapi_server.CustomerTokenCreationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/payments/v1/authorizations/{authorization_token}/customer-token'.format(authorization_token='authorization_token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

