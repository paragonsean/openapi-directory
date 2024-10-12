# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.committee_reports_page import CommitteeReportsPage
from openapi_server.models.committee_totals_page import CommitteeTotalsPage
from openapi_server.models.election_page import ElectionPage
from openapi_server.models.election_summary import ElectionSummary
from openapi_server.models.elections_list_page import ElectionsListPage
from openapi_server.models.entity_receipt_disbursement_totals_page import EntityReceiptDisbursementTotalsPage
from openapi_server.models.inaugural_donations_page import InauguralDonationsPage


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_reports_get(client):
    """Test case for committee_committee_id_reports_get

    
    """
    params = [('min_party_coordinated_expenditures', 'min_party_coordinated_expenditures_example'),
                    ('is_amended', True),
                    ('max_party_coordinated_expenditures', 'max_party_coordinated_expenditures_example'),
                    ('max_cash_on_hand_end_period_amount', 'max_cash_on_hand_end_period_amount_example'),
                    ('max_disbursements_amount', 'max_disbursements_amount_example'),
                    ('max_debts_owed_expenditures', 'max_debts_owed_expenditures_example'),
                    ('min_receipts_amount', 'min_receipts_amount_example'),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('min_debts_owed_amount', 'min_debts_owed_amount_example'),
                    ('sort_hide_null', False),
                    ('candidate_id', 'candidate_id_example'),
                    ('min_independent_expenditures', 'min_independent_expenditures_example'),
                    ('per_page', 20),
                    ('sort', ["-coverage_end_date"]),
                    ('api_key', 'DEMO_KEY'),
                    ('max_receipts_amount', 'max_receipts_amount_example'),
                    ('report_type', ['report_type_example']),
                    ('max_total_contributions', 'max_total_contributions_example'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('year', [56]),
                    ('max_independent_expenditures', 'max_independent_expenditures_example'),
                    ('type', ['type_example']),
                    ('min_cash_on_hand_end_period_amount', 'min_cash_on_hand_end_period_amount_example'),
                    ('min_disbursements_amount', 'min_disbursements_amount_example'),
                    ('min_total_contributions', 'min_total_contributions_example'),
                    ('beginning_image_number', ['beginning_image_number_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/reports'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_totals_get(client):
    """Test case for committee_committee_id_totals_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort_nulls_last', False),
                    ('sort', '-cycle'),
                    ('cycle', [56]),
                    ('sort_null_only', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/totals'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elections_get(client):
    """Test case for elections_get

    
    """
    params = [('district', 'district_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', 56),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', 'state_example'),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('office', 'office_example'),
                    ('sort', '-total_receipts')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/elections/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elections_search_get(client):
    """Test case for elections_search_get

    
    """
    params = [('zip', [56]),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('office', ['office_example']),
                    ('sort', ["sort_order","district"])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/elections/search/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elections_summary_get(client):
    """Test case for elections_summary_get

    
    """
    params = [('state', 'state_example'),
                    ('district', 'district_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('office', 'office_example'),
                    ('cycle', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/elections/summary/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_entity_type_get(client):
    """Test case for reports_entity_type_get

    
    """
    params = [('max_party_coordinated_expenditures', 'max_party_coordinated_expenditures_example'),
                    ('max_debts_owed_expenditures', 'max_debts_owed_expenditures_example'),
                    ('min_receipts_amount', 'min_receipts_amount_example'),
                    ('min_debts_owed_amount', 'min_debts_owed_amount_example'),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('candidate_id', 'candidate_id_example'),
                    ('sort', ["-coverage_end_date"]),
                    ('q_spender', ['q_spender_example']),
                    ('max_receipts_amount', 'max_receipts_amount_example'),
                    ('filer_type', 'filer_type_example'),
                    ('report_type', ['report_type_example']),
                    ('max_total_contributions', 'max_total_contributions_example'),
                    ('sort_nulls_last', False),
                    ('max_independent_expenditures', 'max_independent_expenditures_example'),
                    ('min_total_contributions', 'min_total_contributions_example'),
                    ('min_party_coordinated_expenditures', 'min_party_coordinated_expenditures_example'),
                    ('beginning_image_number', ['beginning_image_number_example']),
                    ('min_receipt_date', '2013-10-20'),
                    ('is_amended', True),
                    ('max_disbursements_amount', 'max_disbursements_amount_example'),
                    ('max_cash_on_hand_end_period_amount', 'max_cash_on_hand_end_period_amount_example'),
                    ('amendment_indicator', ['amendment_indicator_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('min_independent_expenditures', 'min_independent_expenditures_example'),
                    ('per_page', 20),
                    ('q_filer', ['q_filer_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('committee_type', ['committee_type_example']),
                    ('page', 1),
                    ('year', [56]),
                    ('committee_id', ['committee_id_example']),
                    ('min_cash_on_hand_end_period_amount', 'min_cash_on_hand_end_period_amount_example'),
                    ('min_disbursements_amount', 'min_disbursements_amount_example'),
                    ('most_recent', True)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reports/{entity_type}'.format(entity_type='entity_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_totals_by_entity_get(client):
    """Test case for totals_by_entity_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', 'end_date'),
                    ('cycle', 56),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/totals/by_entity/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_totals_entity_type_get(client):
    """Test case for totals_entity_type_get

    
    """
    params = [('treasurer_name', ['treasurer_name_example']),
                    ('max_disbursements', 'max_disbursements_example'),
                    ('committee_state', ['committee_state_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('sponsor_candidate_id', ['sponsor_candidate_id_example']),
                    ('min_disbursements', 'min_disbursements_example'),
                    ('min_last_cash_on_hand_end_period', 'min_last_cash_on_hand_end_period_example'),
                    ('max_last_cash_on_hand_end_period', 'max_last_cash_on_hand_end_period_example'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('filing_frequency', ['filing_frequency_example']),
                    ('sort', '-cycle'),
                    ('max_last_debts_owed_by_committee', 'max_last_debts_owed_by_committee_example'),
                    ('min_first_f1_date', '2013-10-20'),
                    ('committee_designation', ['committee_designation_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('max_receipts', 'max_receipts_example'),
                    ('committee_type', ['committee_type_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('min_last_debts_owed_by_committee', 'min_last_debts_owed_by_committee_example'),
                    ('max_first_f1_date', '2013-10-20'),
                    ('organization_type', ['organization_type_example']),
                    ('min_receipts', 'min_receipts_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/totals/{entity_type}'.format(entity_type='entity_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_totals_inaugural_committees_by_contributor_get(client):
    """Test case for totals_inaugural_committees_by_contributor_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('contributor_name', ['contributor_name_example']),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort', ["-total_donation"])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/totals/inaugural_committees/by_contributor/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

