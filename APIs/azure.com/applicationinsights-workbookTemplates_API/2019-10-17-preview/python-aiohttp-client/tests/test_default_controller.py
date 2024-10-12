# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workbook_error import WorkbookError
from openapi_server.models.workbook_template import WorkbookTemplate
from openapi_server.models.workbook_template_update_parameters import WorkbookTemplateUpdateParameters
from openapi_server.models.workbook_templates_list_result import WorkbookTemplatesListResult


pytestmark = pytest.mark.asyncio

async def test_workbook_templates_create_or_update(client):
    """Test case for workbook_templates_create_or_update

    
    """
    workbook_template_properties = {"properties":{"author":"author","localized":{"key":[{"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}]},{"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}]}]},"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}],"priority":6}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooktemplates/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=workbook_template_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbook_templates_delete(client):
    """Test case for workbook_templates_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooktemplates/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbook_templates_get(client):
    """Test case for workbook_templates_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooktemplates/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbook_templates_list_by_resource_group(client):
    """Test case for workbook_templates_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooktemplates'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbook_templates_update(client):
    """Test case for workbook_templates_update

    
    """
    workbook_template_update_parameters = {"properties":{"author":"author","localized":{"key":[{"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}]},{"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}]}]},"templateData":"{}","galleries":[{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"},{"name":"name","category":"category","type":"type","order":0,"resourceType":"resourceType"}],"priority":6},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooktemplates/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=workbook_template_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

