# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.driving_license_schema import DrivingLicenseSchema
from openapi_server.models.drvlc400_response import Drvlc400Response
from openapi_server.models.drvlc401_response import Drvlc401Response
from openapi_server.models.drvlc404_response import Drvlc404Response
from openapi_server.models.drvlc500_response import Drvlc500Response
from openapi_server.models.drvlc502_response import Drvlc502Response
from openapi_server.models.drvlc503_response import Drvlc503Response
from openapi_server.models.drvlc504_response import Drvlc504Response
from openapi_server.models.drvlc_request import DrvlcRequest
from openapi_server.models.rvcer_request import RvcerRequest
from openapi_server.models.vehicle_registration_schema import VehicleRegistrationSchema


pytestmark = pytest.mark.asyncio

async def test_drvlc(client):
    """Test case for drvlc

    Driving License
    """
    body = openapi_server.DrvlcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/transportcg/v3/drvlc/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rvcer(client):
    """Test case for rvcer

    Registration of Vehicles
    """
    body = openapi_server.RvcerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'clientId': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/transportcg/v3/rvcer/certificate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

