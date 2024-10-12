# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_dns_alias import ServerDnsAlias
from openapi_server.models.server_dns_alias_acquisition import ServerDnsAliasAcquisition
from openapi_server.models.server_dns_alias_list_result import ServerDnsAliasListResult


pytestmark = pytest.mark.asyncio

async def test_server_dns_aliases_acquire(client):
    """Test case for server_dns_aliases_acquire

    
    """
    parameters = {"oldServerDnsAliasId":"oldServerDnsAliasId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/dnsAliases/{dns_alias_name}/acquire'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', dns_alias_name='dns_alias_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_dns_aliases_create_or_update(client):
    """Test case for server_dns_aliases_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/dnsAliases/{dns_alias_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', dns_alias_name='dns_alias_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_dns_aliases_delete(client):
    """Test case for server_dns_aliases_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/dnsAliases/{dns_alias_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', dns_alias_name='dns_alias_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_dns_aliases_get(client):
    """Test case for server_dns_aliases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/dnsAliases/{dns_alias_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', dns_alias_name='dns_alias_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_dns_aliases_list_by_server(client):
    """Test case for server_dns_aliases_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/dnsAliases'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

