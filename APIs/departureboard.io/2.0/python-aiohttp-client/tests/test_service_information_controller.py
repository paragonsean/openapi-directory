# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_service_details_by_id(client):
    """Test case for get_service_details_by_id

    getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation.
    """
    params = [('apiKey', 'api_key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2.0/getServiceDetailsByID/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

