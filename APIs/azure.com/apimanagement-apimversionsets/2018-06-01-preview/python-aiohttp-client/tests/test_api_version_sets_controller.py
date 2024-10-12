# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_version_set_collection import ApiVersionSetCollection
from openapi_server.models.api_version_set_contract import ApiVersionSetContract
from openapi_server.models.api_version_set_list_by_service_default_response import ApiVersionSetListByServiceDefaultResponse
from openapi_server.models.api_version_set_update_parameters import ApiVersionSetUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_api_version_set_create_or_update(client):
    """Test case for api_version_set_create_or_update

    
    """
    parameters = {"properties":{"versioningScheme":"Segment","displayName":"displayName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', version_set_id='version_set_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_version_set_delete(client):
    """Test case for api_version_set_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', version_set_id='version_set_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_version_set_get(client):
    """Test case for api_version_set_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', version_set_id='version_set_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_version_set_get_entity_tag(client):
    """Test case for api_version_set_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', version_set_id='version_set_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_version_set_list_by_service(client):
    """Test case for api_version_set_list_by_service

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_version_set_update(client):
    """Test case for api_version_set_update

    
    """
    parameters = {"properties":{"versioningScheme":"Segment","displayName":"displayName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/api-version-sets/{version_set_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', version_set_id='version_set_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

