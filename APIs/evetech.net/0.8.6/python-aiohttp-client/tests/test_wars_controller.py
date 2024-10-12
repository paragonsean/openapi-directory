# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_wars_war_id_killmails200_ok import GetWarsWarIdKillmails200Ok
from openapi_server.models.get_wars_war_id_killmails_unprocessable_entity import GetWarsWarIdKillmailsUnprocessableEntity
from openapi_server.models.get_wars_war_id_ok import GetWarsWarIdOk
from openapi_server.models.get_wars_war_id_unprocessable_entity import GetWarsWarIdUnprocessableEntity
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_wars(client):
    """Test case for get_wars

    List wars
    """
    params = [('datasource', tranquility),
                    ('max_war_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/wars/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wars_war_id(client):
    """Test case for get_wars_war_id

    Get war information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/wars/{war_id}'.format(war_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wars_war_id_killmails(client):
    """Test case for get_wars_war_id_killmails

    List kills for a war
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/wars/{war_id}/killmails'.format(war_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

