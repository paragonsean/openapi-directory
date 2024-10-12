# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_template_create_or_update_request import EmailTemplateCreateOrUpdateRequest
from openapi_server.models.email_template_get200_response import EmailTemplateGet200Response
from openapi_server.models.email_template_list_by_service_default_response import EmailTemplateListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_email_template_create_or_update(client):
    """Test case for email_template_create_or_update

    
    """
    parameters = openapi_server.EmailTemplateCreateOrUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/templates/{template_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', template_name='template_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_template_delete(client):
    """Test case for email_template_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/templates/{template_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', template_name='template_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_template_get(client):
    """Test case for email_template_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/templates/{template_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', template_name='template_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_template_get_entity_tag(client):
    """Test case for email_template_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/templates/{template_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', template_name='template_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_template_update(client):
    """Test case for email_template_update

    
    """
    parameters = openapi_server.EmailTemplateCreateOrUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/templates/{template_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', template_name='template_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

