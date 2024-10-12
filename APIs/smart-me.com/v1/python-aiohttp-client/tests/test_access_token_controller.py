# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_to_put import AccessTokenToPut


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_access_token_put(client):
    """Test case for access_token_put

    Creates a Access Token to write on a Card (e.g. NFC)
    """
    body = {"UserId":6,"CardId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/AccessToken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

