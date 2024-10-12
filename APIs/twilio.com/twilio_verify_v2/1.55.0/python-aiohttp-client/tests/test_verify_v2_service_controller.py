# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.verify_v2_service import VerifyV2Service


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_service(client):
    """Test case for create_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'code_length': 56,
        'custom_code_enabled': True,
        'default_template_sid': 'default_template_sid_example',
        'do_not_share_warning_enabled': True,
        'dtmf_input_required': True,
        'friendly_name': 'friendly_name_example',
        'lookup_enabled': True,
        'psd2_enabled': True,
        'push_apn_credential_sid': 'push_apn_credential_sid_example',
        'push_fcm_credential_sid': 'push_fcm_credential_sid_example',
        'push_include_date': True,
        'skip_sms_to_landlines': True,
        'totp_code_length': 56,
        'totp_issuer': 'totp_issuer_example',
        'totp_skew': 56,
        'totp_time_step': 56,
        'tts_name': 'tts_name_example',
        'verify_event_subscription_enabled': True
        }
    response = await client.request(
        method='POST',
        path='/v2/Services',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_service(client):
    """Test case for fetch_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service(client):
    """Test case for list_service

    
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
        path='/v2/Services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_service(client):
    """Test case for update_service

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'code_length': 56,
        'custom_code_enabled': True,
        'default_template_sid': 'default_template_sid_example',
        'do_not_share_warning_enabled': True,
        'dtmf_input_required': True,
        'friendly_name': 'friendly_name_example',
        'lookup_enabled': True,
        'psd2_enabled': True,
        'push_apn_credential_sid': 'push_apn_credential_sid_example',
        'push_fcm_credential_sid': 'push_fcm_credential_sid_example',
        'push_include_date': True,
        'skip_sms_to_landlines': True,
        'totp_code_length': 56,
        'totp_issuer': 'totp_issuer_example',
        'totp_skew': 56,
        'totp_time_step': 56,
        'tts_name': 'tts_name_example',
        'verify_event_subscription_enabled': True
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

