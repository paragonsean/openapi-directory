# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dpcer400_response import Dpcer400Response
from openapi_server.models.dpcer401_response import Dpcer401Response
from openapi_server.models.dpcer404_response import Dpcer404Response
from openapi_server.models.dpcer500_response import Dpcer500Response
from openapi_server.models.dpcer502_response import Dpcer502Response
from openapi_server.models.dpcer503_response import Dpcer503Response
from openapi_server.models.dpcer504_response import Dpcer504Response
from openapi_server.models.dpcer_request import DpcerRequest


pytestmark = pytest.mark.asyncio

async def test_dpcer(client):
    """Test case for dpcer

    Dependency Certificate
    """
    body = openapi_server.DpcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sainikwelfarepud/v3/dpcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

