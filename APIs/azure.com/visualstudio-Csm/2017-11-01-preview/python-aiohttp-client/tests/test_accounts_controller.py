# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_resource import AccountResource
from openapi_server.models.account_resource_list_result import AccountResourceListResult
from openapi_server.models.account_resource_request import AccountResourceRequest
from openapi_server.models.check_name_availability_parameter import CheckNameAvailabilityParameter
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult


pytestmark = pytest.mark.asyncio

async def test_accounts_check_name_availability(client):
    """Test case for accounts_check_name_availability

    Accounts_CheckNameAvailability
    """
    body = {"resourceName":"resourceName","resourceType":"resourceType"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/microsoft.visualstudio/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_create_or_update(client):
    """Test case for accounts_create_or_update

    Accounts_CreateOrUpdate
    """
    body = {"accountName":"accountName","location":"location","operationType":"unknown","properties":{"key":"properties"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_delete(client):
    """Test case for accounts_delete

    Accounts_Delete
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    Accounts_Get
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account/{resource_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_list_by_resource_group(client):
    """Test case for accounts_list_by_resource_group

    Accounts_ListByResourceGroup
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.visualstudio/account'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

