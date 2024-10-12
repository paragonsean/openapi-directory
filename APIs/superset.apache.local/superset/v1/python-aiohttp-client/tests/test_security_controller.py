# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.security_csrf_token_get200_response import SecurityCsrfTokenGet200Response
from openapi_server.models.security_login_post200_response import SecurityLoginPost200Response
from openapi_server.models.security_login_post_request import SecurityLoginPostRequest
from openapi_server.models.security_refresh_post200_response import SecurityRefreshPost200Response


pytestmark = pytest.mark.asyncio

async def test_security_csrf_token_get(client):
    """Test case for security_csrf_token_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/security/csrf_token/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_login_post(client):
    """Test case for security_login_post

    
    """
    body = openapi_server.SecurityLoginPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/security/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_refresh_post(client):
    """Test case for security_refresh_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/security/refresh',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

