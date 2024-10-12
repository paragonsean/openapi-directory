# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO


pytestmark = pytest.mark.asyncio

async def test_list_booking_proposals(client):
    """Test case for list_booking_proposals

    Query for available RentalObjects of a specific view
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('radius', 56),
                    ('offset', 56),
                    ('limit', 56),
                    ('providernetwork', 'providernetwork_example'),
                    ('begin', 'begin_example'),
                    ('end', 'end_example'),
                    ('expand', 'expand_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/bookingproposals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

