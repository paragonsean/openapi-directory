# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mrcer400_response import Mrcer400Response
from openapi_server.models.mrcer401_response import Mrcer401Response
from openapi_server.models.mrcer404_response import Mrcer404Response
from openapi_server.models.mrcer500_response import Mrcer500Response
from openapi_server.models.mrcer502_response import Mrcer502Response
from openapi_server.models.mrcer503_response import Mrcer503Response
from openapi_server.models.mrcer504_response import Mrcer504Response
from openapi_server.models.mrcer_request import MrcerRequest


pytestmark = pytest.mark.asyncio

async def test_mrcer(client):
    """Test case for mrcer

    Merit Certificate
    """
    body = openapi_server.MrcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/asrb/v3/mrcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

