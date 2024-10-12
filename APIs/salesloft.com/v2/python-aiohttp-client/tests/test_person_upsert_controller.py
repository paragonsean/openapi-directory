# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.person_upsert import PersonUpsert


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_person_upserts_json_post(client):
    """Test case for v2_person_upserts_json_post

    Upsert a person
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
        'id': 56,
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
        'upsert_key': 'upsert_key_example',
        'work_city': 'work_city_example',
        'work_country': 'work_country_example',
        'work_state': 'work_state_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/person_upserts.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

