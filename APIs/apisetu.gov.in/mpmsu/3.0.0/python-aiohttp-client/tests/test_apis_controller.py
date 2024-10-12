# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.micer400_response import Micer400Response
from openapi_server.models.micer401_response import Micer401Response
from openapi_server.models.micer404_response import Micer404Response
from openapi_server.models.micer500_response import Micer500Response
from openapi_server.models.micer502_response import Micer502Response
from openapi_server.models.micer503_response import Micer503Response
from openapi_server.models.micer504_response import Micer504Response
from openapi_server.models.micer_request import MicerRequest


pytestmark = pytest.mark.asyncio

async def test_micer(client):
    """Test case for micer

    Migration Certificate
    """
    body = openapi_server.MicerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mpmsu/v3/micer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pvcer(client):
    """Test case for pvcer

    Provisional Certificate
    """
    body = openapi_server.MicerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mpmsu/v3/pvcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

