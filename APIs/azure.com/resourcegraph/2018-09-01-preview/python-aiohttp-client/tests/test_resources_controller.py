# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_resources(client):
    """Test case for resources

    
    """
    query = {"subscriptions":["subscriptions","subscriptions"],"query":"query","options":{"$skip":0,"$top":147,"$skipToken":"$skipToken"},"facets":[{"expression":"expression","options":{"filter":"filter","$top":81,"sortOrder":"desc","sortBy":"sortBy"}},{"expression":"expression","options":{"filter":"filter","$top":81,"sortOrder":"desc","sortBy":"sortBy"}}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ResourceGraph/resources',
        headers=headers,
        json=query,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

