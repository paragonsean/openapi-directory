# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sscer400_response import Sscer400Response
from openapi_server.models.sscer401_response import Sscer401Response
from openapi_server.models.sscer404_response import Sscer404Response
from openapi_server.models.sscer500_response import Sscer500Response
from openapi_server.models.sscer502_response import Sscer502Response
from openapi_server.models.sscer503_response import Sscer503Response
from openapi_server.models.sscer504_response import Sscer504Response
from openapi_server.models.sscer_request import SscerRequest


pytestmark = pytest.mark.asyncio

async def test_sscer(client):
    """Test case for sscer

    Class X Marksheet
    """
    body = openapi_server.SscerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/biharboard/v3/sscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_svcer(client):
    """Test case for svcer

    Class X Provisional Certificate
    """
    body = openapi_server.SscerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/biharboard/v3/svcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

