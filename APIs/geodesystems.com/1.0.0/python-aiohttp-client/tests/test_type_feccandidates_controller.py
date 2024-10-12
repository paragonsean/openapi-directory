# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_feccandidates(client):
    """Test case for search_feccandidates

    Search API for 'Candidates' entry type
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
                    ('search.db_feccandidates.name', 'search_db_feccandidates_name_example'),
                    ('search.db_feccandidates.party', 'search_db_feccandidates_party_example'),
                    ('search.db_feccandidates.state', 'search_db_feccandidates_state_example'),
                    ('search.db_feccandidates.district', 'search_db_feccandidates_district_example'),
                    ('search.db_feccandidates.gender', 'search_db_feccandidates_gender_example'),
                    ('search.db_feccandidates.beginning_cash', 3.4),
                    ('search.db_feccandidates.ending_cash', 3.4),
                    ('search.db_feccandidates.total_receipts', 3.4),
                    ('search.db_feccandidates.total_indivual_contributions', 3.4),
                    ('search.db_feccandidates.transfers_from_committees', 3.4),
                    ('search.db_feccandidates.transfers_to_committees', 3.4),
                    ('search.db_feccandidates.total_disbursements', 3.4),
                    ('search.db_feccandidates.contributions_from_candidate', 3.4),
                    ('search.db_feccandidates.loans_from_candidates', 3.4),
                    ('search.db_feccandidates.other_loans', 3.4),
                    ('search.db_feccandidates.candidate_loan_repayments', 3.4),
                    ('search.db_feccandidates.other_loan_repayments', 3.4),
                    ('search.db_feccandidates.debts_owed_by', 3.4),
                    ('search.db_feccandidates.contributions_from_other_committees', 3.4),
                    ('search.db_feccandidates.contributions_from_party_committees', 3.4),
                    ('search.db_feccandidates.coverage_end_date', 'search_db_feccandidates_coverage_end_date_example'),
                    ('search.db_feccandidates.individual_refunds', 3.4),
                    ('search.db_feccandidates.committee_refunds', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/feccandidates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

