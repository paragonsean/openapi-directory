# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.get_ssis_object_metadata_request import GetSsisObjectMetadataRequest
from openapi_server.models.integration_runtime_object_metadata_get200_response import IntegrationRuntimeObjectMetadataGet200Response
from openapi_server.models.ssis_object_metadata_status_response import SsisObjectMetadataStatusResponse


pytestmark = pytest.mark.asyncio

async def test_integration_runtime_object_metadata_get(client):
    """Test case for integration_runtime_object_metadata_get

    
    """
    get_metadata_request = {"metadataPath":"metadataPath"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/integrationRuntimes/{integration_runtime_name}/getObjectMetadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', integration_runtime_name='integration_runtime_name_example'),
        headers=headers,
        json=get_metadata_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_runtime_object_metadata_refresh(client):
    """Test case for integration_runtime_object_metadata_refresh

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/integrationRuntimes/{integration_runtime_name}/refreshObjectMetadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', integration_runtime_name='integration_runtime_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

