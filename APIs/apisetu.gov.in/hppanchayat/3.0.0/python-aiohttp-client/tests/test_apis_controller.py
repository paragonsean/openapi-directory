# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fmcer400_response import Fmcer400Response
from openapi_server.models.fmcer401_response import Fmcer401Response
from openapi_server.models.fmcer404_response import Fmcer404Response
from openapi_server.models.fmcer500_response import Fmcer500Response
from openapi_server.models.fmcer502_response import Fmcer502Response
from openapi_server.models.fmcer503_response import Fmcer503Response
from openapi_server.models.fmcer504_response import Fmcer504Response
from openapi_server.models.fmcer_request import FmcerRequest


pytestmark = pytest.mark.asyncio

async def test_fmcer(client):
    """Test case for fmcer

    Family Membership Certificate
    """
    body = openapi_server.FmcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hppanchayat/v3/fmcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

