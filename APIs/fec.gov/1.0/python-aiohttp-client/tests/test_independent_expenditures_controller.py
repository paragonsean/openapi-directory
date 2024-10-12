# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ie_totals_by_candidate_page import IETotalsByCandidatePage
from openapi_server.models.schedule_eby_candidate_page import ScheduleEByCandidatePage
from openapi_server.models.schedule_e_efile_page import ScheduleEEfilePage
from openapi_server.models.schedule_e_page import ScheduleEPage


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_e_efile_get(client):
    """Test case for schedules_schedule_e_efile_get

    
    """
    params = [('max_expenditure_amount', 56),
                    ('support_oppose_indicator', ['support_oppose_indicator_example']),
                    ('min_expenditure_date', '2013-10-20'),
                    ('filing_form', ['filing_form_example']),
                    ('max_expenditure_date', '2013-10-20'),
                    ('max_filed_date', '2013-10-20'),
                    ('is_notice', True),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('payee_name', ['payee_name_example']),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('candidate_office_district', ['candidate_office_district_example']),
                    ('sort', '-expenditure_date'),
                    ('api_key', 'DEMO_KEY'),
                    ('min_expenditure_amount', 56),
                    ('spender_name', ['spender_name_example']),
                    ('min_dissemination_date', '2013-10-20'),
                    ('candidate_office_state', ['candidate_office_state_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('candidate_search', ['candidate_search_example']),
                    ('image_number', ['image_number_example']),
                    ('candidate_party', ['candidate_party_example']),
                    ('min_filed_date', '2013-10-20'),
                    ('max_dissemination_date', '2013-10-20'),
                    ('most_recent', True),
                    ('candidate_office', 'candidate_office_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_e/efile/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_e_totals_by_candidate_get(client):
    """Test case for schedules_schedule_e_totals_by_candidate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_e/totals/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_eby_candidate_get(client):
    """Test case for schedules_schedule_eby_candidate_get

    
    """
    params = [('district', 'district_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('support_oppose', 'support_oppose_example'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', 'state_example'),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('office', 'office_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_e/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_eget(client):
    """Test case for schedules_schedule_eget

    
    """
    params = [('last_expenditure_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('is_notice', [True]),
                    ('payee_name', ['payee_name_example']),
                    ('min_amount', 'min_amount_example'),
                    ('candidate_id', ['candidate_id_example']),
                    ('sort_hide_null', False),
                    ('last_office_total_ytd', 3.4),
                    ('sort', '-expenditure_date'),
                    ('min_filing_date', '2013-10-20'),
                    ('q_spender', ['q_spender_example']),
                    ('min_dissemination_date', '2013-10-20'),
                    ('candidate_office_state', ['candidate_office_state_example']),
                    ('sort_nulls_last', False),
                    ('last_expenditure_amount', 3.4),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('max_dissemination_date', '2013-10-20'),
                    ('min_date', '2013-10-20'),
                    ('filing_form', ['filing_form_example']),
                    ('support_oppose_indicator', ['support_oppose_indicator_example']),
                    ('min_image_number', 'min_image_number_example'),
                    ('cycle', [56]),
                    ('max_filing_date', '2013-10-20'),
                    ('sort_null_only', False),
                    ('last_support_oppose_indicator', 'last_support_oppose_indicator_example'),
                    ('last_index', 56),
                    ('per_page', 20),
                    ('candidate_office_district', ['candidate_office_district_example']),
                    ('line_number', 'line_number_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('committee_id', ['committee_id_example']),
                    ('candidate_party', ['candidate_party_example']),
                    ('max_amount', 'max_amount_example'),
                    ('most_recent', True),
                    ('candidate_office', ['candidate_office_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_e/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

