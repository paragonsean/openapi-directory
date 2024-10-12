# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.user import User
from openapi_server.models.user_create_parameters import UserCreateParameters
from openapi_server.models.user_get_member_groups_parameters import UserGetMemberGroupsParameters
from openapi_server.models.user_get_member_groups_result import UserGetMemberGroupsResult
from openapi_server.models.user_list_result import UserListResult
from openapi_server.models.user_update_parameters import UserUpdateParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_create(client):
    """Test case for users_create

    
    """
    body = {"passwordProfile":{"password":"password","forceChangePasswordNextLogin":True},"mail":"mail","displayName":"displayName","accountEnabled":True,"userPrincipalName":"userPrincipalName","mailNickname":"mailNickname"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/users'.format(tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete(client):
    """Test case for users_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{tenant_id}/users/{upn_or_object_id}'.format(upn_or_object_id='upn_or_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/users/{upn_or_object_id}'.format(upn_or_object_id='upn_or_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_get_member_groups(client):
    """Test case for users_get_member_groups

    
    """
    body = {"securityEnabledOnly":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{tenant_id}/users/{object_id}/getMemberGroups'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$top', 100),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/users'.format(tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_update(client):
    """Test case for users_update

    
    """
    body = {"passwordProfile":{"password":"password","forceChangePasswordNextLogin":True},"mail":"mail","displayName":"displayName","accountEnabled":True,"userPrincipalName":"userPrincipalName","mailNickname":"mailNickname"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{tenant_id}/users/{upn_or_object_id}'.format(upn_or_object_id='upn_or_object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

