# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.egcer400_response import Egcer400Response
from openapi_server.models.egcer401_response import Egcer401Response
from openapi_server.models.egcer404_response import Egcer404Response
from openapi_server.models.egcer500_response import Egcer500Response
from openapi_server.models.egcer502_response import Egcer502Response
from openapi_server.models.egcer503_response import Egcer503Response
from openapi_server.models.egcer504_response import Egcer504Response
from openapi_server.models.egcer_request import EgcerRequest


pytestmark = pytest.mark.asyncio

async def test_egcer(client):
    """Test case for egcer

    Economically Backward In General Caste Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/egcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ewcer(client):
    """Test case for ewcer

    Economically Weaker Section Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/ewcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_incer(client):
    """Test case for incer

    Income Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/incer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lhcer(client):
    """Test case for lhcer

    Legal Heir Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/lhcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_obcer(client):
    """Test case for obcer

    OBC Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/obcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rscer(client):
    """Test case for rscer

    Residence Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/rscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shcer(client):
    """Test case for shcer

    SC/ST  Certificate
    """
    body = openapi_server.EgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/edistrictodishasp/v3/shcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

