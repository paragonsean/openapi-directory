# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boston_crime(client):
    """Test case for search_boston_crime

    Search API for 'Boston Crime' entry type
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
                    ('search.db_boston_crime.offense', 'search_db_boston_crime_offense_example'),
                    ('search.db_boston_crime.offense_code_group', 'search_db_boston_crime_offense_code_group_example'),
                    ('search.db_boston_crime.offense_description', 'search_db_boston_crime_offense_description_example'),
                    ('search.db_boston_crime.district', 'search_db_boston_crime_district_example'),
                    ('search.db_boston_crime.reporting_area', 'search_db_boston_crime_reporting_area_example'),
                    ('search.db_boston_crime.shooting', 'search_db_boston_crime_shooting_example'),
                    ('search.db_boston_crime.year', 3.4),
                    ('search.db_boston_crime.month', 3.4),
                    ('search.db_boston_crime.day_of_week', 'search_db_boston_crime_day_of_week_example'),
                    ('search.db_boston_crime.hour', 3.4),
                    ('search.db_boston_crime.street', 'search_db_boston_crime_street_example'),
                    ('search.db_boston_crime.location', 'search_db_boston_crime_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boston_crime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

