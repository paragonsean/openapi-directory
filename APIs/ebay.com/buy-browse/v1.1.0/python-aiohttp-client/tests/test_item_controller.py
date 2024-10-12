# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compatibility_payload import CompatibilityPayload
from openapi_server.models.compatibility_response import CompatibilityResponse
from openapi_server.models.item import Item
from openapi_server.models.item_group import ItemGroup
from openapi_server.models.items import Items


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_check_compatibility(client):
    """Test case for check_compatibility

    
    """
    body = openapi_server.CompatibilityPayload()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buy/browse/v1/item/{item_id}/check_compatibility'.format(item_id='item_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item(client):
    """Test case for get_item

    
    """
    params = [('fieldgroups', 'fieldgroups_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/item/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_by_legacy_id(client):
    """Test case for get_item_by_legacy_id

    
    """
    params = [('fieldgroups', 'fieldgroups_example'),
                    ('legacy_item_id', 'legacy_item_id_example'),
                    ('legacy_variation_id', 'legacy_variation_id_example'),
                    ('legacy_variation_sku', 'legacy_variation_sku_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/item/get_item_by_legacy_id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items(client):
    """Test case for get_items

    
    """
    params = [('item_ids', 'item_ids_example'),
                    ('item_group_ids', 'item_group_ids_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/item/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_by_item_group(client):
    """Test case for get_items_by_item_group

    
    """
    params = [('item_group_id', 'item_group_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/item/get_items_by_item_group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

