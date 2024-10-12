# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sync_map_item_response import ListSyncMapItemResponse
from openapi_server.models.sync_map_item_enum_query_from_bound_type import SyncMapItemEnumQueryFromBoundType
from openapi_server.models.sync_map_item_enum_query_result_order import SyncMapItemEnumQueryResultOrder
from openapi_server.models.sync_v1_service_sync_map_sync_map_item import SyncV1ServiceSyncMapSyncMapItem


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sync_map_item(client):
    """Test case for create_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'collection_ttl': 56,
        'data': None,
        'item_ttl': 56,
        'key': 'key_example',
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Maps/{map_sid}/Items'.format(service_sid='service_sid_example', map_sid='map_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sync_map_item(client):
    """Test case for delete_sync_map_item

    
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sync_map_item(client):
    """Test case for fetch_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_map_item(client):
    """Test case for list_sync_map_item

    
    """
    params = [('Order', openapi_server.SyncMapItemEnumQueryResultOrder()),
                    ('From', '_from_example'),
                    ('Bounds', openapi_server.SyncMapItemEnumQueryFromBoundType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Maps/{map_sid}/Items'.format(service_sid='service_sid_example', map_sid='map_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sync_map_item(client):
    """Test case for update_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'collection_ttl': 56,
        'data': None,
        'item_ttl': 56,
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

