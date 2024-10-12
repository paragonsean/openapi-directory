# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_domain import ApiV2010AccountSipSipDomain
from openapi_server.models.list_sip_domain_response import ListSipDomainResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sip_domain(client):
    """Test case for create_sip_domain

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'byoc_trunk_sid': 'byoc_trunk_sid_example',
        'domain_name': 'domain_name_example',
        'emergency_caller_sid': 'emergency_caller_sid_example',
        'emergency_calling_enabled': True,
        'friendly_name': 'friendly_name_example',
        'secure': True,
        'sip_registration': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_status_callback_method': 'voice_status_callback_method_example',
        'voice_status_callback_url': 'voice_status_callback_url_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/SIP/Domains.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sip_domain(client):
    """Test case for delete_sip_domain

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sip_domain(client):
    """Test case for fetch_sip_domain

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sip_domain(client):
    """Test case for list_sip_domain

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/SIP/Domains.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sip_domain(client):
    """Test case for update_sip_domain

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'byoc_trunk_sid': 'byoc_trunk_sid_example',
        'domain_name': 'domain_name_example',
        'emergency_caller_sid': 'emergency_caller_sid_example',
        'emergency_calling_enabled': True,
        'friendly_name': 'friendly_name_example',
        'secure': True,
        'sip_registration': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_status_callback_method': 'voice_status_callback_method_example',
        'voice_status_callback_url': 'voice_status_callback_url_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/SIP/Domains/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

