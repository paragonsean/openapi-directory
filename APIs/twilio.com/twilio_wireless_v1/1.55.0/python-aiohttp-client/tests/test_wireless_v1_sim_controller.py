# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sim_response import ListSimResponse
from openapi_server.models.sim_enum_reset_status import SimEnumResetStatus
from openapi_server.models.sim_enum_status import SimEnumStatus
from openapi_server.models.wireless_v1_sim import WirelessV1Sim


pytestmark = pytest.mark.asyncio

async def test_delete_sim(client):
    """Test case for delete_sim

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sim(client):
    """Test case for fetch_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sim(client):
    """Test case for list_sim

    
    """
    params = [('Status', openapi_server.SimEnumStatus()),
                    ('Iccid', 'iccid_example'),
                    ('RatePlan', 'rate_plan_example'),
                    ('EId', 'eid_example'),
                    ('SimRegistrationCode', 'sim_registration_code_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Sims',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sim(client):
    """Test case for update_sim

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'account_sid': 'account_sid_example',
        'callback_method': 'callback_method_example',
        'callback_url': 'callback_url_example',
        'commands_callback_method': 'commands_callback_method_example',
        'commands_callback_url': 'commands_callback_url_example',
        'friendly_name': 'friendly_name_example',
        'rate_plan': 'rate_plan_example',
        'reset_status': openapi_server.SimEnumResetStatus(),
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_url': 'sms_url_example',
        'status': openapi_server.SimEnumStatus(),
        'unique_name': 'unique_name_example',
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Sims/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

