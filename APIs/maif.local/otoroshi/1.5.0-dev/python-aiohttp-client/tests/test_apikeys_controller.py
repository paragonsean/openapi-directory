# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.deleted import Deleted
from openapi_server.models.group import Group
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.quotas import Quotas


pytestmark = pytest.mark.asyncio

async def test_all_api_keys(client):
    """Test case for all_api_keys

    Get all api keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/apikeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key(client):
    """Test case for api_key

    Get an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/apikeys/{client_id}'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_from_group(client):
    """Test case for api_key_from_group

    Get an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/groups/{group_id}/apikeys/{client_id}'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_from_group_quotas(client):
    """Test case for api_key_from_group_quotas

    Get the quota state of an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/groups/{group_id}/apikeys/{client_id}/quotas'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_group(client):
    """Test case for api_key_group

    Get the group of an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/apikeys/{client_id}/group'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_quotas(client):
    """Test case for api_key_quotas

    Get the quota state of an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/apikeys/{client_id}/quotas'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_keys(client):
    """Test case for api_keys

    Get all api keys for the group of a service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/apikeys'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_keys_from_group(client):
    """Test case for api_keys_from_group

    Get all api keys for the group of a service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/groups/{group_id}/apikeys'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_api_key(client):
    """Test case for create_api_key

    Create a new api key for a service
    """
    body = {"metadata":{"key":"value"},"clientId":"a string value","monthlyQuota":123,"throttlingQuota":123,"clientName":"a string value","authorizedEntities":["a string value"],"clientSecret":"a string value","dailyQuota":123,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/services/{service_id}/apikeys'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_api_key_from_group(client):
    """Test case for create_api_key_from_group

    Create a new api key for a group
    """
    body = {"metadata":{"key":"value"},"clientId":"a string value","monthlyQuota":123,"throttlingQuota":123,"clientName":"a string value","authorizedEntities":["a string value"],"clientSecret":"a string value","dailyQuota":123,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/groups/{group_id}/apikeys'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_key(client):
    """Test case for delete_api_key

    Delete an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/services/{service_id}/apikeys/{client_id}'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_key_from_group(client):
    """Test case for delete_api_key_from_group

    Delete an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/groups/{group_id}/apikeys/{client_id}'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_api_key(client):
    """Test case for patch_api_key

    Update an api key with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/services/{service_id}/apikeys/{client_id}'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_api_key_from_group(client):
    """Test case for patch_api_key_from_group

    Update an api key with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/groups/{group_id}/apikeys/{client_id}'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_api_key_from_group_quotas(client):
    """Test case for reset_api_key_from_group_quotas

    Reset the quota state of an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/groups/{group_id}/apikeys/{client_id}/quotas'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_api_key_quotas(client):
    """Test case for reset_api_key_quotas

    Reset the quota state of an api key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/services/{service_id}/apikeys/{client_id}/quotas'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_api_key(client):
    """Test case for update_api_key

    Update an api key
    """
    body = {"metadata":{"key":"value"},"clientId":"a string value","monthlyQuota":123,"throttlingQuota":123,"clientName":"a string value","authorizedEntities":["a string value"],"clientSecret":"a string value","dailyQuota":123,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/services/{service_id}/apikeys/{client_id}'.format(service_id='service_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_api_key_from_group(client):
    """Test case for update_api_key_from_group

    Update an api key
    """
    body = {"metadata":{"key":"value"},"clientId":"a string value","monthlyQuota":123,"throttlingQuota":123,"clientName":"a string value","authorizedEntities":["a string value"],"clientSecret":"a string value","dailyQuota":123,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/groups/{group_id}/apikeys/{client_id}'.format(group_id='group_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

