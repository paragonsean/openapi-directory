# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_connection_policy import ServerConnectionPolicy


pytestmark = pytest.mark.asyncio

async def test_server_connection_policies_create_or_update(client):
    """Test case for server_connection_policies_create_or_update

    
    """
    parameters = {"kind":"kind","location":"location","properties":{"connectionType":"Default"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/connectionPolicies/{connection_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', connection_policy_name='connection_policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_connection_policies_get(client):
    """Test case for server_connection_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/connectionPolicies/{connection_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', connection_policy_name='connection_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

