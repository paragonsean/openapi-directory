# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account


pytestmark = pytest.mark.asyncio

async def test_v2_accounts_id_json_delete(client):
    """Test case for v2_accounts_id_json_delete

    Delete an account
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/accounts/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_accounts_id_json_get(client):
    """Test case for v2_accounts_id_json_get

    Fetch an account
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_accounts_id_json_put(client):
    """Test case for v2_accounts_id_json_put

    Update an existing Account
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'account_tier_id': 56,
        'archived': True,
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
        'website': 'website_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/accounts/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_accounts_json_get(client):
    """Test case for v2_accounts_json_get

    List accounts
    """
    params = [('ids', [56]),
                    ('crm_id', ['crm_id_example']),
                    ('tag', ['tag_example']),
                    ('tag_id', [56]),
                    ('created_at', ['created_at_example']),
                    ('updated_at', ['updated_at_example']),
                    ('domain', 'domain_example'),
                    ('website', ['website_example']),
                    ('archived', True),
                    ('name', ['name_example']),
                    ('account_stage_id', [56]),
                    ('account_tier_id', [56]),
                    ('owner_id', ['owner_id_example']),
                    ('owner_is_active', True),
                    ('last_contacted', None),
                    ('custom_fields', None),
                    ('industry', ['industry_example']),
                    ('country', ['country_example']),
                    ('state', ['state_example']),
                    ('city', ['city_example']),
                    ('owner_crm_id', ['owner_crm_id_example']),
                    ('locales', ['locales_example']),
                    ('user_relationships', None),
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
        path='/v2/accounts.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_accounts_json_post(client):
    """Test case for v2_accounts_json_post

    Create an account
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
        'website': 'website_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/accounts.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

