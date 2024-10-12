# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.origin import Origin
from openapi_server.models.origin_list_result import OriginListResult
from openapi_server.models.origin_update_parameters import OriginUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_origins_create(client):
    """Test case for origins_create

    
    """
    origin = {"properties":{"resourceState":"Creating","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/origins/{origin_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_name='origin_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=origin,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origins_delete(client):
    """Test case for origins_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/origins/{origin_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_name='origin_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origins_get(client):
    """Test case for origins_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/origins/{origin_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_name='origin_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origins_list_by_endpoint(client):
    """Test case for origins_list_by_endpoint

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/origins'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origins_update(client):
    """Test case for origins_update

    
    """
    origin_update_properties = {"properties":{"hostName":"hostName","httpPort":5249,"originHostHeader":"originHostHeader","weight":596,"priority":1,"httpsPort":39501,"enabled":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cdn/profiles/{profile_name}/endpoints/{endpoint_name}/origins/{origin_name}'.format(resource_group_name='resource_group_name_example', profile_name='profile_name_example', endpoint_name='endpoint_name_example', origin_name='origin_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=origin_update_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

