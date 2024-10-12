# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_point_noaa_flask_month(client):
    """Test case for search_type_point_noaa_flask_month

    Search API for 'NOAA Flask Month Measurements' entry type
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
                    ('search.type_point_noaa_flask_month.site_id', 'search_type_point_noaa_flask_month_site_id_example'),
                    ('search.type_point_noaa_flask_month.parameter', 'search_type_point_noaa_flask_month_parameter_example'),
                    ('search.type_point_noaa_flask_month.project', 'search_type_point_noaa_flask_month_project_example'),
                    ('search.type_point_noaa_flask_month.lab_id_number', 'search_type_point_noaa_flask_month_lab_id_number_example'),
                    ('search.type_point_noaa_flask_month.measurement_group', 'search_type_point_noaa_flask_month_measurement_group_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_point_noaa_flask_month',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

