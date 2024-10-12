# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dgcer400_response import Dgcer400Response
from openapi_server.models.dgcer401_response import Dgcer401Response
from openapi_server.models.dgcer404_response import Dgcer404Response
from openapi_server.models.dgcer500_response import Dgcer500Response
from openapi_server.models.dgcer502_response import Dgcer502Response
from openapi_server.models.dgcer503_response import Dgcer503Response
from openapi_server.models.dgcer504_response import Dgcer504Response
from openapi_server.models.dgcer_request import DgcerRequest


pytestmark = pytest.mark.asyncio

async def test_dgcer(client):
    """Test case for dgcer

    Degree/ Diploma Certificate
    """
    body = openapi_server.DgcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/geetanjaliuniv/v3/dgcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

