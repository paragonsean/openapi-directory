# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alsfc400_response import Alsfc400Response
from openapi_server.models.alsfc401_response import Alsfc401Response
from openapi_server.models.alsfc404_response import Alsfc404Response
from openapi_server.models.alsfc500_response import Alsfc500Response
from openapi_server.models.alsfc502_response import Alsfc502Response
from openapi_server.models.alsfc503_response import Alsfc503Response
from openapi_server.models.alsfc504_response import Alsfc504Response
from openapi_server.models.alsfc_request import AlsfcRequest


pytestmark = pytest.mark.asyncio

async def test_alsfc(client):
    """Test case for alsfc

    Application/ License for Factory
    """
    body = openapi_server.AlsfcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pblabour/v3/alsfc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clcer(client):
    """Test case for clcer

    Registration Certificate for Contract Labour License
    """
    body = openapi_server.AlsfcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pblabour/v3/clcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_srcer(client):
    """Test case for srcer

    Registration Certificate of Shops And Commercial Establishment
    """
    body = openapi_server.AlsfcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pblabour/v3/srcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

