# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.escer400_response import Escer400Response
from openapi_server.models.escer401_response import Escer401Response
from openapi_server.models.escer404_response import Escer404Response
from openapi_server.models.escer500_response import Escer500Response
from openapi_server.models.escer502_response import Escer502Response
from openapi_server.models.escer503_response import Escer503Response
from openapi_server.models.escer504_response import Escer504Response
from openapi_server.models.escer_request import EscerRequest
from openapi_server.models.skcer_request import SkcerRequest


pytestmark = pytest.mark.asyncio

async def test_escer(client):
    """Test case for escer

    Executive Skill Enhancement Certificate
    """
    body = openapi_server.EscerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/nsdcindia/v3/escer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skcer(client):
    """Test case for skcer

    Skill Certificate
    """
    body = openapi_server.SkcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/nsdcindia/v3/skcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

