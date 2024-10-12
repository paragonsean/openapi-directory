# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.socer400_response import Socer400Response
from openapi_server.models.socer401_response import Socer401Response
from openapi_server.models.socer404_response import Socer404Response
from openapi_server.models.socer500_response import Socer500Response
from openapi_server.models.socer502_response import Socer502Response
from openapi_server.models.socer503_response import Socer503Response
from openapi_server.models.socer504_response import Socer504Response
from openapi_server.models.socer_request import SocerRequest


pytestmark = pytest.mark.asyncio

async def test_socer(client):
    """Test case for socer

    Educational/ Exam Registration Certificate
    """
    body = openapi_server.SocerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/gauhati/v3/socer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

