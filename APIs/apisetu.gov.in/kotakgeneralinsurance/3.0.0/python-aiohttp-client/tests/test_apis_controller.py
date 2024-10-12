# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cripc400_response import Cripc400Response
from openapi_server.models.cripc401_response import Cripc401Response
from openapi_server.models.cripc404_response import Cripc404Response
from openapi_server.models.cripc500_response import Cripc500Response
from openapi_server.models.cripc502_response import Cripc502Response
from openapi_server.models.cripc503_response import Cripc503Response
from openapi_server.models.cripc504_response import Cripc504Response
from openapi_server.models.cripc_request import CripcRequest


pytestmark = pytest.mark.asyncio

async def test_cripc(client):
    """Test case for cripc

    Insurance Policy - Car
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/cripc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cvipc(client):
    """Test case for cvipc

    Insurance Policy - Commercial Vehicle
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/cvipc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gicer(client):
    """Test case for gicer

    Insurance Policy - Group
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/gicer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hlipc(client):
    """Test case for hlipc

    Insurance Policy - Health
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/hlipc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hmipc(client):
    """Test case for hmipc

    Insurance Policy - Home
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/hmipc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_twipc(client):
    """Test case for twipc

    Insurance Policy - Two Wheeler
    """
    body = openapi_server.CripcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kotakgeneralinsurance/v3/twipc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

