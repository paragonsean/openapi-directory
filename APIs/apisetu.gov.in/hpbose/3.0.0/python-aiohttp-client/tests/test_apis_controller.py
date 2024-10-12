# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hvcer400_response import Hvcer400Response
from openapi_server.models.hvcer401_response import Hvcer401Response
from openapi_server.models.hvcer404_response import Hvcer404Response
from openapi_server.models.hvcer500_response import Hvcer500Response
from openapi_server.models.hvcer502_response import Hvcer502Response
from openapi_server.models.hvcer503_response import Hvcer503Response
from openapi_server.models.hvcer504_response import Hvcer504Response
from openapi_server.models.hvcer_request import HvcerRequest


pytestmark = pytest.mark.asyncio

async def test_hvcer(client):
    """Test case for hvcer

    Class XII Provisional Certificate
    """
    body = openapi_server.HvcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hpbose/v3/hvcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_svcer(client):
    """Test case for svcer

    Class X Provisional Certificate
    """
    body = openapi_server.HvcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hpbose/v3/svcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

