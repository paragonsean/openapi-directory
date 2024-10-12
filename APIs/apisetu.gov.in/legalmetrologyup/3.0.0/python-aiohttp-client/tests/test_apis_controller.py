# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delcs400_response import Delcs400Response
from openapi_server.models.delcs401_response import Delcs401Response
from openapi_server.models.delcs404_response import Delcs404Response
from openapi_server.models.delcs500_response import Delcs500Response
from openapi_server.models.delcs502_response import Delcs502Response
from openapi_server.models.delcs503_response import Delcs503Response
from openapi_server.models.delcs504_response import Delcs504Response
from openapi_server.models.delcs_request import DelcsRequest


pytestmark = pytest.mark.asyncio

async def test_delcs(client):
    """Test case for delcs

    Dealer License
    """
    body = openapi_server.DelcsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/legalmetrologyup/v3/delcs/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_malcs(client):
    """Test case for malcs

    Manufacturer License
    """
    body = openapi_server.DelcsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/legalmetrologyup/v3/malcs/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_palcs(client):
    """Test case for palcs

    Packers License
    """
    body = openapi_server.DelcsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/legalmetrologyup/v3/palcs/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relcs(client):
    """Test case for relcs

    Repairer License
    """
    body = openapi_server.DelcsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/legalmetrologyup/v3/relcs/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

