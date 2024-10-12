# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar_date_page import CalendarDatePage
from openapi_server.models.election_dates_get_default_response import ElectionDatesGetDefaultResponse
from openapi_server.models.reporting_dates_get_default_response import ReportingDatesGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_calendar_dates_export_get(client):
    """Test case for calendar_dates_export_get

    
    """
    params = [('calendar_category_id', [56]),
                    ('api_key', 'DEMO_KEY'),
                    ('description', ['description_example']),
                    ('sort_nulls_last', False),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('max_end_date', '2013-10-20'),
                    ('summary', ['summary_example']),
                    ('min_end_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('min_start_date', '2013-10-20'),
                    ('per_page', 20),
                    ('max_start_date', '2013-10-20'),
                    ('renderer', ics),
                    ('sort', '-start_date'),
                    ('event_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/calendar-dates/export/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_dates_get(client):
    """Test case for calendar_dates_get

    
    """
    params = [('calendar_category_id', [56]),
                    ('api_key', 'DEMO_KEY'),
                    ('description', ['description_example']),
                    ('sort_nulls_last', False),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('max_end_date', '2013-10-20'),
                    ('summary', ['summary_example']),
                    ('min_end_date', '2013-10-20'),
                    ('sort_hide_null', False),
                    ('min_start_date', '2013-10-20'),
                    ('max_start_date', '2013-10-20'),
                    ('per_page', 20),
                    ('sort', '-start_date'),
                    ('event_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/calendar-dates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_election_dates_get(client):
    """Test case for election_dates_get

    
    """
    params = [('election_state', ['election_state_example']),
                    ('max_election_date', '2013-10-20'),
                    ('election_district', ['election_district_example']),
                    ('min_update_date', '2013-10-20'),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('max_create_date', '2013-10-20'),
                    ('per_page', 20),
                    ('election_year', ['election_year_example']),
                    ('sort', '-election_date'),
                    ('min_create_date', '2013-10-20'),
                    ('api_key', 'DEMO_KEY'),
                    ('election_party', ['election_party_example']),
                    ('office_sought', ['office_sought_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('max_update_date', '2013-10-20'),
                    ('election_type_id', ['election_type_id_example']),
                    ('max_primary_general_date', '2013-10-20'),
                    ('min_election_date', '2013-10-20'),
                    ('min_primary_general_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/election-dates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_dates_get(client):
    """Test case for reporting_dates_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('min_update_date', '2013-10-20'),
                    ('report_type', ['report_type_example']),
                    ('min_due_date', '2013-10-20'),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('max_due_date', '2013-10-20'),
                    ('report_year', [56]),
                    ('sort_nulls_last', False),
                    ('max_create_date', '2013-10-20'),
                    ('max_update_date', '2013-10-20'),
                    ('per_page', 20),
                    ('sort_hide_null', False),
                    ('sort', '-due_date'),
                    ('min_create_date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reporting-dates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

