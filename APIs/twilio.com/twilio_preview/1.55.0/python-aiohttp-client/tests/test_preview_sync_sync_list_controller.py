# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sync_sync_list_response import ListSyncSyncListResponse
from openapi_server.models.preview_sync_service_sync_list import PreviewSyncServiceSyncList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sync_sync_list(client):
    """Test case for create_sync_sync_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/Sync/Services/{service_sid}/Lists'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sync_sync_list(client):
    """Test case for delete_sync_sync_list

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/Sync/Services/{service_sid}/Lists/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sync_sync_list(client):
    """Test case for fetch_sync_sync_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Sync/Services/{service_sid}/Lists/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_sync_list(client):
    """Test case for list_sync_sync_list

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/Sync/Services/{service_sid}/Lists'.format(service_sid='service_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

