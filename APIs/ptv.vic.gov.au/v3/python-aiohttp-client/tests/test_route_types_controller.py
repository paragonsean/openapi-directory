# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_route_types_response import V3RouteTypesResponse


pytestmark = pytest.mark.asyncio

async def test_route_types_get_route_types(client):
    """Test case for route_types_get_route_types

    View all route types and their names
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/route_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

