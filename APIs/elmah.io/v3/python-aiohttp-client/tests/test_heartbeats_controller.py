# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_heartbeat import CreateHeartbeat


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_heartbeats_create(client):
    """Test case for heartbeats_create

    Create a new heartbeat.
    """
    body = {"result":"result","reason":"reason","took":0,"application":"application","version":"version"}
    headers = { 
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/heartbeats/{log_id}/{id}'.format(id='id_example', log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

