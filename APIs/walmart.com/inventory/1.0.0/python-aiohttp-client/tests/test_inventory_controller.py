# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.get_inventory200_response import GetInventory200Response
from openapi_server.models.get_multi_node_inventory_for_all_sku_and_all_ship_nodes200_response import GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response
from openapi_server.models.get_multi_node_inventory_for_sku_and_all_shipnodes200_response import GetMultiNodeInventoryForSkuAndAllShipnodes200Response
from openapi_server.models.get_wfs_inventory200_response import GetWFSInventory200Response
from openapi_server.models.update_bulk_inventory200_response import UpdateBulkInventory200Response
from openapi_server.models.update_multi_node_inventory200_response import UpdateMultiNodeInventory200Response
from openapi_server.models.update_multi_node_inventory_request import UpdateMultiNodeInventoryRequest


pytestmark = pytest.mark.asyncio

async def test_get_inventory(client):
    """Test case for get_inventory

    Inventory
    """
    params = [('sku', 'sku_example'),
                    ('shipNode', 'ship_node_example')]
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='GET',
        path='/v3/inventory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_node_inventory_for_all_sku_and_all_ship_nodes(client):
    """Test case for get_multi_node_inventory_for_all_sku_and_all_ship_nodes

    Multiple Item Inventory for All Ship Nodes
    """
    params = [('limit', '10'),
                    ('nextCursor', 'next_cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='GET',
        path='/v3/inventories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multi_node_inventory_for_sku_and_all_shipnodes(client):
    """Test case for get_multi_node_inventory_for_sku_and_all_shipnodes

    Single Item Inventory by Ship Node
    """
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='GET',
        path='/v3/inventories/{sku}'.format(sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wfs_inventory(client):
    """Test case for get_wfs_inventory

    WFS Inventory
    """
    params = [('sku', 'sku_example'),
                    ('fromModifiedDate', 'from_modified_date_example'),
                    ('toModifiedDate', 'to_modified_date_example'),
                    ('limit', '10'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='GET',
        path='/v3/fulfillment/inventory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_bulk_inventory(client):
    """Test case for update_bulk_inventory

    Bulk Item Inventory Update
    """
    params = [('feedType', 'feed_type_example'),
                    ('shipNode', 'ship_node_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v3/feeds',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_inventory_for_an_item(client):
    """Test case for update_inventory_for_an_item

    Update inventory
    """
    body = {"quantity":{"amount":10,"unit":"EACH"},"sku":"97964_KFTest"}
    params = [('sku', 'sku_example'),
                    ('shipNode', 'ship_node_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='PUT',
        path='/v3/inventory',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_multi_node_inventory(client):
    """Test case for update_multi_node_inventory

    Update Item Inventory per Ship Node
    """
    body = {"inventories":{"nodes":[{"inputQty":{"amount":88,"unit":"EACH"},"shipNode":"1000005050"},{"inputQty":{"amount":55,"unit":"EACH"},"shipNode":"79897837271126017"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wm_sec_access_token': 'eyJraWQiOiIzZjVhYTFmNS1hYWE5LTQzM.....',
        'wm_consumer_channel_type': 'wm_consumer_channel_type_example',
        'wm_qos_correlation_id': 'b3261d2d-028a-4ef7-8602-633c23200af6',
        'wm_svc_name': 'Walmart Service Name',
    }
    response = await client.request(
        method='PUT',
        path='/v3/inventories/{sku}'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

