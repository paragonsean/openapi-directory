# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_police_stop_data(client):
    """Test case for search_police_stop_data

    Search API for 'Police Stop Data' entry type
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
                    ('search.db_police_stop_data.race', 'search_db_police_stop_data_race_example'),
                    ('search.db_police_stop_data.ethnicity', 'search_db_police_stop_data_ethnicity_example'),
                    ('search.db_police_stop_data.sex', 'search_db_police_stop_data_sex_example'),
                    ('search.db_police_stop_data.minutes', 56),
                    ('search.db_police_stop_data.date', 'search_db_police_stop_data_date_example'),
                    ('search.db_police_stop_data.address', 'search_db_police_stop_data_address_example'),
                    ('search.db_police_stop_data.resident', 'search_db_police_stop_data_resident_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/police_stop_data',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

