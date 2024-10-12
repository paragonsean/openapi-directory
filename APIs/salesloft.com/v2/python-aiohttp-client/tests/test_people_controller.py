# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.person import Person


pytestmark = pytest.mark.asyncio

async def test_v2_people_id_json_delete(client):
    """Test case for v2_people_id_json_delete

    Delete a person
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/people/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_people_id_json_get(client):
    """Test case for v2_people_id_json_get

    Fetch a person
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/people/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_people_id_json_put(client):
    """Test case for v2_people_id_json_put

    Update a person
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'account_id': 56,
        'city': 'city_example',
        'contact_restrictions': ['contact_restrictions_example'],
        'country': 'country_example',
        'crm_id': 'crm_id_example',
        'crm_id_type': 'crm_id_type_example',
        'custom_fields': None,
        'do_not_contact': True,
        'email_address': 'email_address_example',
        'first_name': 'first_name_example',
        'home_phone': 'home_phone_example',
        'import_id': 56,
        'job_seniority': 'job_seniority_example',
        'last_name': 'last_name_example',
        'linkedin_url': 'linkedin_url_example',
        'locale': 'locale_example',
        'mobile_phone': 'mobile_phone_example',
        'owner_id': 56,
        'person_company_industry': 'person_company_industry_example',
        'person_company_name': 'person_company_name_example',
        'person_company_website': 'person_company_website_example',
        'person_stage_id': 56,
        'personal_email_address': 'personal_email_address_example',
        'personal_website': 'personal_website_example',
        'phone': 'phone_example',
        'phone_extension': 'phone_extension_example',
        'secondary_email_address': 'secondary_email_address_example',
        'state': 'state_example',
        'tags': ['tags_example'],
        'title': 'title_example',
        'twitter_handle': 'twitter_handle_example',
        'work_city': 'work_city_example',
        'work_country': 'work_country_example',
        'work_state': 'work_state_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/people/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_people_json_get(client):
    """Test case for v2_people_json_get

    List people
    """
    params = [('ids', [56]),
                    ('updated_at', ['updated_at_example']),
                    ('email_addresses', ['email_addresses_example']),
                    ('owned_by_guid', ['owned_by_guid_example']),
                    ('person_stage_id', [56]),
                    ('crm_id', ['crm_id_example']),
                    ('owner_crm_id', ['owner_crm_id_example']),
                    ('do_not_contact', True),
                    ('can_email', True),
                    ('can_call', True),
                    ('can_text', True),
                    ('account_id', [56]),
                    ('custom_fields', None),
                    ('import_id', [56]),
                    ('job_seniority', ['job_seniority_example']),
                    ('tag_id', [56]),
                    ('owner_is_active', True),
                    ('cadence_id', [56]),
                    ('starred_by_guid', ['starred_by_guid_example']),
                    ('replied', True),
                    ('bounced', True),
                    ('success', True),
                    ('eu_resident', True),
                    ('title', ['title_example']),
                    ('country', ['country_example']),
                    ('state', ['state_example']),
                    ('city', ['city_example']),
                    ('last_contacted', None),
                    ('created_at', None),
                    ('new', True),
                    ('phone_number', True),
                    ('locales', ['locales_example']),
                    ('owner_id', [56]),
                    ('_query', 'query_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/people.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_people_json_post(client):
    """Test case for v2_people_json_post

    Create a person
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'account_id': 56,
        'autotag_date': True,
        'city': 'city_example',
        'contact_restrictions': ['contact_restrictions_example'],
        'country': 'country_example',
        'crm_id': 'crm_id_example',
        'crm_id_type': 'crm_id_type_example',
        'custom_fields': None,
        'do_not_contact': True,
        'email_address': 'email_address_example',
        'first_name': 'first_name_example',
        'home_phone': 'home_phone_example',
        'import_id': 56,
        'job_seniority': 'job_seniority_example',
        'last_name': 'last_name_example',
        'linkedin_url': 'linkedin_url_example',
        'locale': 'locale_example',
        'mobile_phone': 'mobile_phone_example',
        'owner_id': 56,
        'person_company_industry': 'person_company_industry_example',
        'person_company_name': 'person_company_name_example',
        'person_company_website': 'person_company_website_example',
        'person_stage_id': 56,
        'personal_email_address': 'personal_email_address_example',
        'personal_website': 'personal_website_example',
        'phone': 'phone_example',
        'phone_extension': 'phone_extension_example',
        'secondary_email_address': 'secondary_email_address_example',
        'state': 'state_example',
        'tags': ['tags_example'],
        'title': 'title_example',
        'twitter_handle': 'twitter_handle_example',
        'work_city': 'work_city_example',
        'work_country': 'work_country_example',
        'work_state': 'work_state_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/people.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

