# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.nbcer400_response import Nbcer400Response
from openapi_server.models.nbcer401_response import Nbcer401Response
from openapi_server.models.nbcer404_response import Nbcer404Response
from openapi_server.models.nbcer500_response import Nbcer500Response
from openapi_server.models.nbcer502_response import Nbcer502Response
from openapi_server.models.nbcer503_response import Nbcer503Response
from openapi_server.models.nbcer504_response import Nbcer504Response
from openapi_server.models.nbcer_request import NbcerRequest


pytestmark = pytest.mark.asyncio

async def test_nbcer(client):
    """Test case for nbcer

    NAC/Birth/Death Certificate
    """
    body = openapi_server.NbcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/saralharyana/v3/nbcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

