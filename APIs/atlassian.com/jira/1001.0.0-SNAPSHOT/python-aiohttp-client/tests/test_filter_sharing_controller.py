# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_share_scope import DefaultShareScope
from openapi_server.models.share_permission import SharePermission
from openapi_server.models.share_permission_input_bean import SharePermissionInputBean


pytestmark = pytest.mark.asyncio

async def test_add_share_permission(client):
    """Test case for add_share_permission

    Add share permission
    """
    body = {"accountId":"accountId","groupId":"groupId","rights":0,"type":"user","groupname":"groupname","projectId":"projectId","projectRoleId":"projectRoleId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/filter/{id}/permission'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_share_permission(client):
    """Test case for delete_share_permission

    Delete share permission
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/filter/{id}/permission/{permission_id}'.format(id=56, permission_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_share_scope(client):
    """Test case for get_default_share_scope

    Get default share scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/defaultShareScope',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_permission(client):
    """Test case for get_share_permission

    Get share permission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/{id}/permission/{permission_id}'.format(id=56, permission_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_permissions(client):
    """Test case for get_share_permissions

    Get share permissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/filter/{id}/permission'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_default_share_scope(client):
    """Test case for set_default_share_scope

    Set default share scope
    """
    body = {"scope":"GLOBAL"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/filter/defaultShareScope',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

