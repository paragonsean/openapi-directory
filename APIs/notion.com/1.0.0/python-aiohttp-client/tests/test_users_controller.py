# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.retrieve_a_user200_response import RetrieveAUser200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_retrieve_a_user(client):
    """Test case for retrieve_a_user

    Retrieve a user
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{id}'.format(id='{{USER_ID}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

