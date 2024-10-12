# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rdcer400_response import Rdcer400Response
from openapi_server.models.rdcer401_response import Rdcer401Response
from openapi_server.models.rdcer404_response import Rdcer404Response
from openapi_server.models.rdcer500_response import Rdcer500Response
from openapi_server.models.rdcer502_response import Rdcer502Response
from openapi_server.models.rdcer503_response import Rdcer503Response
from openapi_server.models.rdcer504_response import Rdcer504Response
from openapi_server.models.rdcer_request import RdcerRequest
from openapi_server.models.ror1b_request import Ror1bRequest


pytestmark = pytest.mark.asyncio

async def test_rdcer(client):
    """Test case for rdcer

    Copy of Registered Deed
    """
    body = openapi_server.RdcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/revenueodisha/v3/rdcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ror1b(client):
    """Test case for ror1b

    Records of Rights
    """
    body = openapi_server.Ror1bRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/revenueodisha/v3/ror1b/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

