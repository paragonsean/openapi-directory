# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.vehicle import Vehicle
from openapi_server.models.vehicle_request import VehicleRequest


pytestmark = pytest.mark.asyncio

async def test_get_vehicle_details_by_registration_number(client):
    """Test case for get_vehicle_details_by_registration_number

    Get vehicle details by registration number
    """
    body = {"registrationNumber":"registrationNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
        'x_correlation_id': 'x_correlation_id_example',
    }
    response = await client.request(
        method='POST',
        path='/vehicle-enquiry/v1/vehicles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

