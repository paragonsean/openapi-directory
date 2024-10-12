# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_communication_link import ServerCommunicationLink
from openapi_server.models.server_communication_link_list_result import ServerCommunicationLinkListResult


pytestmark = pytest.mark.asyncio

async def test_server_communication_links_create_or_update(client):
    """Test case for server_communication_links_create_or_update

    
    """
    parameters = {"kind":"kind","location":"location","properties":{"partnerServer":"partnerServer","state":"state"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/communicationLinks/{communication_link_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', communication_link_name='communication_link_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_communication_links_delete(client):
    """Test case for server_communication_links_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/communicationLinks/{communication_link_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', communication_link_name='communication_link_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_communication_links_get(client):
    """Test case for server_communication_links_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/communicationLinks/{communication_link_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', communication_link_name='communication_link_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_communication_links_list_by_server(client):
    """Test case for server_communication_links_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/communicationLinks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

