# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.get_validity200_response import GetValidity200Response


pytestmark = pytest.mark.asyncio

async def test_get_validity(client):
    """Test case for get_validity

    Validate API key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/validate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

