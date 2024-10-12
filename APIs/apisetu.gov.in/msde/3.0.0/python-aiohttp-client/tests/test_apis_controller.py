# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.iticr400_response import Iticr400Response
from openapi_server.models.iticr401_response import Iticr401Response
from openapi_server.models.iticr404_response import Iticr404Response
from openapi_server.models.iticr500_response import Iticr500Response
from openapi_server.models.iticr502_response import Iticr502Response
from openapi_server.models.iticr503_response import Iticr503Response
from openapi_server.models.iticr504_response import Iticr504Response
from openapi_server.models.iticr_request import IticrRequest


pytestmark = pytest.mark.asyncio

async def test_iticr(client):
    """Test case for iticr

    ITI Certificate
    """
    body = openapi_server.IticrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/msde/v3/iticr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

