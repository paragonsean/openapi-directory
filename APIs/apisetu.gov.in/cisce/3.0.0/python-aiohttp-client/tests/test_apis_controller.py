# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hpcer400_response import Hpcer400Response
from openapi_server.models.hpcer401_response import Hpcer401Response
from openapi_server.models.hpcer404_response import Hpcer404Response
from openapi_server.models.hpcer500_response import Hpcer500Response
from openapi_server.models.hpcer502_response import Hpcer502Response
from openapi_server.models.hpcer503_response import Hpcer503Response
from openapi_server.models.hpcer504_response import Hpcer504Response
from openapi_server.models.hpcer_request import HpcerRequest


pytestmark = pytest.mark.asyncio

async def test_hpcer(client):
    """Test case for hpcer

    Class XII Passing Certificate
    """
    body = openapi_server.HpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cisce/v3/hpcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hscer(client):
    """Test case for hscer

    Class XII Marksheet
    """
    body = openapi_server.HpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cisce/v3/hscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hsmgr(client):
    """Test case for hsmgr

    Class XII Migration Certificate
    """
    body = openapi_server.HpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cisce/v3/hsmgr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spcer(client):
    """Test case for spcer

    Class X Passing Certificate
    """
    body = openapi_server.HpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cisce/v3/spcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sscer(client):
    """Test case for sscer

    Class X Marksheet
    """
    body = openapi_server.HpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cisce/v3/sscer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

