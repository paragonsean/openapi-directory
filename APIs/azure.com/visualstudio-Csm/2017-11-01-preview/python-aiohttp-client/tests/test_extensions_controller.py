# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.extension_resource import ExtensionResource
from openapi_server.models.extension_resource_list_result import ExtensionResourceListResult
from openapi_server.models.extension_resource_request import ExtensionResourceRequest


pytestmark = pytest.mark.asyncio

async def test_extensions_create(client):
    """Test case for extensions_create

    Extensions_Create
    """
    body = {"location":"location","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"key":"properties"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{account_resource_name}/extension/{extension_resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', account_resource_name='account_resource_name_example', extension_resource_name='extension_resource_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extensions_delete(client):
    """Test case for extensions_delete

    Extensions_Delete
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{account_resource_name}/extension/{extension_resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', account_resource_name='account_resource_name_example', extension_resource_name='extension_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extensions_get(client):
    """Test case for extensions_get

    Extensions_Get
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{account_resource_name}/extension/{extension_resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', account_resource_name='account_resource_name_example', extension_resource_name='extension_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extensions_list_by_account(client):
    """Test case for extensions_list_by_account

    Extensions_ListByAccount
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{account_resource_name}/extension'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', account_resource_name='account_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extensions_update(client):
    """Test case for extensions_update

    Extensions_Update
    """
    body = {"location":"location","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"key":"properties"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{account_resource_name}/extension/{extension_resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', account_resource_name='account_resource_name_example', extension_resource_name='extension_resource_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

