# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.login_dto import LoginDTO


pytestmark = pytest.mark.asyncio

async def test_auth_login(client):
    """Test case for auth_login

    Authenticate and provide token for autherizations.             
    """
    body = {"remember":True,"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Auth/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

