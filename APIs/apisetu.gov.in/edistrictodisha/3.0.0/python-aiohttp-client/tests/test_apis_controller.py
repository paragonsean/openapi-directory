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
        path='/edistrictodisha/v3/ctcer/certificate',
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
        path='/edistrictodisha/v3/ewcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lhcer(client):
    """Test case for lhcer

    Legal Heir Certificate
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
        path='/edistrictodisha/v3/lhcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_obcer(client):
    """Test case for obcer

    OBC Certificate
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
        path='/edistrictodisha/v3/obcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ror1b(client):
    """Test case for ror1b

    Records of Rights
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
        path='/edistrictodisha/v3/ror1b/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slcer(client):
    """Test case for slcer

    Solvency Certificate
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
        path='/edistrictodisha/v3/slcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

