# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.queue_build_request import QueueBuildRequest
from openapi_server.models.source_upload_definition import SourceUploadDefinition


pytestmark = pytest.mark.asyncio

async def test_registries_get_build_source_upload_url(client):
    """Test case for registries_get_build_source_upload_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/getBuildSourceUploadUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registries_queue_build(client):
    """Test case for registries_queue_build

    
    """
    build_request = {"type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/queueBuild'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        json=build_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

