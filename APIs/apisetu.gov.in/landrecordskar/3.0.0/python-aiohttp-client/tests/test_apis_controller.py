# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.cncer400_response import Cncer400Response
from openapi_server.models.cncer401_response import Cncer401Response
from openapi_server.models.cncer404_response import Cncer404Response
from openapi_server.models.cncer500_response import Cncer500Response
from openapi_server.models.cncer502_response import Cncer502Response
from openapi_server.models.cncer503_response import Cncer503Response
from openapi_server.models.cncer504_response import Cncer504Response
from openapi_server.models.cncer_request import CncerRequest
from openapi_server.models.mutan_request import MutanRequest


pytestmark = pytest.mark.asyncio

async def test_cncer(client):
    """Test case for cncer

    Conversion Certificate
    """
    body = openapi_server.CncerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/landrecordskar/v3/cncer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mutan(client):
    """Test case for mutan

    Mutation Report/ePattadar Passbook
    """
    body = openapi_server.MutanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/landrecordskar/v3/mutan/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

