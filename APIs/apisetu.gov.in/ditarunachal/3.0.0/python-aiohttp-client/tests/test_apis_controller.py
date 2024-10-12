# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ilpmt400_response import Ilpmt400Response
from openapi_server.models.ilpmt401_response import Ilpmt401Response
from openapi_server.models.ilpmt404_response import Ilpmt404Response
from openapi_server.models.ilpmt500_response import Ilpmt500Response
from openapi_server.models.ilpmt502_response import Ilpmt502Response
from openapi_server.models.ilpmt503_response import Ilpmt503Response
from openapi_server.models.ilpmt504_response import Ilpmt504Response
from openapi_server.models.ilpmt_request import IlpmtRequest


pytestmark = pytest.mark.asyncio

async def test_ilpmt(client):
    """Test case for ilpmt

    Inner Line Permit
    """
    body = openapi_server.IlpmtRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ditarunachal/v3/ilpmt/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

