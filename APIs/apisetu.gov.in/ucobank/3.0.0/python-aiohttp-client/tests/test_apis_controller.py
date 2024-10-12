# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tdcer400_response import Tdcer400Response
from openapi_server.models.tdcer401_response import Tdcer401Response
from openapi_server.models.tdcer404_response import Tdcer404Response
from openapi_server.models.tdcer500_response import Tdcer500Response
from openapi_server.models.tdcer502_response import Tdcer502Response
from openapi_server.models.tdcer503_response import Tdcer503Response
from openapi_server.models.tdcer504_response import Tdcer504Response
from openapi_server.models.tdcer_request import TdcerRequest


pytestmark = pytest.mark.asyncio

async def test_tdcer(client):
    """Test case for tdcer

    TDS Certificate
    """
    body = openapi_server.TdcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ucobank/v3/tdcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

