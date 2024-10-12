# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_error import AuthError
from openapi_server.models.error import Error
from openapi_server.models.locate import Locate
from openapi_server.models.post_locate200_response import PostLocate200Response


pytestmark = pytest.mark.asyncio

async def test_post_locate(client):
    """Test case for post_locate

    Location query
    """
    body = {"client":{"manufacturer":"Lemon","model":"Flagship X1","name":"FinderApp","version":"2.0.31"},"lte":[{"cid":2898945,"mcc":262,"mnc":2}],"wlan":[{"mac":"F4-55-95-11-2C-C1"}]}
    params = [('confidence', 68),
                    ('fallback', ['fallback_example']),
                    ('desired', ['desired_example']),
                    ('required', ['required_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_encoding': 'content_encoding_example',
        'x_request_id': 'x_request_id_example',
        'APIKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

