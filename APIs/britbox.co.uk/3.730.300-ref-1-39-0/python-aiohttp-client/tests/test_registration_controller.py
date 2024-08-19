# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.registration_request import RegistrationRequest
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    
    """
    body = {"firstName":"firstName","lastName":"lastName","marketing":True,"password":"password","pin":"pin","languageCode":"languageCode","email":"email","segments":["segments","segments"]}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/register',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

