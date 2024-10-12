# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.nncer400_response import Nncer400Response
from openapi_server.models.nncer401_response import Nncer401Response
from openapi_server.models.nncer404_response import Nncer404Response
from openapi_server.models.nncer500_response import Nncer500Response
from openapi_server.models.nncer502_response import Nncer502Response
from openapi_server.models.nncer503_response import Nncer503Response
from openapi_server.models.nncer504_response import Nncer504Response
from openapi_server.models.nncer_request import NncerRequest


pytestmark = pytest.mark.asyncio

async def test_nncer(client):
    """Test case for nncer

    Non-Encumbrance Certificate
    """
    body = openapi_server.NncerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/revenueassam/v3/nncer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

