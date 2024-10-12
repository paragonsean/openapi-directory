# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trcer400_response import Trcer400Response
from openapi_server.models.trcer401_response import Trcer401Response
from openapi_server.models.trcer404_response import Trcer404Response
from openapi_server.models.trcer500_response import Trcer500Response
from openapi_server.models.trcer502_response import Trcer502Response
from openapi_server.models.trcer503_response import Trcer503Response
from openapi_server.models.trcer504_response import Trcer504Response
from openapi_server.models.trcer_request import TrcerRequest


pytestmark = pytest.mark.asyncio

async def test_trcer(client):
    """Test case for trcer

    Transfer Certificate
    """
    body = openapi_server.TrcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/dbraitandaman/v3/trcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

