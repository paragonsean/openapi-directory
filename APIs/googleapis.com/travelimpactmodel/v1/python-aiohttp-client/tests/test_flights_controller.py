# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compute_flight_emissions_request import ComputeFlightEmissionsRequest
from openapi_server.models.compute_flight_emissions_response import ComputeFlightEmissionsResponse


pytestmark = pytest.mark.asyncio

async def test_travelimpactmodel_flights_compute_flight_emissions(client):
    """Test case for travelimpactmodel_flights_compute_flight_emissions

    
    """
    body = {"flights":[{"operatingCarrierCode":"operatingCarrierCode","origin":"origin","destination":"destination","departureDate":{"month":2,"year":7,"day":5},"flightNumber":9},{"operatingCarrierCode":"operatingCarrierCode","origin":"origin","destination":"destination","departureDate":{"month":2,"year":7,"day":5},"flightNumber":9}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/flights:computeFlightEmissions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

