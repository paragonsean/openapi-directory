# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getinventorywithdispatchedreservations200_response_inner import Getinventorywithdispatchedreservations200ResponseInner
from openapi_server.models.inventory_by_sku200_response import InventoryBySku200Response
from openapi_server.models.inventoryperdock200_response_inner import Inventoryperdock200ResponseInner
from openapi_server.models.save_supply_lot import SaveSupplyLot
from openapi_server.models.update_inventory_by_skuand_warehouse_request1 import UpdateInventoryBySkuandWarehouseRequest1


pytestmark = pytest.mark.asyncio

async def test_get_supply_lots(client):
    """Test case for get_supply_lots

    List supply lots
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/items/{sku_id}/warehouses/{warehouse_id}/supplyLots'.format(sku_id='sku_id_example', warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getinventorywithdispatchedreservations(client):
    """Test case for getinventorywithdispatchedreservations

    List inventory with dispatched reservations
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/items/{item_id}/warehouses/{warehouse_id}/dispatched'.format(item_id='item_id_example', warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_by_sku(client):
    """Test case for inventory_by_sku

    List inventory by SKU
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
        path='/api/logistics/pvt/inventory/skus/{sku_id}'.format(sku_id='sku_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventoryperdock(client):
    """Test case for inventoryperdock

    List inventory per dock
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/items/{sku_id}/docks/{dock_id}'.format(sku_id='sku_id_example', dock_id='dock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventoryperdockandwarehouse(client):
    """Test case for inventoryperdockandwarehouse

    List inventory per dock and warehouse
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/items/{sku_id}/docks/{dock_id}/warehouses/{warehouse_id}'.format(sku_id='sku_id_example', dock_id='dock_id_example', warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventoryperwarehouse(client):
    """Test case for inventoryperwarehouse

    List inventory per warehouse
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/items/{sku_id}/warehouses/{warehouse_id}'.format(sku_id='sku_id_example', warehouse_id='warehouse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_save_supply_lot(client):
    """Test case for save_supply_lot

    Save supply lot
    """
    body = {"dateOfSupplyUtc":"2020-04-05T00:00:00+00:00","keepSellingAfterExpiration":true,"quantity":1000}
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/inventory/items/{sku_id}/warehouses/{warehouse_id}/supplyLots/{supply_lot_id}'.format(sku_id='sku_id_example', warehouse_id='warehouse_id_example', supply_lot_id='supply_lot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer_supply_lot(client):
    """Test case for transfer_supply_lot

    Transfer supply lot
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/inventory/items/{sku_id}/warehouses/{warehouse_id}/supplyLots/{supply_lot_id}/transfer'.format(sku_id='sku_id_example', warehouse_id='warehouse_id_example', supply_lot_id='supply_lot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_update_inventory_by_skuand_warehouse(client):
    """Test case for update_inventory_by_skuand_warehouse

    Update inventory by SKU and warehouse
    """
    body = {"dateUtcOnBalanceSystem":"null","quantity":101,"timeToRefill (deprecated)":"00:00:00","unlimitedQuantity":false}
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/inventory/skus/{sku_id}/warehouses/{warehouse_id}'.format(sku_id='sku_id_example', warehouse_id='warehouse_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

