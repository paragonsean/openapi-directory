# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pvcer400_response import Pvcer400Response
from openapi_server.models.pvcer401_response import Pvcer401Response
from openapi_server.models.pvcer404_response import Pvcer404Response
from openapi_server.models.pvcer500_response import Pvcer500Response
from openapi_server.models.pvcer502_response import Pvcer502Response
from openapi_server.models.pvcer503_response import Pvcer503Response
from openapi_server.models.pvcer504_response import Pvcer504Response
from openapi_server.models.pvcer_request import PvcerRequest


pytestmark = pytest.mark.asyncio

async def test_pvcer(client):
    """Test case for pvcer

    Provisional Certificate
    """
    body = openapi_server.PvcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/kkhsou/v3/pvcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

