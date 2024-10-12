# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.epfsc400_response import Epfsc400Response
from openapi_server.models.epfsc401_response import Epfsc401Response
from openapi_server.models.epfsc404_response import Epfsc404Response
from openapi_server.models.epfsc500_response import Epfsc500Response
from openapi_server.models.epfsc502_response import Epfsc502Response
from openapi_server.models.epfsc503_response import Epfsc503Response
from openapi_server.models.epfsc504_response import Epfsc504Response
from openapi_server.models.epfsc_request import EpfscRequest
from openapi_server.models.pecer_request import PecerRequest
from openapi_server.models.uncrd_request import UncrdRequest


pytestmark = pytest.mark.asyncio

async def test_epfsc(client):
    """Test case for epfsc

    Scheme Certificate
    """
    body = openapi_server.EpfscRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/epfindia/v3/epfsc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pecer(client):
    """Test case for pecer

    Pension Certificate
    """
    body = openapi_server.PecerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/epfindia/v3/pecer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uncrd(client):
    """Test case for uncrd

    UAN Card
    """
    body = openapi_server.UncrdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/epfindia/v3/uncrd/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

