# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.skmst400_response import Skmst400Response
from openapi_server.models.skmst401_response import Skmst401Response
from openapi_server.models.skmst404_response import Skmst404Response
from openapi_server.models.skmst500_response import Skmst500Response
from openapi_server.models.skmst502_response import Skmst502Response
from openapi_server.models.skmst503_response import Skmst503Response
from openapi_server.models.skmst504_response import Skmst504Response
from openapi_server.models.skmst_request import SkmstRequest


pytestmark = pytest.mark.asyncio

async def test_skmst(client):
    """Test case for skmst

    Skill Marksheet/ Score Card
    """
    body = openapi_server.SkmstRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cpctmp/v3/skmst/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

