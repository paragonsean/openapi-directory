# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tags_resource import TagsResource
from openapi_server.models.web_test import WebTest
from openapi_server.models.web_test_list_result import WebTestListResult


pytestmark = pytest.mark.asyncio

async def test_web_tests_create_or_update(client):
    """Test case for web_tests_create_or_update

    
    """
    web_test_definition = {"kind":"ping","properties":{"RetryEnabled":True,"Description":"Description","Configuration":{"WebTest":"WebTest"},"Timeout":6,"Kind":"ping","SyntheticMonitorId":"SyntheticMonitorId","Locations":[{"Id":"Id"},{"Id":"Id"}],"Enabled":True,"Frequency":0,"provisioningState":"provisioningState","Name":"Name"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/webtests/{web_test_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', web_test_name='web_test_name_example'),
        headers=headers,
        json=web_test_definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_delete(client):
    """Test case for web_tests_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/webtests/{web_test_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', web_test_name='web_test_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_get(client):
    """Test case for web_tests_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/webtests/{web_test_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', web_test_name='web_test_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_list(client):
    """Test case for web_tests_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Insights/webtests'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_list_by_component(client):
    """Test case for web_tests_list_by_component

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{component_name}/webtests'.format(component_name='component_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_list_by_resource_group(client):
    """Test case for web_tests_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/webtests'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_tests_update_tags(client):
    """Test case for web_tests_update_tags

    
    """
    web_test_tags = {"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/webtests/{web_test_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', web_test_name='web_test_name_example'),
        headers=headers,
        json=web_test_tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

