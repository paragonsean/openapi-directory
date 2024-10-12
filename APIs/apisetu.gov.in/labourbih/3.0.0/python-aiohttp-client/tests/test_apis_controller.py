# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alimw400_response import Alimw400Response
from openapi_server.models.alimw401_response import Alimw401Response
from openapi_server.models.alimw404_response import Alimw404Response
from openapi_server.models.alimw500_response import Alimw500Response
from openapi_server.models.alimw502_response import Alimw502Response
from openapi_server.models.alimw503_response import Alimw503Response
from openapi_server.models.alimw504_response import Alimw504Response
from openapi_server.models.alimw_request import AlimwRequest


pytestmark = pytest.mark.asyncio

async def test_alimw(client):
    """Test case for alimw

    Application for License for Inter State Migrant Workmen
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/alimw/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alsbl(client):
    """Test case for alsbl

    Application/ License for Boilers
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/alsbl/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alsfc(client):
    """Test case for alsfc

    Application/ License for Factory
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/alsfc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apptu(client):
    """Test case for apptu

    Application realted to Trade Unions
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/apptu/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clcer(client):
    """Test case for clcer

    Registration Certificate for Contract Labour License
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/clcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_noocl(client):
    """Test case for noocl

    Notice of Closure
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/noocl/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_srcer(client):
    """Test case for srcer

    Registration Certificate of Shops And Commercial Establishment
    """
    body = openapi_server.AlimwRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/labourbih/v3/srcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

