# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.podoc400_response import Podoc400Response
from openapi_server.models.podoc401_response import Podoc401Response
from openapi_server.models.podoc404_response import Podoc404Response
from openapi_server.models.podoc500_response import Podoc500Response
from openapi_server.models.podoc502_response import Podoc502Response
from openapi_server.models.podoc503_response import Podoc503Response
from openapi_server.models.podoc504_response import Podoc504Response
from openapi_server.models.podoc_request import PodocRequest


pytestmark = pytest.mark.asyncio

async def test_podoc(client):
    """Test case for podoc

    Policy Document
    """
    body = openapi_server.PodocRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/licindia/v3/podoc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

