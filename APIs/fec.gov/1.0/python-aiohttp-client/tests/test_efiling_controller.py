# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_f3_filing_page import BaseF3FilingPage
from openapi_server.models.base_f3_p_filing_page import BaseF3PFilingPage
from openapi_server.models.base_f3_x_filing_page import BaseF3XFilingPage
from openapi_server.models.e_filings_page import EFilingsPage


pytestmark = pytest.mark.asyncio

async def test_efile_filings_get(client):
    """Test case for efile_filings_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_receipt_date', '2013-10-20'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('sort', '-receipt_date'),
                    ('q_filer', ['q_filer_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/efile/filings/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_efile_reports_house_senate_get(client):
    """Test case for efile_reports_house_senate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_receipt_date', '2013-10-20'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('sort', '-receipt_date'),
                    ('q_filer', ['q_filer_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/efile/reports/house-senate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_efile_reports_pac_party_get(client):
    """Test case for efile_reports_pac_party_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_receipt_date', '2013-10-20'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('sort', '-receipt_date'),
                    ('q_filer', ['q_filer_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/efile/reports/pac-party/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_efile_reports_presidential_get(client):
    """Test case for efile_reports_presidential_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_receipt_date', '2013-10-20'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('max_receipt_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('file_number', [56]),
                    ('per_page', 20),
                    ('sort', '-receipt_date'),
                    ('q_filer', ['q_filer_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/efile/reports/presidential/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

