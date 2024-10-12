# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_colorado_water_rights(client):
    """Test case for search_colorado_water_rights

    Search API for 'Colorado Water Rights' entry type
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
                    ('search.db_colorado_water_rights.structure_name', 'search_db_colorado_water_rights_structure_name_example'),
                    ('search.db_colorado_water_rights.structure_type', 'search_db_colorado_water_rights_structure_type_example'),
                    ('search.db_colorado_water_rights.water_source', 'search_db_colorado_water_rights_water_source_example'),
                    ('search.db_colorado_water_rights.county', 'search_db_colorado_water_rights_county_example'),
                    ('search.db_colorado_water_rights.adjudication_date', 'search_db_colorado_water_rights_adjudication_date_example'),
                    ('search.db_colorado_water_rights.appropriation_date', 'search_db_colorado_water_rights_appropriation_date_example'),
                    ('search.db_colorado_water_rights.priority_no', 'search_db_colorado_water_rights_priority_no_example'),
                    ('search.db_colorado_water_rights.decreed_uses', 'search_db_colorado_water_rights_decreed_uses_example'),
                    ('search.db_colorado_water_rights.net_absolute', 3.4),
                    ('search.db_colorado_water_rights.net_conditional', 3.4),
                    ('search.db_colorado_water_rights.net_apex_absolute', 3.4),
                    ('search.db_colorado_water_rights.net_apex_conditional', 3.4),
                    ('search.db_colorado_water_rights.decreed_units', 'search_db_colorado_water_rights_decreed_units_example'),
                    ('search.db_colorado_water_rights.seasonal_limits', 'search_db_colorado_water_rights_seasonal_limits_example'),
                    ('search.db_colorado_water_rights.comments', 'search_db_colorado_water_rights_comments_example'),
                    ('search.db_colorado_water_rights.more_information', 'search_db_colorado_water_rights_more_information_example'),
                    ('search.db_colorado_water_rights.location', 'search_db_colorado_water_rights_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/colorado_water_rights',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

