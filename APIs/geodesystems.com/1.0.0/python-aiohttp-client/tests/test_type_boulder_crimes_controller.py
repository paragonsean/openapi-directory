# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder_crimes(client):
    """Test case for search_boulder_crimes

    Search API for 'Boulder Crime Reports' entry type
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
                    ('search.db_boulder_crimes.offense', 'search_db_boulder_crimes_offense_example'),
                    ('search.db_boulder_crimes.reportdate', 'search_db_boulder_crimes_reportdate_example'),
                    ('search.db_boulder_crimes.blockadd', 'search_db_boulder_crimes_blockadd_example'),
                    ('search.db_boulder_crimes.location', 'search_db_boulder_crimes_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_crimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

