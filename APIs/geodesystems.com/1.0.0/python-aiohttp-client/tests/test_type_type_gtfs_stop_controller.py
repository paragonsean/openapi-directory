# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_gtfs_stop(client):
    """Test case for search_type_gtfs_stop

    Search API for 'Transit Stop' entry type
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
                    ('search.type_gtfs_stop.stop_id', 'search_type_gtfs_stop_stop_id_example'),
                    ('search.type_gtfs_stop.stop_code', 'search_type_gtfs_stop_stop_code_example'),
                    ('search.type_gtfs_stop.zone_id', 'search_type_gtfs_stop_zone_id_example'),
                    ('search.type_gtfs_stop.location_type', 'search_type_gtfs_stop_location_type_example'),
                    ('search.type_gtfs_stop.wheelchair_boarding', 'search_type_gtfs_stop_wheelchair_boarding_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_gtfs_stop',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

