# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_active_service_type import TflApiPresentationEntitiesActiveServiceType
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction


pytestmark = pytest.mark.asyncio

async def test_mode_arrivals(client):
    """Test case for mode_arrivals

    Gets the next arrival predictions for all stops of a given mode
    """
    params = [('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Mode/{mode}/Arrivals'.format(mode='mode_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mode_get_active_service_types(client):
    """Test case for mode_get_active_service_types

    Returns the service type active for a mode.              Currently only supports tube
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Mode/ActiveServiceTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

