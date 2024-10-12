# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_document_permission_response import ListDocumentPermissionResponse
from openapi_server.models.sync_v1_service_document_document_permission import SyncV1ServiceDocumentDocumentPermission


pytestmark = pytest.mark.asyncio

async def test_delete_document_permission(client):
    """Test case for delete_document_permission

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', document_sid='document_sid_example', identity='identity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_document_permission(client):
    """Test case for fetch_document_permission

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', document_sid='document_sid_example', identity='identity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_document_permission(client):
    """Test case for list_document_permission

    
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
        path='/v1/Services/{service_sid}/Documents/{document_sid}/Permissions'.format(service_sid='service_sid_example', document_sid='document_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_document_permission(client):
    """Test case for update_document_permission

    
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
        path='/v1/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}'.format(service_sid='service_sid_example', document_sid='document_sid_example', identity='identity_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

