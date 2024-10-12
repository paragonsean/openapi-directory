# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.predictions200_response import Predictions200Response
from openapi_server.models.predictions400_response import Predictions400Response


pytestmark = pytest.mark.asyncio

async def test_predictions(client):
    """Test case for predictions

    Get predictions for a given year
    """
    params = [('year', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pcraig3/groundhog-day-api/1.2.1/api/v1/predictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

