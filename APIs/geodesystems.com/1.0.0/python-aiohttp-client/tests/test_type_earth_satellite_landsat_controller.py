# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_earth_satellite_landsat(client):
    """Test case for search_earth_satellite_landsat

    Search API for 'Landsat Satellite Data' entry type
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
                    ('search.earth_satellite_landsat.sensor', 'search_earth_satellite_landsat_sensor_example'),
                    ('search.earth_satellite_landsat.satellite', 'search_earth_satellite_landsat_satellite_example'),
                    ('search.earth_satellite_landsat.wrs_path_number', 56),
                    ('search.earth_satellite_landsat.wrs_row_number', 56),
                    ('search.earth_satellite_landsat.ground_station', 'search_earth_satellite_landsat_ground_station_example'),
                    ('search.earth_satellite_landsat.archive_version_number', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/earth_satellite_landsat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

