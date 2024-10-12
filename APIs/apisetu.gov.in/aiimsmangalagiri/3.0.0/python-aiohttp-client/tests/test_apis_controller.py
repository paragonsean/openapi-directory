# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.labrp400_response import Labrp400Response
from openapi_server.models.labrp401_response import Labrp401Response
from openapi_server.models.labrp404_response import Labrp404Response
from openapi_server.models.labrp500_response import Labrp500Response
from openapi_server.models.labrp502_response import Labrp502Response
from openapi_server.models.labrp503_response import Labrp503Response
from openapi_server.models.labrp504_response import Labrp504Response
from openapi_server.models.labrp_request import LabrpRequest


pytestmark = pytest.mark.asyncio

async def test_labrp(client):
    """Test case for labrp

    Clinical Laboratory Report
    """
    body = openapi_server.LabrpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/aiimsmangalagiri/v3/labrp/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

