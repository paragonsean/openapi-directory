# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.phcer400_response import Phcer400Response
from openapi_server.models.phcer401_response import Phcer401Response
from openapi_server.models.phcer404_response import Phcer404Response
from openapi_server.models.phcer500_response import Phcer500Response
from openapi_server.models.phcer502_response import Phcer502Response
from openapi_server.models.phcer503_response import Phcer503Response
from openapi_server.models.phcer504_response import Phcer504Response
from openapi_server.models.phcer_request import PhcerRequest
from openapi_server.models.rpcer_request import RpcerRequest


pytestmark = pytest.mark.asyncio

async def test_phcer(client):
    """Test case for phcer

    Pharmacist Registration Certificate
    """
    body = openapi_server.PhcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hpayushboard/v3/phcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rpcer(client):
    """Test case for rpcer

    Pharmacist Renewal certificate
    """
    body = openapi_server.RpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hpayushboard/v3/rpcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

