# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_district12 import APIDistrict12
from openapi_server.models.api_district_list2 import APIDistrictList2


pytestmark = pytest.mark.asyncio

async def test_districts_get_all_districts2(client):
    """Test case for districts_get_all_districts2

    Returns a list of districts
    """
    params = [('st', 'st_example'),
                    ('q', 'q_example'),
                    ('city', 'city_example'),
                    ('zip', 'zip_example'),
                    ('nearLatitude', 3.4),
                    ('nearLongitude', 3.4),
                    ('boundaryAddress', 'boundary_address_example'),
                    ('distanceMiles', 56),
                    ('isInBoundaryOnly', True),
                    ('boxLatitudeNW', 3.4),
                    ('boxLongitudeNW', 3.4),
                    ('boxLatitudeSE', 3.4),
                    ('boxLongitudeSE', 3.4),
                    ('page', 56),
                    ('perPage', 56),
                    ('sortBy', 'sort_by_example'),
                    ('includeUnrankedDistrictsInRankSort', True),
                    ('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/districts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_districts_get_district2(client):
    """Test case for districts_get_district2

    Returns a detailed record for one district
    """
    params = [('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/districts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

