# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_started_dto import ActionStartedDTO
from openapi_server.models.macro_request_dto import MacroRequestDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_run(client):
    """Test case for run

    Executes a macro.
    """
    body = /home-api/assets/examples/macros/runMacroAsynchronously.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/macros/{macro_id}/run'.format(macro_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

