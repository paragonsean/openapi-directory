# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedule_aby_employer_page import ScheduleAByEmployerPage
from openapi_server.models.schedule_aby_occupation_page import ScheduleAByOccupationPage
from openapi_server.models.schedule_aby_size_candidate_page import ScheduleABySizeCandidatePage
from openapi_server.models.schedule_aby_size_page import ScheduleABySizePage
from openapi_server.models.schedule_aby_state_candidate_page import ScheduleAByStateCandidatePage
from openapi_server.models.schedule_aby_state_page import ScheduleAByStatePage
from openapi_server.models.schedule_aby_state_recipient_totals_page import ScheduleAByStateRecipientTotalsPage
from openapi_server.models.schedule_aby_zip_page import ScheduleAByZipPage
from openapi_server.models.schedule_a_efile_page import ScheduleAEfilePage
from openapi_server.models.schedule_a_page import ScheduleAPage


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_a_efile_get(client):
    """Test case for schedules_schedule_a_efile_get

    
    """
    params = [('min_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('contributor_employer', ['contributor_employer_example']),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('contributor_name', ['contributor_name_example']),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('contributor_state', ['contributor_state_example']),
                    ('sort', '-contribution_receipt_date'),
                    ('line_number', 'line_number_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('contributor_occupation', ['contributor_occupation_example']),
                    ('contributor_city', ['contributor_city_example']),
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
        path='/v1/schedules/schedule_a/efile/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_a_sub_id_get(client):
    """Test case for schedules_schedule_a_sub_id_get

    
    """
    params = [('is_individual', True),
                    ('min_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('min_image_number', 'min_image_number_example'),
                    ('contributor_type', ['contributor_type_example']),
                    ('contributor_id', ['contributor_id_example']),
                    ('recipient_committee_org_type', ['recipient_committee_org_type_example']),
                    ('contributor_employer', ['contributor_employer_example']),
                    ('sort_null_only', False),
                    ('last_index', 56),
                    ('contributor_name', ['contributor_name_example']),
                    ('min_amount', 'min_amount_example'),
                    ('sort_hide_null', False),
                    ('recipient_committee_designation', ['recipient_committee_designation_example']),
                    ('max_load_date', '2013-10-20'),
                    ('recipient_committee_type', ['recipient_committee_type_example']),
                    ('sort', '-contribution_receipt_date'),
                    ('last_contribution_receipt_date', '2013-10-20'),
                    ('last_contribution_receipt_amount', 3.4),
                    ('line_number', 'line_number_example'),
                    ('contributor_state', ['contributor_state_example']),
                    ('per_page', 20),
                    ('api_key', 'DEMO_KEY'),
                    ('two_year_transaction_period', [56]),
                    ('contributor_zip', ['contributor_zip_example']),
                    ('min_load_date', '2013-10-20'),
                    ('contributor_occupation', ['contributor_occupation_example']),
                    ('contributor_city', ['contributor_city_example']),
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
        path='/v1/schedules/schedule_a/{sub_id}'.format(sub_id='sub_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_employer_get(client):
    """Test case for schedules_schedule_aby_employer_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('employer', ['employer_example']),
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
        path='/v1/schedules/schedule_a/by_employer/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_occupation_get(client):
    """Test case for schedules_schedule_aby_occupation_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('occupation', ['occupation_example']),
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
        path='/v1/schedules/schedule_a/by_occupation/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_size_by_candidate_get(client):
    """Test case for schedules_schedule_aby_size_by_candidate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('sort_nulls_last', False),
                    ('page', 1),
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
        path='/v1/schedules/schedule_a/by_size/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_size_get(client):
    """Test case for schedules_schedule_aby_size_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_null_only', False),
                    ('size', [56]),
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
        path='/v1/schedules/schedule_a/by_size/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_state_by_candidate_get(client):
    """Test case for schedules_schedule_aby_state_by_candidate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('sort_nulls_last', False),
                    ('page', 1),
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
        path='/v1/schedules/schedule_a/by_state/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_state_by_candidate_totals_get(client):
    """Test case for schedules_schedule_aby_state_by_candidate_totals_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('sort_nulls_last', False),
                    ('page', 1),
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
        path='/v1/schedules/schedule_a/by_state/by_candidate/totals/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_state_get(client):
    """Test case for schedules_schedule_aby_state_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('hide_null', False),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort', '-total')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_a/by_state/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_state_totals_get(client):
    """Test case for schedules_schedule_aby_state_totals_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('committee_type', ['committee_type_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort', 'cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/schedules/schedule_a/by_state/totals/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aby_zip_get(client):
    """Test case for schedules_schedule_aby_zip_get

    
    """
    params = [('zip', ['zip_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', ['state_example']),
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
        path='/v1/schedules/schedule_a/by_zip/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_schedule_aget(client):
    """Test case for schedules_schedule_aget

    
    """
    params = [('is_individual', True),
                    ('min_date', '2013-10-20'),
                    ('max_image_number', 'max_image_number_example'),
                    ('min_image_number', 'min_image_number_example'),
                    ('contributor_type', ['contributor_type_example']),
                    ('contributor_id', ['contributor_id_example']),
                    ('recipient_committee_org_type', ['recipient_committee_org_type_example']),
                    ('contributor_employer', ['contributor_employer_example']),
                    ('sort_null_only', False),
                    ('last_index', 56),
                    ('contributor_name', ['contributor_name_example']),
                    ('min_amount', 'min_amount_example'),
                    ('sort_hide_null', False),
                    ('recipient_committee_designation', ['recipient_committee_designation_example']),
                    ('max_load_date', '2013-10-20'),
                    ('recipient_committee_type', ['recipient_committee_type_example']),
                    ('sort', '-contribution_receipt_date'),
                    ('last_contribution_receipt_date', '2013-10-20'),
                    ('last_contribution_receipt_amount', 3.4),
                    ('line_number', 'line_number_example'),
                    ('contributor_state', ['contributor_state_example']),
                    ('per_page', 20),
                    ('api_key', 'DEMO_KEY'),
                    ('two_year_transaction_period', [56]),
                    ('contributor_zip', ['contributor_zip_example']),
                    ('min_load_date', '2013-10-20'),
                    ('contributor_occupation', ['contributor_occupation_example']),
                    ('contributor_city', ['contributor_city_example']),
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
        path='/v1/schedules/schedule_a/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

