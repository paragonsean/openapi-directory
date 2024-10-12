# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_point_geomag_iaga2002(client):
    """Test case for search_type_point_geomag_iaga2002

    Search API for 'IAGA 2002 Geomagnetism Data' entry type
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
                    ('search.type_point_geomag_iaga2002.iaga_code', 'search_type_point_geomag_iaga2002_iaga_code_example'),
                    ('search.type_point_geomag_iaga2002.station_name', 'search_type_point_geomag_iaga2002_station_name_example'),
                    ('search.type_point_geomag_iaga2002.source_of_data', 'search_type_point_geomag_iaga2002_source_of_data_example'),
                    ('search.type_point_geomag_iaga2002.digital_sampling', 'search_type_point_geomag_iaga2002_digital_sampling_example'),
                    ('search.type_point_geomag_iaga2002.data_interval', 'search_type_point_geomag_iaga2002_data_interval_example'),
                    ('search.type_point_geomag_iaga2002.data_type', 'search_type_point_geomag_iaga2002_data_type_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_point_geomag_iaga2002',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

