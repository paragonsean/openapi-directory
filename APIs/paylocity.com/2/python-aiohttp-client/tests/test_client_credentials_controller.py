# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_client_secret import AddClientSecret
from openapi_server.models.client_credentials_response import ClientCredentialsResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_client_secret(client):
    """Test case for add_client_secret

    Obtain new client secret.
    """
    body = openapi_server.AddClientSecret()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/credentials/secrets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

