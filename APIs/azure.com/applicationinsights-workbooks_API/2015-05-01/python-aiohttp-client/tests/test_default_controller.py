# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workbook import Workbook
from openapi_server.models.workbook_error import WorkbookError
from openapi_server.models.workbooks_list_result import WorkbooksListResult


pytestmark = pytest.mark.asyncio

async def test_workbooks_create_or_update(client):
    """Test case for workbooks_create_or_update

    
    """
    workbook_properties = {"kind":"user","properties":{"serializedData":"serializedData","kind":"shared","name":"name","category":"category","timeModified":"timeModified","userId":"userId","version":"version","sourceResourceId":"sourceResourceId","workbookId":"workbookId","tags":["tags","tags"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooks/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=workbook_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbooks_delete(client):
    """Test case for workbooks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooks/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbooks_get(client):
    """Test case for workbooks_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooks/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbooks_list_by_resource_group(client):
    """Test case for workbooks_list_by_resource_group

    
    """
    params = [('category', 'category_example'),
                    ('tags', ['tags_example']),
                    ('canFetchContent', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workbooks_update(client):
    """Test case for workbooks_update

    
    """
    workbook_properties = {"kind":"user","properties":{"serializedData":"serializedData","kind":"shared","name":"name","category":"category","timeModified":"timeModified","userId":"userId","version":"version","sourceResourceId":"sourceResourceId","workbookId":"workbookId","tags":["tags","tags"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroup/{resource_group_name}/providers/microsoft.insights/workbooks/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=workbook_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

