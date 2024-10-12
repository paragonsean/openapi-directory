# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cvcer400_response import Cvcer400Response
from openapi_server.models.cvcer401_response import Cvcer401Response
from openapi_server.models.cvcer404_response import Cvcer404Response
from openapi_server.models.cvcer500_response import Cvcer500Response
from openapi_server.models.cvcer502_response import Cvcer502Response
from openapi_server.models.cvcer503_response import Cvcer503Response
from openapi_server.models.cvcer504_response import Cvcer504Response
from openapi_server.models.cvcer_request import CvcerRequest


pytestmark = pytest.mark.asyncio

async def test_cvcer(client):
    """Test case for cvcer

    Caste Validity Certificate
    """
    body = openapi_server.CvcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/barti/v3/cvcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

