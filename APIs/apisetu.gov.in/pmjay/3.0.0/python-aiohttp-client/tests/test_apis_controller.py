# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pmjay400_response import Pmjay400Response
from openapi_server.models.pmjay401_response import Pmjay401Response
from openapi_server.models.pmjay404_response import Pmjay404Response
from openapi_server.models.pmjay500_response import Pmjay500Response
from openapi_server.models.pmjay502_response import Pmjay502Response
from openapi_server.models.pmjay503_response import Pmjay503Response
from openapi_server.models.pmjay504_response import Pmjay504Response
from openapi_server.models.pmjay_request import PmjayRequest


pytestmark = pytest.mark.asyncio

async def test_pmjay(client):
    """Test case for pmjay

    Pradhan Mantri Jan Arogya Yojana
    """
    body = openapi_server.PmjayRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pmjay/v3/pmjay/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

