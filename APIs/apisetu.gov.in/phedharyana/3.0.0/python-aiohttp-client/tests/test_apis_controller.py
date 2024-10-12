# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.etcer400_response import Etcer400Response
from openapi_server.models.etcer401_response import Etcer401Response
from openapi_server.models.etcer404_response import Etcer404Response
from openapi_server.models.etcer500_response import Etcer500Response
from openapi_server.models.etcer502_response import Etcer502Response
from openapi_server.models.etcer503_response import Etcer503Response
from openapi_server.models.etcer504_response import Etcer504Response
from openapi_server.models.etcer_request import EtcerRequest
from openapi_server.models.govid_request import GovidRequest
from openapi_server.models.sicer_request import SicerRequest


pytestmark = pytest.mark.asyncio

async def test_etcer(client):
    """Test case for etcer

    Enlistment Certificate
    """
    body = openapi_server.EtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/phedharyana/v3/etcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_govid(client):
    """Test case for govid

    ID Card
    """
    body = openapi_server.GovidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/phedharyana/v3/govid/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sicer(client):
    """Test case for sicer

    Sanction Letter/ Certificate
    """
    body = openapi_server.SicerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/phedharyana/v3/sicer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

