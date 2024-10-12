# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO


pytestmark = pytest.mark.asyncio

async def test_get_prices(client):
    """Test case for get_prices

    Get information about the prices.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/providernetworks/{providernetwork_uid}/prices'.format(providernetwork_uid='providernetwork_uid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

