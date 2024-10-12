# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.resource_change_data import ResourceChangeData
from openapi_server.models.resource_change_details_request_parameters import ResourceChangeDetailsRequestParameters
from openapi_server.models.resource_change_list import ResourceChangeList
from openapi_server.models.resource_changes_request_parameters import ResourceChangesRequestParameters


pytestmark = pytest.mark.asyncio

async def test_resource_change_details(client):
    """Test case for resource_change_details

    
    """
    parameters = {"resourceId":"resourceId","changeId":"changeId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ResourceGraph/resourceChangeDetails',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_changes(client):
    """Test case for resource_changes

    
    """
    parameters = {"resourceId":"resourceId","$top":81,"$skipToken":"$skipToken","interval":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ResourceGraph/resourceChanges',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

