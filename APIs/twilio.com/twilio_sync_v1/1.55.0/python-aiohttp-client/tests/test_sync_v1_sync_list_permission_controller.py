# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sync_list_permission_response import ListSyncListPermissionResponse
from openapi_server.models.sync_v1_service_sync_list_sync_list_permission import SyncV1ServiceSyncListSyncListPermission


pytestmark = pytest.mark.asyncio

async def test_delete_sync_list_permission(client):
    """Test case for delete_sync_list_permission

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', list_sid='list_sid_example', identity='identity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sync_list_permission(client):
    """Test case for fetch_sync_list_permission

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', list_sid='list_sid_example', identity='identity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_list_permission(client):
    """Test case for list_sync_list_permission

    
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
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Permissions'.format(service_sid='service_sid_example', list_sid='list_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sync_list_permission(client):
    """Test case for update_sync_list_permission

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'manage': True,
        'read': True,
        'write': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', list_sid='list_sid_example', identity='identity_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

