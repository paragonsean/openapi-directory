# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_gazeteer_counties(client):
    """Test case for search_gazeteer_counties

    Search API for 'Census Gazeteer Counties' entry type
    """
    params = [('text', 'text_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('fromdate', '2013-10-20T19:20:30+01:00'),
                    ('todate', '2013-10-20T19:20:30+01:00'),
                    ('createdate.from', '2013-10-20T19:20:30+01:00'),
                    ('createdate.to', '2013-10-20T19:20:30+01:00'),
                    ('changedate.from', '2013-10-20T19:20:30+01:00'),
                    ('changedate.to', '2013-10-20T19:20:30+01:00'),
                    ('group', 'group_example'),
                    ('filesuffix', 'filesuffix_example'),
                    ('maxlatitude', 3.4),
                    ('minlongitude', 3.4),
                    ('minlatitude', 3.4),
                    ('maxlongitude', 3.4),
                    ('max', 56),
                    ('skip', 56),
                    ('search.db_gazeteer_counties.state_abbreviation', 'search_db_gazeteer_counties_state_abbreviation_example'),
                    ('search.db_gazeteer_counties.state_fips', 'search_db_gazeteer_counties_state_fips_example'),
                    ('search.db_gazeteer_counties.county_fips', 'search_db_gazeteer_counties_county_fips_example'),
                    ('search.db_gazeteer_counties.full_county_fips', 'search_db_gazeteer_counties_full_county_fips_example'),
                    ('search.db_gazeteer_counties.county_name', 'search_db_gazeteer_counties_county_name_example'),
                    ('search.db_gazeteer_counties.area_land', 3.4),
                    ('search.db_gazeteer_counties.area_water', 3.4),
                    ('search.db_gazeteer_counties.location', 'search_db_gazeteer_counties_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/gazeteer_counties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

