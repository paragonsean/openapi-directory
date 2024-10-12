# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cocer400_response import Cocer400Response
from openapi_server.models.cocer401_response import Cocer401Response
from openapi_server.models.cocer404_response import Cocer404Response
from openapi_server.models.cocer500_response import Cocer500Response
from openapi_server.models.cocer502_response import Cocer502Response
from openapi_server.models.cocer503_response import Cocer503Response
from openapi_server.models.cocer504_response import Cocer504Response
from openapi_server.models.cocer_request import CocerRequest


pytestmark = pytest.mark.asyncio

async def test_cocer(client):
    """Test case for cocer

    Company Related Certificate
    """
    body = openapi_server.CocerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ktech/v3/cocer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rfcer(client):
    """Test case for rfcer

    Registration Certificate of Firm/ Company
    """
    body = openapi_server.CocerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ktech/v3/rfcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

