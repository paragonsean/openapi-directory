# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_events0_get(client):
    """Test case for events0_get

    
    """
    params = [('filter_by_custom_event_field__custom_NNNNNN', 'filter_by_custom_event_field__custom_nnnnnn_example'),
                    ('filter_by_integration_metadata_field_1', 'filter_by_integration_metadata_field_1_example'),
                    ('filter_by_integration_metadata_field_2', 'filter_by_integration_metadata_field_2_example'),
                    ('filter_by_integration_metadata_field_3', 'filter_by_integration_metadata_field_3_example'),
                    ('filter_by_integration_metadata_field_4', 'filter_by_integration_metadata_field_4_example'),
                    ('filter_by_integration_metadata_field_5', 'filter_by_integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'filter_by_event_name_contains_text': 'filter_by_event_name_contains_text_example',
        'filter_by_start_date_greater_than_or_equal_to': '2013-10-20',
        'filter_by_start_date_smaller_than_or_equal_to': '2013-10-20',
        'filter_by_end_date_greater_than_or_equal_to': '2013-10-20',
        'filter_by_end_date_smaller_than_or_equal_to': '2013-10-20',
        'filter_by_event_participation_type_id': 3.4,
        'filter_by_event_format_id': 3.4,
        'filter_by_event_star_rating': 3.4,
        'filter_by_event_tag': 'filter_by_event_tag_example',
        'hydrate_tasks': 'false',
        'hydrate_task_sections_list': 'false',
        'hydrate_custom_fields': 'false',
    }
    response = await client.request(
        method='GET',
        path='/v1/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events1_post(client):
    """Test case for events1_post

    
    """
    params = [('integration_metadata_field_1', 'integration_metadata_field_1_example'),
                    ('integration_metadata_field_2', 'integration_metadata_field_2_example'),
                    ('integration_metadata_field_3', 'integration_metadata_field_3_example'),
                    ('integration_metadata_field_4', 'integration_metadata_field_4_example'),
                    ('integration_metadata_field_5', 'integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'name': 'name_example',
        'start_date': '2013-10-20',
        'end_date': '2013-10-20',
        'format_id': 1.0,
        'participation_type_id': 1.0,
    }
    response = await client.request(
        method='POST',
        path='/v1/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events2_patch(client):
    """Test case for events2_patch

    
    """
    params = [('website_url', 'website_url_example'),
                    ('venue_name', 'venue_name_example'),
                    ('event_notes', 3.4),
                    ('booth_notes', 3.4),
                    ('budget_notes', 3.4),
                    ('roi_notes', 3.4),
                    ('integration_metadata_field_1', 'integration_metadata_field_1_example'),
                    ('integration_metadata_field_2', 'integration_metadata_field_2_example'),
                    ('integration_metadata_field_3', 'integration_metadata_field_3_example'),
                    ('integration_metadata_field_4', 'integration_metadata_field_4_example'),
                    ('integration_metadata_field_5', 'integration_metadata_field_5_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
        'name': 'name_example',
        'start_date': '2013-10-20',
        'end_date': '2013-10-20',
        'participation_type_id': 3.4,
        'format_id': 3.4,
        'star_rating': 3.4,
        'booth_size': 3.4,
        'booth_number': 3.4,
        'budget_booth_reservation': 3.4,
        'budget_booth_services': 3.4,
        'budget_attendee_registrations': 3.4,
        'budget_travel': 3.4,
        'budget_giveaways': 3.4,
        'budget_shipments': 3.4,
        'budget_misc_expenses': 3.4,
        'budget_sponsorships': 3.4,
        'roi_num_leads': 3.4,
        'roi_num_impressions_booth': 3.4,
        'roi_num_impressions_sponsorships': 3.4,
        'roi_num_impressions_media': 3.4,
        'roi_num_meetings_existing_customers': 3.4,
        'roi_num_meetings_new_customers': 3.4,
        'roi_amount_actual_sales': 3.4,
        'roi_amount_potential_sales': 3.4,
    }
    response = await client.request(
        method='PATCH',
        path='/v1/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events3_delete(client):
    """Test case for events3_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='DELETE',
        path='/v1/events/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_info0_get(client):
    """Test case for events_info0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
        'id': 3.4,
    }
    response = await client.request(
        method='GET',
        path='/v1/events/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

