# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_sovereignty_campaigns200_ok import GetSovereigntyCampaigns200Ok
from openapi_server.models.get_sovereignty_map200_ok import GetSovereigntyMap200Ok
from openapi_server.models.get_sovereignty_structures200_ok import GetSovereigntyStructures200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_sovereignty_campaigns(client):
    """Test case for get_sovereignty_campaigns

    List sovereignty campaigns
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/sovereignty/campaigns/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sovereignty_map(client):
    """Test case for get_sovereignty_map

    List sovereignty of systems
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/sovereignty/map/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sovereignty_structures(client):
    """Test case for get_sovereignty_structures

    List sovereignty structures
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/sovereignty/structures/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

