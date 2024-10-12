# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filings_page import FilingsPage
from openapi_server.models.operations_log_page import OperationsLogPage


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_filings_get(client):
    """Test case for candidate_candidate_id_filings_get

    
    """
    params = [('is_amended', True),
                    ('min_receipt_date', '2013-10-20'),
                    ('form_category', ['form_category_example']),
                    ('request_type', ['request_type_example']),
                    ('primary_general_indicator', ['primary_general_indicator_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('office', ['office_example']),
                    ('sort', ["-receipt_date"]),
                    ('q_filer', ['q_filer_example']),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('filer_type', 'filer_type_example'),
                    ('most_recent', True),
                    ('report_type', ['report_type_example']),
                    ('committee_type', 'committee_type_example'),
                    ('party', ['party_example']),
                    ('form_type', ['form_type_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('report_year', [56]),
                    ('amendment_indicator', ['amendment_indicator_example']),
                    ('document_type', ['document_type_example']),
                    ('beginning_image_number', ['beginning_image_number_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/filings'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_filings_get(client):
    """Test case for committee_committee_id_filings_get

    
    """
    params = [('is_amended', True),
                    ('min_receipt_date', '2013-10-20'),
                    ('form_category', ['form_category_example']),
                    ('request_type', ['request_type_example']),
                    ('primary_general_indicator', ['primary_general_indicator_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('office', ['office_example']),
                    ('sort', ["-receipt_date"]),
                    ('q_filer', ['q_filer_example']),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('filer_type', 'filer_type_example'),
                    ('most_recent', True),
                    ('report_type', ['report_type_example']),
                    ('committee_type', 'committee_type_example'),
                    ('party', ['party_example']),
                    ('form_type', ['form_type_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('report_year', [56]),
                    ('amendment_indicator', ['amendment_indicator_example']),
                    ('document_type', ['document_type_example']),
                    ('beginning_image_number', ['beginning_image_number_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/filings'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filings_get(client):
    """Test case for filings_get

    
    """
    params = [('is_amended', True),
                    ('min_receipt_date', '2013-10-20'),
                    ('form_category', ['form_category_example']),
                    ('request_type', ['request_type_example']),
                    ('primary_general_indicator', ['primary_general_indicator_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('office', ['office_example']),
                    ('sort', ["-receipt_date"]),
                    ('q_filer', ['q_filer_example']),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('filer_type', 'filer_type_example'),
                    ('most_recent', True),
                    ('report_type', ['report_type_example']),
                    ('committee_type', 'committee_type_example'),
                    ('party', ['party_example']),
                    ('form_type', ['form_type_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('report_year', [56]),
                    ('committee_id', ['committee_id_example']),
                    ('amendment_indicator', ['amendment_indicator_example']),
                    ('document_type', ['document_type_example']),
                    ('beginning_image_number', ['beginning_image_number_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/filings/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_log_get(client):
    """Test case for operations_log_get

    
    """
    params = [('min_receipt_date', '2013-10-20'),
                    ('candidate_committee_id', ['candidate_committee_id_example']),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('max_transaction_data_complete_date', '2013-10-20'),
                    ('per_page', 20),
                    ('sort', ["-report_year"]),
                    ('api_key', 'DEMO_KEY'),
                    ('report_type', ['report_type_example']),
                    ('min_transaction_data_complete_date', '2013-10-20'),
                    ('form_type', ['form_type_example']),
                    ('sort_nulls_last', False),
                    ('max_coverage_end_date', '2013-10-20'),
                    ('page', 1),
                    ('report_year', [56]),
                    ('status_num', ['status_num_example']),
                    ('amendment_indicator', ['amendment_indicator_example']),
                    ('beginning_image_number', ['beginning_image_number_example']),
                    ('min_coverage_end_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/operations-log/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

