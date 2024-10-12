# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pan_verification_record_schema import PANVerificationRecordSchema
from openapi_server.models.pancr400_response import Pancr400Response
from openapi_server.models.pancr401_response import Pancr401Response
from openapi_server.models.pancr404_response import Pancr404Response
from openapi_server.models.pancr500_response import Pancr500Response
from openapi_server.models.pancr502_response import Pancr502Response
from openapi_server.models.pancr503_response import Pancr503Response
from openapi_server.models.pancr504_response import Pancr504Response
from openapi_server.models.pancr_request import PancrRequest


pytestmark = pytest.mark.asyncio

async def test_pancr(client):
    """Test case for pancr

    PAN Verification Record
    """
    body = openapi_server.PancrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pan/v3/pancr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

