# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_season import OnDemandSeason
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_get_vod_season(client):
    """Test case for get_vod_season

    Get a specific season on an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.season+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/seasons/{season_id}'.format(ondemand_id=61326, season_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_season_videos(client):
    """Test case for get_vod_season_videos

    Get all the videos in a season on an On Demand page
    """
    params = [('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos'.format(ondemand_id=61326, season_id=12345),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_seasons(client):
    """Test case for get_vod_seasons

    Get all the seasons on an On Demand page
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.season+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/seasons'.format(ondemand_id=61326),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

