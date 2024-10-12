# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedules_schedule_f_get_default_response import SchedulesScheduleFGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_f_sub_id_get(client):
    """Test case for schedules_schedule_f_sub_id_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_f/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_fget(client):
    """Test case for schedules_schedule_fget

    
    """
    params = [('min_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('cycle', [56]),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('payee_name', ['payee_name_example']),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('candidate_id', ['candidate_id_example']),
                    ('sort_hide_null', False),
                    ('line_number', 'line_number_example'),
                    ('sort', 'expenditure_date'),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('max_amount', 'max_amount_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_f/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

