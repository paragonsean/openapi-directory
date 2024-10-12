# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ratcr400_response import Ratcr400Response
from openapi_server.models.ratcr401_response import Ratcr401Response
from openapi_server.models.ratcr404_response import Ratcr404Response
from openapi_server.models.ratcr500_response import Ratcr500Response
from openapi_server.models.ratcr502_response import Ratcr502Response
from openapi_server.models.ratcr503_response import Ratcr503Response
from openapi_server.models.ratcr504_response import Ratcr504Response
from openapi_server.models.ratcr_request import RatcrRequest


pytestmark = pytest.mark.asyncio

async def test_ratcr(client):
    """Test case for ratcr

    Ration Card
    """
    body = openapi_server.RatcrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/aaharjh/v3/ratcr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

