# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_image_upload_url_input import GetImageUploadUrlInput
from openapi_server.models.image_definition import ImageDefinition


pytestmark = pytest.mark.asyncio

async def test_images_get_upload_url_for_data(client):
    """Test case for images_get_upload_url_for_data

    
    """
    parameters = {"entityType":"entityType","relativePath":"relativePath","entityTypeName":"entityTypeName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/images/getDataImageUploadUrl'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_images_get_upload_url_for_entity_type(client):
    """Test case for images_get_upload_url_for_entity_type

    
    """
    parameters = {"entityType":"entityType","relativePath":"relativePath","entityTypeName":"entityTypeName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/images/getEntityTypeImageUploadUrl'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

