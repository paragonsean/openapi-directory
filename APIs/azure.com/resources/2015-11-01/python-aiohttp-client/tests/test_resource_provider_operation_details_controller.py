# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_provider_operation_detail_list_result import ResourceProviderOperationDetailListResult


pytestmark = pytest.mark.asyncio

async def test_resource_provider_operation_details_list(client):
    """Test case for resource_provider_operation_details_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/{resource_provider_namespace}/operations'.format(resource_provider_namespace='resource_provider_namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

