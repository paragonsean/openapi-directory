# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pecer400_response import Pecer400Response
from openapi_server.models.pecer401_response import Pecer401Response
from openapi_server.models.pecer404_response import Pecer404Response
from openapi_server.models.pecer500_response import Pecer500Response
from openapi_server.models.pecer502_response import Pecer502Response
from openapi_server.models.pecer503_response import Pecer503Response
from openapi_server.models.pecer504_response import Pecer504Response
from openapi_server.models.pecer_request import PecerRequest


pytestmark = pytest.mark.asyncio

async def test_pecer(client):
    """Test case for pecer

    Pension Certificate
    """
    body = openapi_server.PecerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bhavishya/v3/pecer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

