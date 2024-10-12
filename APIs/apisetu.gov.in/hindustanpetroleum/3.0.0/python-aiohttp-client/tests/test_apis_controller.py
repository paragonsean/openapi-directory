# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lpgsv400_response import Lpgsv400Response
from openapi_server.models.lpgsv401_response import Lpgsv401Response
from openapi_server.models.lpgsv404_response import Lpgsv404Response
from openapi_server.models.lpgsv500_response import Lpgsv500Response
from openapi_server.models.lpgsv502_response import Lpgsv502Response
from openapi_server.models.lpgsv503_response import Lpgsv503Response
from openapi_server.models.lpgsv504_response import Lpgsv504Response
from openapi_server.models.lpgsv_request import LpgsvRequest


pytestmark = pytest.mark.asyncio

async def test_lpgsv(client):
    """Test case for lpgsv

    LPG Subscription Voucher
    """
    body = openapi_server.LpgsvRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hindustanpetroleum/v3/lpgsv/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

