# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_warehouses200_response_inner import AllWarehouses200ResponseInner
from openapi_server.models.create_update_warehouse_request import CreateUpdateWarehouseRequest
from openapi_server.models.warehouse_by_id200_response import WarehouseById200Response


pytestmark = pytest.mark.asyncio

async def test_activate_warehouse(client):
    """Test case for activate_warehouse

    Activate warehouse
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/warehouses/{warehouse_id}/activation'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_warehouses(client):
    """Test case for all_warehouses

    List all warehouses
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/warehouses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_warehouse(client):
    """Test case for create_update_warehouse

    Create/update warehouse
    """
    body = {"id":"15bfc76","name":"Estoque Principal","warehouseDocks":[{"cost":"5.00","costToDisplay":"5,00","dockId":"1a8bce3","name":"Centro de Distribui├º├úo Principal","time":"3.00:00:00","translateDays":"dias"}]}
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/warehouses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_warehouse(client):
    """Test case for deactivate_warehouse

    Deactivate warehouse
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/warehouses/{warehouse_id}/deactivation'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_warehouse(client):
    """Test case for remove_warehouse

    Remove warehouse
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/configuration/warehouses/{warehouse_id}'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_warehouse_by_id(client):
    """Test case for warehouse_by_id

    List warehouse by ID
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/warehouses/{warehouse_id}'.format(warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

