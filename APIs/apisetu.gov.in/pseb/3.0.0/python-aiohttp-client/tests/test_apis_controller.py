# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cemst400_response import Cemst400Response
from openapi_server.models.cemst401_response import Cemst401Response
from openapi_server.models.cemst404_response import Cemst404Response
from openapi_server.models.cemst500_response import Cemst500Response
from openapi_server.models.cemst502_response import Cemst502Response
from openapi_server.models.cemst503_response import Cemst503Response
from openapi_server.models.cemst504_response import Cemst504Response
from openapi_server.models.cemst_request import CemstRequest


pytestmark = pytest.mark.asyncio

async def test_cemst(client):
    """Test case for cemst

    Class VIII Marksheet
    """
    body = openapi_server.CemstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pseb/v3/cemst/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cfmst(client):
    """Test case for cfmst

    Class V Marksheet
    """
    body = openapi_server.CemstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pseb/v3/cfmst/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hscer(client):
    """Test case for hscer

    Class XII Marksheet
    """
    body = openapi_server.CemstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pseb/v3/hscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_micer(client):
    """Test case for micer

    Migration Certificate
    """
    body = openapi_server.CemstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pseb/v3/micer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sscer(client):
    """Test case for sscer

    Class X Marksheet
    """
    body = openapi_server.CemstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pseb/v3/sscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

