# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_accident_stats_accident_detail import TflApiPresentationEntitiesAccidentStatsAccidentDetail


pytestmark = pytest.mark.asyncio

async def test_accident_stats_get(client):
    """Test case for accident_stats_get

    Gets all accident details for accidents occuring in the specified year
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/AccidentStats/{year}'.format(year=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

