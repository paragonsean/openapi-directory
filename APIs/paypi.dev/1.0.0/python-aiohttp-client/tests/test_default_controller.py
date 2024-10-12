# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_code_post200_response import CheckCodePost200Response
from openapi_server.models.check_code_post401_response import CheckCodePost401Response
from openapi_server.models.check_code_post403_response import CheckCodePost403Response
from openapi_server.models.check_code_post_request import CheckCodePostRequest
from openapi_server.models.send_code_post200_response import SendCodePost200Response
from openapi_server.models.send_code_post400_response import SendCodePost400Response
from openapi_server.models.send_code_post_request import SendCodePostRequest


pytestmark = pytest.mark.asyncio

async def test_check_code_post(client):
    """Test case for check_code_post

    Check verification code
    """
    body = openapi_server.CheckCodePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/checkCode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_code_post(client):
    """Test case for send_code_post

    Send verification code
    """
    body = {"email":"test@test.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sendCode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

