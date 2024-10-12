# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number import ApiV2010AccountIncomingPhoneNumber
from openapi_server.models.incoming_phone_number_enum_emergency_status import IncomingPhoneNumberEnumEmergencyStatus
from openapi_server.models.incoming_phone_number_enum_voice_receive_mode import IncomingPhoneNumberEnumVoiceReceiveMode
from openapi_server.models.list_incoming_phone_number_response import ListIncomingPhoneNumberResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_incoming_phone_number(client):
    """Test case for create_incoming_phone_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address_sid': 'address_sid_example',
        'api_version': 'api_version_example',
        'area_code': 'area_code_example',
        'bundle_sid': 'bundle_sid_example',
        'emergency_address_sid': 'emergency_address_sid_example',
        'emergency_status': openapi_server.IncomingPhoneNumberEnumEmergencyStatus(),
        'friendly_name': 'friendly_name_example',
        'identity_sid': 'identity_sid_example',
        'phone_number': 'phone_number_example',
        'sms_application_sid': 'sms_application_sid_example',
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_url': 'sms_url_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'trunk_sid': 'trunk_sid_example',
        'voice_application_sid': 'voice_application_sid_example',
        'voice_caller_id_lookup': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_receive_mode': openapi_server.IncomingPhoneNumberEnumVoiceReceiveMode(),
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_incoming_phone_number(client):
    """Test case for delete_incoming_phone_number

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_incoming_phone_number(client):
    """Test case for fetch_incoming_phone_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incoming_phone_number(client):
    """Test case for list_incoming_phone_number

    
    """
    params = [('Beta', True),
                    ('FriendlyName', 'friendly_name_example'),
                    ('PhoneNumber', 'phone_number_example'),
                    ('Origin', 'origin_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_incoming_phone_number(client):
    """Test case for update_incoming_phone_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'account_sid2': 'account_sid_example',
        'address_sid': 'address_sid_example',
        'api_version': 'api_version_example',
        'bundle_sid': 'bundle_sid_example',
        'emergency_address_sid': 'emergency_address_sid_example',
        'emergency_status': openapi_server.IncomingPhoneNumberEnumEmergencyStatus(),
        'friendly_name': 'friendly_name_example',
        'identity_sid': 'identity_sid_example',
        'sms_application_sid': 'sms_application_sid_example',
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_url': 'sms_url_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'trunk_sid': 'trunk_sid_example',
        'voice_application_sid': 'voice_application_sid_example',
        'voice_caller_id_lookup': True,
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_receive_mode': openapi_server.IncomingPhoneNumberEnumVoiceReceiveMode(),
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

