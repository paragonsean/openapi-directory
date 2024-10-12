# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.skcer400_response import Skcer400Response
from openapi_server.models.skcer401_response import Skcer401Response
from openapi_server.models.skcer404_response import Skcer404Response
from openapi_server.models.skcer500_response import Skcer500Response
from openapi_server.models.skcer502_response import Skcer502Response
from openapi_server.models.skcer503_response import Skcer503Response
from openapi_server.models.skcer504_response import Skcer504Response
from openapi_server.models.skcer_request import SkcerRequest


pytestmark = pytest.mark.asyncio

async def test_skcer(client):
    """Test case for skcer

    Skill Certificate
    """
    body = openapi_server.SkcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/insvalsura/v3/skcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skmst(client):
    """Test case for skmst

    Skill Marksheet/ Score Card
    """
    body = openapi_server.SkcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/insvalsura/v3/skmst/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

