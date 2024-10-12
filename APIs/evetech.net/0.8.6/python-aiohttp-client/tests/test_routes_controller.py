# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_route_origin_destination_not_found import GetRouteOriginDestinationNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_route_origin_destination(client):
    """Test case for get_route_origin_destination

    Get route
    """
    params = [('avoid', [56]),
                    ('connections', [openapi_server.list[int]()]),
                    ('datasource', tranquility),
                    ('flag', shortest)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/route/{origin}/{destination}'.format(destination=56, origin=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

