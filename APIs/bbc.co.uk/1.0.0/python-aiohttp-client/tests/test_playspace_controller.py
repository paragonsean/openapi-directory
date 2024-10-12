# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.playspace_container import PlayspaceContainer


pytestmark = pytest.mark.asyncio

async def test_get_container(client):
    """Test case for get_container

    Playspace Container by ID
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/playspace/containers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggest_container(client):
    """Test case for suggest_container

    Suggested Playspace Container
    """
    params = [('previous_pid', 'previous_pid_example'),
                    ('previous_container', 'previous_container_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/playspace/containers/suggested',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

