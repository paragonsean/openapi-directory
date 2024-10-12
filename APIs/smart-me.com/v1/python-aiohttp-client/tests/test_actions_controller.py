# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_information import ActionInformation
from openapi_server.models.action_to_post import ActionToPost


pytestmark = pytest.mark.asyncio

async def test_actions_get(client):
    """Test case for actions_get

    Gets all available Actions of a Device
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Actions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_actions_post(client):
    """Test case for actions_post

    Set an action for the specified device.
    """
    body = {"Actions":[{"Value":0.8008281904610115,"ObisCode":"ObisCode"},{"Value":0.8008281904610115,"ObisCode":"ObisCode"}],"DeviceID":"DeviceID"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Actions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

