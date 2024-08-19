# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transformation import Transformation


pytestmark = pytest.mark.asyncio

async def test_transformations_create_or_replace(client):
    """Test case for transformations_create_or_replace

    
    """
    transformation = {"properties":{"streamingUnits":0,"query":"query","etag":"etag"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/transformations/{transformation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', transformation_name='transformation_name_example'),
        headers=headers,
        json=transformation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transformations_get(client):
    """Test case for transformations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/transformations/{transformation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', transformation_name='transformation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transformations_update(client):
    """Test case for transformations_update

    
    """
    transformation = {"properties":{"streamingUnits":0,"query":"query","etag":"etag"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StreamAnalytics/streamingjobs/{job_name}/transformations/{transformation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example', transformation_name='transformation_name_example'),
        headers=headers,
        json=transformation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

