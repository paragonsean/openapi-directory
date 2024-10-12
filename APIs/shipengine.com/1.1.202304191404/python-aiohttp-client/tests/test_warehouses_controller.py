# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_warehouse_request_body import CreateWarehouseRequestBody
from openapi_server.models.create_warehouse_response_body import CreateWarehouseResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_warehouse_by_id_response_body import GetWarehouseByIdResponseBody
from openapi_server.models.list_warehouses_response_body import ListWarehousesResponseBody
from openapi_server.models.update_warehouse_request_body import UpdateWarehouseRequestBody
from openapi_server.models.update_warehouse_settings_request_body import UpdateWarehouseSettingsRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_warehouse(client):
    """Test case for create_warehouse

    Create Warehouse
    """
    body = openapi_server.CreateWarehouseRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/warehouses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_warehouse(client):
    """Test case for delete_warehouse

    Delete Warehouse By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/warehouses/{warehouse_id}'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_warehouse_by_id(client):
    """Test case for get_warehouse_by_id

    Get Warehouse By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/warehouses/{warehouse_id}'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_warehouses(client):
    """Test case for list_warehouses

    List Warehouses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/warehouses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_warehouse(client):
    """Test case for update_warehouse

    Update Warehouse By Id
    """
    body = openapi_server.UpdateWarehouseRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/warehouses/{warehouse_id}'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_warehouse_settings(client):
    """Test case for update_warehouse_settings

    Update Warehouse Settings
    """
    body = openapi_server.UpdateWarehouseSettingsRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/warehouses/{warehouse_id}/settings'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

