# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_type_edgar_filing(client):
    """Test case for search_type_edgar_filing

    Search API for 'SEC EDGAR Filing' entry type
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
                    ('search.type_edgar_filing.form_type', 'search_type_edgar_filing_form_type_example'),
                    ('search.type_edgar_filing.company_name', 'search_type_edgar_filing_company_name_example'),
                    ('search.type_edgar_filing.cik_number', 'search_type_edgar_filing_cik_number_example'),
                    ('search.type_edgar_filing.standard_industrial_classification', 'search_type_edgar_filing_standard_industrial_classification_example'),
                    ('search.type_edgar_filing.irs_number', 'search_type_edgar_filing_irs_number_example'),
                    ('search.type_edgar_filing.state', 'search_type_edgar_filing_state_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/type_edgar_filing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

