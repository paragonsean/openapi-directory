# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hscer400_response import Hscer400Response
from openapi_server.models.hscer401_response import Hscer401Response
from openapi_server.models.hscer404_response import Hscer404Response
from openapi_server.models.hscer500_response import Hscer500Response
from openapi_server.models.hscer502_response import Hscer502Response
from openapi_server.models.hscer503_response import Hscer503Response
from openapi_server.models.hscer504_response import Hscer504Response
from openapi_server.models.hscer_request import HscerRequest


pytestmark = pytest.mark.asyncio

async def test_hscer(client):
    """Test case for hscer

    Class XII Marksheet
    """
    body = openapi_server.HscerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mbose/v3/hscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sscer(client):
    """Test case for sscer

    Class X Marksheet
    """
    body = openapi_server.HscerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mbose/v3/sscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

