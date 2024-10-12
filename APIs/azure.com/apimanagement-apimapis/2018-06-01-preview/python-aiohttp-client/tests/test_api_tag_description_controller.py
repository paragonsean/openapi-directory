# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.tag_description_create_or_update_request import TagDescriptionCreateOrUpdateRequest
from openapi_server.models.tag_description_get200_response import TagDescriptionGet200Response
from openapi_server.models.tag_description_list_by_api200_response import TagDescriptionListByApi200Response


pytestmark = pytest.mark.asyncio

async def test_tag_description_create_or_update(client):
    """Test case for tag_description_create_or_update

    
    """
    parameters = openapi_server.TagDescriptionCreateOrUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/tagDescriptions/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_description_delete(client):
    """Test case for tag_description_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/tagDescriptions/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_description_get(client):
    """Test case for tag_description_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/tagDescriptions/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_description_get_entity_state(client):
    """Test case for tag_description_get_entity_state

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/tagDescriptions/{tag_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', tag_id='tag_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_description_list_by_api(client):
    """Test case for tag_description_list_by_api

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/tagDescriptions'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

