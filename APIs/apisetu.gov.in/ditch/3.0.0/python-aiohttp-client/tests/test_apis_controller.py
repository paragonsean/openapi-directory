# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.incer400_response import Incer400Response
from openapi_server.models.incer401_response import Incer401Response
from openapi_server.models.incer404_response import Incer404Response
from openapi_server.models.incer500_response import Incer500Response
from openapi_server.models.incer502_response import Incer502Response
from openapi_server.models.incer503_response import Incer503Response
from openapi_server.models.incer504_response import Incer504Response
from openapi_server.models.incer_request import IncerRequest
from openapi_server.models.sicrd_request import SicrdRequest


pytestmark = pytest.mark.asyncio

async def test_incer(client):
    """Test case for incer

    Income Certificate
    """
    body = openapi_server.IncerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ditch/v3/incer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rmcer(client):
    """Test case for rmcer

    Marriage Certificate
    """
    body = openapi_server.IncerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ditch/v3/rmcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rscer(client):
    """Test case for rscer

    Residence Certificate
    """
    body = openapi_server.IncerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ditch/v3/rscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sicrd(client):
    """Test case for sicrd

    Senior Citizen Identity Card/ Certificate
    """
    body = openapi_server.SicrdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ditch/v3/sicrd/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

