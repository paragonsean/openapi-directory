# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.locations_response import LocationsResponse


pytestmark = pytest.mark.asyncio

async def test_list_locations(client):
    """Test case for list_locations

    List locations
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/connections/{connection_id}/data/commerce-locations'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002', connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

