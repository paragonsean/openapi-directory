# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_ufo_sightings(client):
    """Test case for search_ufo_sightings

    Search API for 'Ufo Sightings' entry type
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
                    ('search.db_ufo_sightings.datetime', 'search_db_ufo_sightings_datetime_example'),
                    ('search.db_ufo_sightings.city', 'search_db_ufo_sightings_city_example'),
                    ('search.db_ufo_sightings.state', 'search_db_ufo_sightings_state_example'),
                    ('search.db_ufo_sightings.country', 'search_db_ufo_sightings_country_example'),
                    ('search.db_ufo_sightings.shape', 'search_db_ufo_sightings_shape_example'),
                    ('search.db_ufo_sightings.duration_seconds', 3.4),
                    ('search.db_ufo_sightings.duration_hours_min', 'search_db_ufo_sightings_duration_hours_min_example'),
                    ('search.db_ufo_sightings.comments', 'search_db_ufo_sightings_comments_example'),
                    ('search.db_ufo_sightings.date_posted', 'search_db_ufo_sightings_date_posted_example'),
                    ('search.db_ufo_sightings.latitude', 3.4),
                    ('search.db_ufo_sightings.longitude', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/ufo_sightings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

