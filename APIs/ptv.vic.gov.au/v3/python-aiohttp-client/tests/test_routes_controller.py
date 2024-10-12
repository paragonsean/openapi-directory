# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_route_response import V3RouteResponse


pytestmark = pytest.mark.asyncio

async def test_routes_one_or_more_routes(client):
    """Test case for routes_one_or_more_routes

    View route names and numbers for all routes
    """
    params = [('route_types', [56]),
                    ('route_name', 'route_name_example'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/routes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routes_route_from_id(client):
    """Test case for routes_route_from_id

    View route name and number for specific route ID
    """
    params = [('include_geopath', True),
                    ('geopath_utc', '2013-10-20T19:20:30+01:00'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/routes/{route_id}'.format(route_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

