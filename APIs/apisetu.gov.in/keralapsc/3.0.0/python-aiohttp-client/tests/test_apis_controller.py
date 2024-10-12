# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.otcer400_response import Otcer400Response
from openapi_server.models.otcer401_response import Otcer401Response
from openapi_server.models.otcer404_response import Otcer404Response
from openapi_server.models.otcer500_response import Otcer500Response
from openapi_server.models.otcer502_response import Otcer502Response
from openapi_server.models.otcer503_response import Otcer503Response
from openapi_server.models.otcer504_response import Otcer504Response
from openapi_server.models.otcer_request import OtcerRequest


pytestmark = pytest.mark.asyncio

async def test_otcer(client):
    """Test case for otcer

    OTV Certificate
    """
    body = openapi_server.OtcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/keralapsc/v3/otcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

