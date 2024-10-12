# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legal_search_get_default_response import LegalSearchGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_legal_search_get(client):
    """Test case for legal_search_get

    
    """
    params = [('case_statutory_citation', ['case_statutory_citation_example']),
                    ('af_min_rtb_date', '2013-10-20'),
                    ('af_report_year', 'af_report_year_example'),
                    ('q', 'q_example'),
                    ('from_hit', 56),
                    ('ao_requestor_type', [56]),
                    ('case_max_close_date', '2013-10-20'),
                    ('ao_is_pending', True),
                    ('af_fd_fine_amount', 56),
                    ('case_min_open_date', '2013-10-20'),
                    ('ao_min_issue_date', '2013-10-20'),
                    ('sort', 'sort_example'),
                    ('ao_citation_require_all', True),
                    ('case_doc_category_id', ['case_doc_category_id_example']),
                    ('ao_status', 'ao_status_example'),
                    ('af_max_rtb_date', '2013-10-20'),
                    ('af_rtb_fine_amount', 56),
                    ('case_respondents', 'case_respondents_example'),
                    ('ao_entity_name', ['ao_entity_name_example']),
                    ('ao_requestor', 'ao_requestor_example'),
                    ('ao_category', ['ao_category_example']),
                    ('ao_regulatory_citation', ['ao_regulatory_citation_example']),
                    ('case_regulatory_citation', ['case_regulatory_citation_example']),
                    ('case_citation_require_all', True),
                    ('case_dispositions', ['case_dispositions_example']),
                    ('ao_name', ['ao_name_example']),
                    ('af_max_fd_date', '2013-10-20'),
                    ('ao_max_request_date', '2013-10-20'),
                    ('mur_type', 'mur_type_example'),
                    ('hits_returned', 56),
                    ('case_election_cycles', 56),
                    ('case_min_close_date', '2013-10-20'),
                    ('ao_max_issue_date', '2013-10-20'),
                    ('af_committee_id', 'af_committee_id_example'),
                    ('af_min_fd_date', '2013-10-20'),
                    ('case_max_open_date', '2013-10-20'),
                    ('api_key', 'DEMO_KEY'),
                    ('ao_min_request_date', '2013-10-20'),
                    ('ao_no', ['ao_no_example']),
                    ('type', 'type_example'),
                    ('case_no', ['case_no_example']),
                    ('ao_statutory_citation', ['ao_statutory_citation_example']),
                    ('af_name', ['af_name_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/legal/search/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

