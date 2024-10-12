# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sync_sync_map_item_response import ListSyncSyncMapItemResponse
from openapi_server.models.preview_sync_service_sync_map_sync_map_item import PreviewSyncServiceSyncMapSyncMapItem
from openapi_server.models.sync_map_item_enum_query_from_bound_type import SyncMapItemEnumQueryFromBoundType
from openapi_server.models.sync_map_item_enum_query_result_order import SyncMapItemEnumQueryResultOrder


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sync_sync_map_item(client):
    """Test case for create_sync_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'data': None,
        'key': 'key_example'
        }
    response = await client.request(
        method='POST',
        path='/Sync/Services/{service_sid}/Maps/{map_sid}/Items'.format(service_sid='service_sid_example', map_sid='map_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sync_sync_map_item(client):
    """Test case for delete_sync_sync_map_item

    
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/Sync/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sync_sync_map_item(client):
    """Test case for fetch_sync_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Sync/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_sync_map_item(client):
    """Test case for list_sync_sync_map_item

    
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
        path='/Sync/Services/{service_sid}/Maps/{map_sid}/Items'.format(service_sid='service_sid_example', map_sid='map_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sync_sync_map_item(client):
    """Test case for update_sync_sync_map_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'data': None
        }
    response = await client.request(
        method='POST',
        path='/Sync/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(service_sid='service_sid_example', map_sid='map_sid_example', key='key_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

