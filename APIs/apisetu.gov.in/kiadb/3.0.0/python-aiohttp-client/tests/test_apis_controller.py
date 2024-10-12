# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alltr400_response import Alltr400Response
from openapi_server.models.alltr401_response import Alltr401Response
from openapi_server.models.alltr404_response import Alltr404Response
from openapi_server.models.alltr500_response import Alltr500Response
from openapi_server.models.alltr502_response import Alltr502Response
from openapi_server.models.alltr503_response import Alltr503Response
from openapi_server.models.alltr504_response import Alltr504Response
from openapi_server.models.alltr_request import AlltrRequest


pytestmark = pytest.mark.asyncio

async def test_alltr(client):
    """Test case for alltr

    Allotment Letter
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/alltr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bknoc(client):
    """Test case for bknoc

    NOC For Banks
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/bknoc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bpcer(client):
    """Test case for bpcer

    Building Plan
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/bpcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cfltr(client):
    """Test case for cfltr

    Confirmatory Letter
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/cfltr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lcsag(client):
    """Test case for lcsag

    Lease cum Sale Agreement
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/lcsag/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pscer(client):
    """Test case for pscer

    Possession Certificate
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/pscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_psnoc(client):
    """Test case for psnoc

    NOC for New Power Supply
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/psnoc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wtrbl(client):
    """Test case for wtrbl

    Water Bill/ Connection
    """
    body = openapi_server.AlltrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kiadb/v3/wtrbl/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

