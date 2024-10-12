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
from openapi_server.models.regrii_request import RegriiRequest


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
        path='/enibandhanjh/v3/rdcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regrii(client):
    """Test case for regrii

    ROR Register 2
    """
    body = openapi_server.RegriiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/enibandhanjh/v3/regrii/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rmcer(client):
    """Test case for rmcer

    Marriage Certificate
    """
    body = openapi_server.RegriiRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/enibandhanjh/v3/rmcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

