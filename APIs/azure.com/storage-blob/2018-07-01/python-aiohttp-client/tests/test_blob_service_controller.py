# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blob_service_properties import BlobServiceProperties


pytestmark = pytest.mark.asyncio

async def test_blob_services_get_service_properties(client):
    """Test case for blob_services_get_service_properties

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/{blob_services_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', blob_services_name='blob_services_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_services_set_service_properties(client):
    """Test case for blob_services_set_service_properties

    
    """
    parameters = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/{blob_services_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', blob_services_name='blob_services_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

