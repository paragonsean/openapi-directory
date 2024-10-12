# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_mobile_authorization_code_request import CreateMobileAuthorizationCodeRequest
from openapi_server.models.create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse


pytestmark = pytest.mark.asyncio

async def test_create_mobile_authorization_code(client):
    """Test case for create_mobile_authorization_code

    CreateMobileAuthorizationCode
    """
    body = {"request_body":{"location_id":"YOUR_LOCATION_ID"},"request_url":"/mobile/authorization-code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/mobile/authorization-code',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

