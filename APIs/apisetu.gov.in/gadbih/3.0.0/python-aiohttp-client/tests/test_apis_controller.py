# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ctcer400_response import Ctcer400Response
from openapi_server.models.ctcer401_response import Ctcer401Response
from openapi_server.models.ctcer404_response import Ctcer404Response
from openapi_server.models.ctcer500_response import Ctcer500Response
from openapi_server.models.ctcer502_response import Ctcer502Response
from openapi_server.models.ctcer503_response import Ctcer503Response
from openapi_server.models.ctcer504_response import Ctcer504Response
from openapi_server.models.ctcer_request import CtcerRequest


pytestmark = pytest.mark.asyncio

async def test_ctcer(client):
    """Test case for ctcer

    Caste Certificate
    """
    body = openapi_server.CtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/gadbih/v3/ctcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ewcer(client):
    """Test case for ewcer

    Economically Weaker Section Certificate
    """
    body = openapi_server.CtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/gadbih/v3/ewcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_incer(client):
    """Test case for incer

    Income Certificate
    """
    body = openapi_server.CtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/gadbih/v3/incer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rscer(client):
    """Test case for rscer

    Residence Certificate
    """
    body = openapi_server.CtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/gadbih/v3/rscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

