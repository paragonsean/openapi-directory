# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_upsert import AccountUpsert


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_account_upserts_json_post(client):
    """Test case for v2_account_upserts_json_post

    Upsert an account
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'account_tier_id': 56,
        'city': 'city_example',
        'company_stage_id': 56,
        'company_type': 'company_type_example',
        'conversational_name': 'conversational_name_example',
        'country': 'country_example',
        'crm_id': 'crm_id_example',
        'crm_id_type': 'crm_id_type_example',
        'custom_fields': None,
        'description': 'description_example',
        'do_not_contact': True,
        'domain': 'domain_example',
        'founded': 'founded_example',
        'id': 56,
        'industry': 'industry_example',
        'linkedin_url': 'linkedin_url_example',
        'locale': 'locale_example',
        'name': 'name_example',
        'owner_id': 56,
        'phone': 'phone_example',
        'postal_code': 'postal_code_example',
        'revenue_range': 'revenue_range_example',
        'size': 'size_example',
        'state': 'state_example',
        'street': 'street_example',
        'tags': ['tags_example'],
        'twitter_handle': 'twitter_handle_example',
        'upsert_key': 'upsert_key_example',
        'website': 'website_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/account_upserts.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

