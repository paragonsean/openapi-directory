# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedule_bby_purpose_page import ScheduleBByPurposePage
from openapi_server.models.schedule_bby_recipient_id_page import ScheduleBByRecipientIDPage
from openapi_server.models.schedule_bby_recipient_page import ScheduleBByRecipientPage
from openapi_server.models.schedule_b_efile_page import ScheduleBEfilePage
from openapi_server.models.schedule_b_page import ScheduleBPage


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_b_efile_get(client):
    """Test case for schedules_schedule_b_efile_get

    
    """
    params = [('min_date', '2013-10-20'),
                    ('api_key', 'DEMO_KEY'),
                    ('disbursement_description', ['disbursement_description_example']),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('image_number', ['image_number_example']),
                    ('sort_hide_null', False),
                    ('max_date', '2013-10-20'),
                    ('per_page', 20),
                    ('min_amount', 'min_amount_example'),
                    ('max_amount', 'max_amount_example'),
                    ('sort', '-disbursement_date'),
                    ('recipient_city', ['recipient_city_example']),
                    ('recipient_state', ['recipient_state_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_b/efile/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_b_sub_id_get(client):
    """Test case for schedules_schedule_b_sub_id_get

    
    """
    params = [('min_date', '2013-10-20'),
                    ('spender_committee_designation', ['spender_committee_designation_example']),
                    ('recipient_committee_id', ['recipient_committee_id_example']),
                    ('last_disbursement_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('disbursement_description', ['disbursement_description_example']),
                    ('disbursement_purpose_category', ['disbursement_purpose_category_example']),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('last_index', 56),
                    ('sort_hide_null', False),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('line_number', 'line_number_example'),
                    ('sort', '-disbursement_date'),
                    ('recipient_city', ['recipient_city_example']),
                    ('spender_committee_type', ['spender_committee_type_example']),
                    ('last_disbursement_amount', 3.4),
                    ('spender_committee_org_type', ['spender_committee_org_type_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('two_year_transaction_period', [56]),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('recipient_name', ['recipient_name_example']),
                    ('max_amount', 'max_amount_example'),
                    ('recipient_state', ['recipient_state_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_b/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_bby_purpose_get(client):
    """Test case for schedules_schedule_bby_purpose_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('purpose', ['purpose_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
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
        path='/v1/schedules/schedule_b/by_purpose/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_bby_recipient_get(client):
    """Test case for schedules_schedule_bby_recipient_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('recipient_name', ['recipient_name_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
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
        path='/v1/schedules/schedule_b/by_recipient/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_bby_recipient_id_get(client):
    """Test case for schedules_schedule_bby_recipient_id_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('recipient_id', ['recipient_id_example']),
                    ('sort_hide_null', False),
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
        path='/v1/schedules/schedule_b/by_recipient_id/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_bget(client):
    """Test case for schedules_schedule_bget

    
    """
    params = [('min_date', '2013-10-20'),
                    ('spender_committee_designation', ['spender_committee_designation_example']),
                    ('recipient_committee_id', ['recipient_committee_id_example']),
                    ('last_disbursement_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('disbursement_description', ['disbursement_description_example']),
                    ('disbursement_purpose_category', ['disbursement_purpose_category_example']),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('last_index', 56),
                    ('sort_hide_null', False),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('line_number', 'line_number_example'),
                    ('sort', '-disbursement_date'),
                    ('recipient_city', ['recipient_city_example']),
                    ('spender_committee_type', ['spender_committee_type_example']),
                    ('last_disbursement_amount', 3.4),
                    ('spender_committee_org_type', ['spender_committee_org_type_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('two_year_transaction_period', [56]),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('recipient_name', ['recipient_name_example']),
                    ('max_amount', 'max_amount_example'),
                    ('recipient_state', ['recipient_state_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_b/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

