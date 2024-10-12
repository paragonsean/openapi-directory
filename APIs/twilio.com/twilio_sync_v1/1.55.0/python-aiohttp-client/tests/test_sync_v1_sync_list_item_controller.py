# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sync_list_item_response import ListSyncListItemResponse
from openapi_server.models.sync_list_item_enum_query_from_bound_type import SyncListItemEnumQueryFromBoundType
from openapi_server.models.sync_list_item_enum_query_result_order import SyncListItemEnumQueryResultOrder
from openapi_server.models.sync_v1_service_sync_list_sync_list_item import SyncV1ServiceSyncListSyncListItem


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sync_list_item(client):
    """Test case for create_sync_list_item

    
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
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Items'.format(service_sid='service_sid_example', list_sid='list_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sync_list_item(client):
    """Test case for delete_sync_list_item

    
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}'.format(service_sid='service_sid_example', list_sid='list_sid_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sync_list_item(client):
    """Test case for fetch_sync_list_item

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}'.format(service_sid='service_sid_example', list_sid='list_sid_example', index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_list_item(client):
    """Test case for list_sync_list_item

    
    """
    params = [('Order', openapi_server.SyncListItemEnumQueryResultOrder()),
                    ('From', '_from_example'),
                    ('Bounds', openapi_server.SyncListItemEnumQueryFromBoundType()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Items'.format(service_sid='service_sid_example', list_sid='list_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sync_list_item(client):
    """Test case for update_sync_list_item

    
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
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Items/{index}'.format(service_sid='service_sid_example', list_sid='list_sid_example', index=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

