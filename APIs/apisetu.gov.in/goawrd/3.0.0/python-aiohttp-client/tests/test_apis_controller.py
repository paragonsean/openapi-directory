# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ercer400_response import Ercer400Response
from openapi_server.models.ercer401_response import Ercer401Response
from openapi_server.models.ercer404_response import Ercer404Response
from openapi_server.models.ercer500_response import Ercer500Response
from openapi_server.models.ercer502_response import Ercer502Response
from openapi_server.models.ercer503_response import Ercer503Response
from openapi_server.models.ercer504_response import Ercer504Response
from openapi_server.models.ercer_request import ErcerRequest


pytestmark = pytest.mark.asyncio

async def test_ercer(client):
    """Test case for ercer

    Registration Certificate of Establishment Employing Contract Labour
    """
    body = openapi_server.ErcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/goawrd/v3/ercer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pfdaw(client):
    """Test case for pfdaw

    Permission/ Certificate for Well
    """
    body = openapi_server.ErcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/goawrd/v3/pfdaw/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tpcer(client):
    """Test case for tpcer

    Permission/ Certificate for Transportation (Petroleum Products, Water etc.)
    """
    body = openapi_server.ErcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/goawrd/v3/tpcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

