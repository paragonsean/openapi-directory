# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.adcrd400_response import Adcrd400Response
from openapi_server.models.adcrd401_response import Adcrd401Response
from openapi_server.models.adcrd404_response import Adcrd404Response
from openapi_server.models.adcrd500_response import Adcrd500Response
from openapi_server.models.adcrd502_response import Adcrd502Response
from openapi_server.models.adcrd503_response import Adcrd503Response
from openapi_server.models.adcrd504_response import Adcrd504Response
from openapi_server.models.adcrd_request import AdcrdRequest


pytestmark = pytest.mark.asyncio

async def test_adcrd(client):
    """Test case for adcrd

    Admit Card
    """
    body = openapi_server.AdcrdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/meark/v3/adcrd/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

