# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_gazeteer_census_tracts(client):
    """Test case for search_gazeteer_census_tracts

    Search API for 'Census Tracts' entry type
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
                    ('search.db_gazeteer_census_tracts.state', 'search_db_gazeteer_census_tracts_state_example'),
                    ('search.db_gazeteer_census_tracts.state_fips', 'search_db_gazeteer_census_tracts_state_fips_example'),
                    ('search.db_gazeteer_census_tracts.county_name', 'search_db_gazeteer_census_tracts_county_name_example'),
                    ('search.db_gazeteer_census_tracts.county_fips', 'search_db_gazeteer_census_tracts_county_fips_example'),
                    ('search.db_gazeteer_census_tracts.census_tract_id', 'search_db_gazeteer_census_tracts_census_tract_id_example'),
                    ('search.db_gazeteer_census_tracts.full_census_tract_id', 'search_db_gazeteer_census_tracts_full_census_tract_id_example'),
                    ('search.db_gazeteer_census_tracts.land_area', 3.4),
                    ('search.db_gazeteer_census_tracts.water_area', 3.4),
                    ('search.db_gazeteer_census_tracts.location', 'search_db_gazeteer_census_tracts_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/gazeteer_census_tracts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

