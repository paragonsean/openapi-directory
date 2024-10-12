# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dipcr400_response import Dipcr400Response
from openapi_server.models.dipcr401_response import Dipcr401Response
from openapi_server.models.dipcr404_response import Dipcr404Response
from openapi_server.models.dipcr500_response import Dipcr500Response
from openapi_server.models.dipcr502_response import Dipcr502Response
from openapi_server.models.dipcr503_response import Dipcr503Response
from openapi_server.models.dipcr504_response import Dipcr504Response
from openapi_server.models.dipcr_request import DipcrRequest


pytestmark = pytest.mark.asyncio

async def test_dipcr(client):
    """Test case for dipcr

    Diploma Certificate
    """
    body = openapi_server.DipcrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hptechboard/v3/dipcr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

