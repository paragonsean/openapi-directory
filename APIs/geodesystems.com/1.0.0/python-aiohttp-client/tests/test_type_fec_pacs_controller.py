# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_fec_pacs(client):
    """Test case for search_fec_pacs

    Search API for 'FEC PACs' entry type
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
                    ('search.db_fec_pacs.committee', 'search_db_fec_pacs_committee_example'),
                    ('search.db_fec_pacs.total_receipts', 3.4),
                    ('search.db_fec_pacs.beginning_cash', 3.4),
                    ('search.db_fec_pacs.ending_cash', 3.4),
                    ('search.db_fec_pacs.contributions_from_individuals', 3.4),
                    ('search.db_fec_pacs.contributions_from_other_committees', 3.4),
                    ('search.db_fec_pacs.trans_from_affiliates', 3.4),
                    ('search.db_fec_pacs.contributions_to_other_committee', 3.4),
                    ('search.db_fec_pacs.contributions_from_candidate', 3.4),
                    ('search.db_fec_pacs.loans_from_candidate', 3.4),
                    ('search.db_fec_pacs.total_loans_received', 3.4),
                    ('search.db_fec_pacs.total_distributions', 3.4),
                    ('search.db_fec_pacs.transfers_to_affiliates', 3.4),
                    ('search.db_fec_pacs.refunds_to_individuals', 3.4),
                    ('search.db_fec_pacs.refends_to_othercommittees', 3.4),
                    ('search.db_fec_pacs.candidate_loan_repayments', 3.4),
                    ('search.db_fec_pacs.loan_repayments', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/fec_pacs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

