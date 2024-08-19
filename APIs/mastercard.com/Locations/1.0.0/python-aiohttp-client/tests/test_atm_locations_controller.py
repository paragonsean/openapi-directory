# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.atms_response import AtmsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_atms_v1_atm_get(client):
    """Test case for atms_v1_atm_get

    Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features.
    """
    params = [('PageOffset', 0),
                    ('PageLength', 5),
                    ('AddressLine1', '114 Fifth Avenue'),
                    ('AddressLine2', 'Apartment 1'),
                    ('City', 'New York City'),
                    ('CountrySubdivision', 'NY'),
                    ('PostalCode', '11101'),
                    ('Country', 'USA'),
                    ('Latitude', 38.76006576913497),
                    ('Longitude', -90.74615107952418),
                    ('DistanceUnit', 'MILE'),
                    ('Radius', 25),
                    ('SupportEMV', 1),
                    ('InternationalMaestroAccepted', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/atms/v1/atm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

