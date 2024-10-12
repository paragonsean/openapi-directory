# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provider_operations_metadata import ProviderOperationsMetadata
from openapi_server.models.provider_operations_metadata_list_result import ProviderOperationsMetadataListResult


pytestmark = pytest.mark.asyncio

async def test_provider_operations_metadata_get(client):
    """Test case for provider_operations_metadata_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'resourceTypes')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/providerOperations/{resource_provider_namespace}'.format(resource_provider_namespace='resource_provider_namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provider_operations_metadata_list(client):
    """Test case for provider_operations_metadata_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'resourceTypes')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/providerOperations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

