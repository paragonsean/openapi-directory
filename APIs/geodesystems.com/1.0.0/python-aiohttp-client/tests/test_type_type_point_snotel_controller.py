# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_point_snotel(client):
    """Test case for search_type_point_snotel

    Search API for 'SNOTEL Snow Data' entry type
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
                    ('search.type_point_snotel.site_id', 'search_type_point_snotel_site_id_example'),
                    ('search.type_point_snotel.site_number', 'search_type_point_snotel_site_number_example'),
                    ('search.type_point_snotel.state', 'search_type_point_snotel_state_example'),
                    ('search.type_point_snotel.network', 'search_type_point_snotel_network_example'),
                    ('search.type_point_snotel.huc_name', 'search_type_point_snotel_huc_name_example'),
                    ('search.type_point_snotel.huc_id', 'search_type_point_snotel_huc_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_point_snotel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

