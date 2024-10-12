# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sslcr400_response import Sslcr400Response
from openapi_server.models.sslcr401_response import Sslcr401Response
from openapi_server.models.sslcr404_response import Sslcr404Response
from openapi_server.models.sslcr500_response import Sslcr500Response
from openapi_server.models.sslcr502_response import Sslcr502Response
from openapi_server.models.sslcr503_response import Sslcr503Response
from openapi_server.models.sslcr504_response import Sslcr504Response
from openapi_server.models.sslcr_request import SslcrRequest


pytestmark = pytest.mark.asyncio

async def test_sslcr(client):
    """Test case for sslcr

    Class X School Leaving Certificate
    """
    body = openapi_server.SslcrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pareekshabhavanker/v3/sslcr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

