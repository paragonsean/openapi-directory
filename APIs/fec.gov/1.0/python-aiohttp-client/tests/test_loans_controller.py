# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedules_schedule_c_get_default_response import SchedulesScheduleCGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_c_sub_id_get(client):
    """Test case for schedules_schedule_c_sub_id_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', 'sort_example'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_c/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_cget(client):
    """Test case for schedules_schedule_cget

    
    """
    params = [('min_payment_to_date', 56),
                    ('max_image_number', 'max_image_number_example'),
                    ('min_image_number', 'min_image_number_example'),
                    ('max_incurred_date', '2013-10-20'),
                    ('sort_null_only', False),
                    ('last_index', 56),
                    ('sort_hide_null', False),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('loan_source_name', ['loan_source_name_example']),
                    ('line_number', 'line_number_example'),
                    ('sort', '-incurred_date'),
                    ('max_payment_to_date', 56),
                    ('candidate_name', ['candidate_name_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', True),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('min_incurred_date', '2013-10-20'),
                    ('max_amount', 'max_amount_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_c/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

