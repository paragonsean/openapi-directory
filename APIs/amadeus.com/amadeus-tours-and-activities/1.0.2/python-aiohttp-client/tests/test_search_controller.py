# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.successful_search import SuccessfulSearch


pytestmark = pytest.mark.asyncio

async def test_list_activities(client):
    """Test case for list_activities

    Returns Activities around a given location
    """
    params = [('latitude', 41.397158),
                    ('longitude', 2.160873),
                    ('radius', 1)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shopping/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_activities_by_square(client):
    """Test case for list_activities_by_square

    Returns Activities around a given location
    """
    params = [('north', 41.397158),
                    ('west', 2.160873),
                    ('south', 41.394582),
                    ('east', 2.177181)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shopping/activities/by-square',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

