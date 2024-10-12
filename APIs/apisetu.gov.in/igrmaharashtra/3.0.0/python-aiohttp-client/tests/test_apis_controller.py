# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.llcer400_response import Llcer400Response
from openapi_server.models.llcer401_response import Llcer401Response
from openapi_server.models.llcer404_response import Llcer404Response
from openapi_server.models.llcer500_response import Llcer500Response
from openapi_server.models.llcer502_response import Llcer502Response
from openapi_server.models.llcer503_response import Llcer503Response
from openapi_server.models.llcer504_response import Llcer504Response
from openapi_server.models.llcer_request import LlcerRequest


pytestmark = pytest.mark.asyncio

async def test_llcer(client):
    """Test case for llcer

    Leave and License Certificate
    """
    body = openapi_server.LlcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/igrmaharashtra/v3/llcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

