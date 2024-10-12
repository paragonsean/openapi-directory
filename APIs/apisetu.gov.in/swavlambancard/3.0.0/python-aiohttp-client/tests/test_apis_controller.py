# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.dpicr400_response import Dpicr400Response
from openapi_server.models.dpicr401_response import Dpicr401Response
from openapi_server.models.dpicr404_response import Dpicr404Response
from openapi_server.models.dpicr500_response import Dpicr500Response
from openapi_server.models.dpicr502_response import Dpicr502Response
from openapi_server.models.dpicr503_response import Dpicr503Response
from openapi_server.models.dpicr504_response import Dpicr504Response
from openapi_server.models.dpicr_request import DpicrRequest
from openapi_server.models.govid_request import GovidRequest


pytestmark = pytest.mark.asyncio

async def test_dpicr(client):
    """Test case for dpicr

    Disabled Person Identity Card/ Certificate
    """
    body = openapi_server.DpicrRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/swavlambancard/v3/dpicr/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_govid(client):
    """Test case for govid

    ID Card
    """
    body = openapi_server.GovidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/swavlambancard/v3/govid/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

