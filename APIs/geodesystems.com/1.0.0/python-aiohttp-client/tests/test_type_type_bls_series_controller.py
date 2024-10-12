# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_bls_series(client):
    """Test case for search_type_bls_series

    Search API for 'BLS Series' entry type
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
                    ('search.type_bls_series.survey_name', 'search_type_bls_series_survey_name_example'),
                    ('search.type_bls_series.measure_data_type', 'search_type_bls_series_measure_data_type_example'),
                    ('search.type_bls_series.industry', 'search_type_bls_series_industry_example'),
                    ('search.type_bls_series.sector', 'search_type_bls_series_sector_example'),
                    ('search.type_bls_series.area', 'search_type_bls_series_area_example'),
                    ('search.type_bls_series.item', 'search_type_bls_series_item_example'),
                    ('search.type_bls_series.seasonality', 'search_type_bls_series_seasonality_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_bls_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

