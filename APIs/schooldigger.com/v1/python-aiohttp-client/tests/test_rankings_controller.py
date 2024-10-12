# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_district_list_rank import APIDistrictListRank
from openapi_server.models.api_school_list_rank import APISchoolListRank


pytestmark = pytest.mark.asyncio

async def test_rankings_get_rank(client):
    """Test case for rankings_get_rank

    Returns a SchoolDigger school ranking list
    """
    params = [('year', 56),
                    ('level', 'level_example'),
                    ('page', 56),
                    ('perPage', 56),
                    ('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/rankings/schools/{st}'.format(st='st_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rankings_get_rank_district(client):
    """Test case for rankings_get_rank_district

    Returns a SchoolDigger district ranking list
    """
    params = [('year', 56),
                    ('page', 56),
                    ('perPage', 56),
                    ('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/rankings/districts/{st}'.format(st='st_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

