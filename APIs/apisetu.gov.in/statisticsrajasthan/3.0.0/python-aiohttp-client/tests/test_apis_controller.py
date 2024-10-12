# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.btcer400_response import Btcer400Response
from openapi_server.models.btcer401_response import Btcer401Response
from openapi_server.models.btcer404_response import Btcer404Response
from openapi_server.models.btcer500_response import Btcer500Response
from openapi_server.models.btcer502_response import Btcer502Response
from openapi_server.models.btcer503_response import Btcer503Response
from openapi_server.models.btcer504_response import Btcer504Response
from openapi_server.models.btcer_request import BtcerRequest
from openapi_server.models.dtcer_request import DtcerRequest
from openapi_server.models.rmcer_request import RmcerRequest


pytestmark = pytest.mark.asyncio

async def test_btcer(client):
    """Test case for btcer

    Birth Certificate
    """
    body = openapi_server.BtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/statisticsrajasthan/v3/btcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dtcer(client):
    """Test case for dtcer

    Death Certificate
    """
    body = openapi_server.DtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/statisticsrajasthan/v3/dtcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rmcer(client):
    """Test case for rmcer

    Marriage Certificate
    """
    body = openapi_server.RmcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/statisticsrajasthan/v3/rmcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

