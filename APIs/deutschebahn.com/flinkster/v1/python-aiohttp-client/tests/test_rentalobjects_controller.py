# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO


pytestmark = pytest.mark.asyncio

async def test_get_rental_object(client):
    """Test case for get_rental_object

    Get information about the RentalObject.
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/flinkster-api-ng/v1/providernetworks/{providernetwork_uid}/rentalobjects/{rental_object_uid}'.format(rental_object_uid='rental_object_uid_example', providernetwork_uid='providernetwork_uid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

