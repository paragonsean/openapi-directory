# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server.models.shortlink_request import ShortlinkRequest
from openapi_server.models.shortlink_response import ShortlinkResponse


pytestmark = pytest.mark.asyncio

async def test_add_shortlink(client):
    """Test case for add_shortlink

    add a shortlink
    """
    body = {"keyid":"keyid","shortlink":"shortlink"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/cgi-bin/shortlink',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

