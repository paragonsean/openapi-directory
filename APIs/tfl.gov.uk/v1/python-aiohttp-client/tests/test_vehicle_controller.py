# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction


pytestmark = pytest.mark.asyncio

async def test_vehicle_get(client):
    """Test case for vehicle_get

    Gets the predictions for a given list of vehicle Id's.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Vehicle/{ids}/Arrivals'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

