# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_db_co_indicators(client):
    """Test case for search_db_co_indicators

    Search API for 'Colorado Health Indicators' entry type
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
                    ('search.db_db_co_indicators.geo_name', 'search_db_db_co_indicators_geo_name_example'),
                    ('search.db_db_co_indicators.domain', 'search_db_db_co_indicators_domain_example'),
                    ('search.db_db_co_indicators.subdomain', 'search_db_db_co_indicators_subdomain_example'),
                    ('search.db_db_co_indicators.indicatorName', 'search_db_db_co_indicators_indicator_name_example'),
                    ('search.db_db_co_indicators.description', 'search_db_db_co_indicators_description_example'),
                    ('search.db_db_co_indicators.measure', 3.4),
                    ('search.db_db_co_indicators.location', 'search_db_db_co_indicators_location_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/db_co_indicators',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

