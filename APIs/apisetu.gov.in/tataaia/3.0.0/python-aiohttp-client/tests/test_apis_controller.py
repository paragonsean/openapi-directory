# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.licer400_response import Licer400Response
from openapi_server.models.licer401_response import Licer401Response
from openapi_server.models.licer404_response import Licer404Response
from openapi_server.models.licer500_response import Licer500Response
from openapi_server.models.licer502_response import Licer502Response
from openapi_server.models.licer503_response import Licer503Response
from openapi_server.models.licer504_response import Licer504Response
from openapi_server.models.licer_request import LicerRequest
from openapi_server.models.prcpt_request import PrcptRequest


pytestmark = pytest.mark.asyncio

async def test_licer(client):
    """Test case for licer

    Insurance Policy - Life
    """
    body = openapi_server.LicerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tataaia/v3/licer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prcpt(client):
    """Test case for prcpt

    Premium Receipt
    """
    body = openapi_server.PrcptRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tataaia/v3/prcpt/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

