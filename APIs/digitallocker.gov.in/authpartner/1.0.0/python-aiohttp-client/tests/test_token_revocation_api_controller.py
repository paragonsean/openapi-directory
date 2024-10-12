# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_token_revocation_id_request import GetTokenRevocationIdRequest


pytestmark = pytest.mark.asyncio

async def test_get_token_revocation_id(client):
    """Test case for get_token_revocation_id

    Revoke Token.
    """
    body = openapi_server.GetTokenRevocationIdRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

