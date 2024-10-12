# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_pre_order_create_request import AppPreOrderCreateRequest
from openapi_server.models.app_pre_order_response import AppPreOrderResponse
from openapi_server.models.app_pre_order_update_request import AppPreOrderUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_pre_orders_create_instance(client):
    """Test case for app_pre_orders_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}}},"attributes":{"appReleaseDate":"2000-01-23"},"type":"appPreOrders"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appPreOrders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_pre_orders_delete_instance(client):
    """Test case for app_pre_orders_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appPreOrders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_pre_orders_get_instance(client):
    """Test case for app_pre_orders_get_instance

    
    """
    params = [('fields[appPreOrders]', ['fields_app_pre_orders_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPreOrders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_pre_orders_update_instance(client):
    """Test case for app_pre_orders_update_instance

    
    """
    body = {"data":{"attributes":{"appReleaseDate":"2000-01-23"},"id":"id","type":"appPreOrders"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appPreOrders/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

