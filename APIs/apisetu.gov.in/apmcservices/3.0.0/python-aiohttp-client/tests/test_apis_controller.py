# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apmcl400_response import Apmcl400Response
from openapi_server.models.apmcl401_response import Apmcl401Response
from openapi_server.models.apmcl404_response import Apmcl404Response
from openapi_server.models.apmcl500_response import Apmcl500Response
from openapi_server.models.apmcl502_response import Apmcl502Response
from openapi_server.models.apmcl503_response import Apmcl503Response
from openapi_server.models.apmcl504_response import Apmcl504Response
from openapi_server.models.apmcl_request import ApmclRequest


pytestmark = pytest.mark.asyncio

async def test_apmcl(client):
    """Test case for apmcl

    Agriculture Produce Market Committee License
    """
    body = openapi_server.ApmclRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apmcservices/v3/apmcl/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

