# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ndcer400_response import Ndcer400Response
from openapi_server.models.ndcer401_response import Ndcer401Response
from openapi_server.models.ndcer404_response import Ndcer404Response
from openapi_server.models.ndcer500_response import Ndcer500Response
from openapi_server.models.ndcer502_response import Ndcer502Response
from openapi_server.models.ndcer503_response import Ndcer503Response
from openapi_server.models.ndcer504_response import Ndcer504Response
from openapi_server.models.ndcer_request import NdcerRequest


pytestmark = pytest.mark.asyncio

async def test_ndcer(client):
    """Test case for ndcer

    No Dues/ Objection Certificate
    """
    body = openapi_server.NdcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/npsailu/v3/ndcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

