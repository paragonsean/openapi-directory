# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_school20_full import APISchool20Full
from openapi_server.models.api_school_list2 import APISchoolList2


pytestmark = pytest.mark.asyncio

async def test_schools_get_all_schools20(client):
    """Test case for schools_get_all_schools20

    Returns a list of schools
    """
    params = [('st', 'st_example'),
                    ('q', 'q_example'),
                    ('qSearchSchoolNameOnly', True),
                    ('districtID', 'district_id_example'),
                    ('level', 'level_example'),
                    ('city', 'city_example'),
                    ('zip', 'zip_example'),
                    ('isMagnet', True),
                    ('isCharter', True),
                    ('isVirtual', True),
                    ('isTitleI', True),
                    ('isTitleISchoolwide', True),
                    ('nearLatitude', 3.4),
                    ('nearLongitude', 3.4),
                    ('nearAddress', 'near_address_example'),
                    ('distanceMiles', 56),
                    ('boundaryLatitude', 3.4),
                    ('boundaryLongitude', 3.4),
                    ('boundaryAddress', 'boundary_address_example'),
                    ('isInBoundaryOnly', True),
                    ('boxLatitudeNW', 3.4),
                    ('boxLongitudeNW', 3.4),
                    ('boxLatitudeSE', 3.4),
                    ('boxLongitudeSE', 3.4),
                    ('page', 56),
                    ('perPage', 56),
                    ('sortBy', 'sort_by_example'),
                    ('includeUnrankedSchoolsInRankSort', True),
                    ('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/schools',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schools_get_school20(client):
    """Test case for schools_get_school20

    Returns a detailed record for one school
    """
    params = [('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/schools/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

