# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vochse400_response import Vochse400Response
from openapi_server.models.vochse401_response import Vochse401Response
from openapi_server.models.vochse404_response import Vochse404Response
from openapi_server.models.vochse500_response import Vochse500Response
from openapi_server.models.vochse502_response import Vochse502Response
from openapi_server.models.vochse503_response import Vochse503Response
from openapi_server.models.vochse504_response import Vochse504Response
from openapi_server.models.vochse_request import VochseRequest


pytestmark = pytest.mark.asyncio

async def test_vochse(client):
    """Test case for vochse

    Vocational Higher Secondary
    """
    body = openapi_server.VochseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vhseker/v3/vochse/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

