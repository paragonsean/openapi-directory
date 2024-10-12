# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_incursions200_ok import GetIncursions200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_incursions(client):
    """Test case for get_incursions

    List incursions
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/incursions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

