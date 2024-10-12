# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.kecer400_response import Kecer400Response
from openapi_server.models.kecer401_response import Kecer401Response
from openapi_server.models.kecer404_response import Kecer404Response
from openapi_server.models.kecer500_response import Kecer500Response
from openapi_server.models.kecer502_response import Kecer502Response
from openapi_server.models.kecer503_response import Kecer503Response
from openapi_server.models.kecer504_response import Kecer504Response
from openapi_server.models.kecer_request import KecerRequest
from openapi_server.models.tapcn_request import TapcnRequest
from openapi_server.models.tdlcs_request import TdlcsRequest


pytestmark = pytest.mark.asyncio

async def test_kecer(client):
    """Test case for kecer

    Khatha Extract / Certificate
    """
    body = openapi_server.KecerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/municipaladmin/v3/kecer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tapcn(client):
    """Test case for tapcn

    New Tap Connection
    """
    body = openapi_server.TapcnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/municipaladmin/v3/tapcn/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tdlcs(client):
    """Test case for tdlcs

    Trade License/ Certificate
    """
    body = openapi_server.TdlcsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/municipaladmin/v3/tdlcs/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ugdcn(client):
    """Test case for ugdcn

    Jalanidhi - New UGD Connection
    """
    body = openapi_server.TapcnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/municipaladmin/v3/ugdcn/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

