# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedules_schedule_d_get_default_response import SchedulesScheduleDGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_d_sub_id_get(client):
    """Test case for schedules_schedule_d_sub_id_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', 'load_date'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_d/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_dget(client):
    """Test case for schedules_schedule_dget

    
    """
    params = [('max_payment_period', 3.4),
                    ('min_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('max_amount_outstanding_close', 3.4),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('min_payment_period', 3.4),
                    ('min_amount_incurred', 3.4),
                    ('creditor_debtor_name', ['creditor_debtor_name_example']),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('min_amount_outstanding_beginning', 3.4),
                    ('sort', 'load_date'),
                    ('min_amount_outstanding_close', 3.4),
                    ('api_key', 'DEMO_KEY'),
                    ('nature_of_debt', 'nature_of_debt_example'),
                    ('max_amount_incurred', 3.4),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('max_amount_outstanding_beginning', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_d/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

