# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_mobile import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile
from openapi_server.models.incoming_phone_number_mobile_enum_emergency_status import IncomingPhoneNumberMobileEnumEmergencyStatus
from openapi_server.models.incoming_phone_number_mobile_enum_voice_receive_mode import IncomingPhoneNumberMobileEnumVoiceReceiveMode
from openapi_server.models.list_available_phone_number_mobile_response import ListAvailablePhoneNumberMobileResponse
from openapi_server.models.list_incoming_phone_number_mobile_response import ListIncomingPhoneNumberMobileResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_incoming_phone_number_mobile(client):
    """Test case for create_incoming_phone_number_mobile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address_sid': 'address_sid_example',
        'api_version': 'api_version_example',
        'bundle_sid': 'bundle_sid_example',
        'emergency_address_sid': 'emergency_address_sid_example',
        'emergency_status': openapi_server.IncomingPhoneNumberMobileEnumEmergencyStatus(),
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
        'voice_receive_mode': openapi_server.IncomingPhoneNumberMobileEnumVoiceReceiveMode(),
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_available_phone_number_mobile(client):
    """Test case for list_available_phone_number_mobile

    
    """
    params = [('AreaCode', 56),
                    ('Contains', 'contains_example'),
                    ('SmsEnabled', True),
                    ('MmsEnabled', True),
                    ('VoiceEnabled', True),
                    ('ExcludeAllAddressRequired', True),
                    ('ExcludeLocalAddressRequired', True),
                    ('ExcludeForeignAddressRequired', True),
                    ('Beta', True),
                    ('NearNumber', 'near_number_example'),
                    ('NearLatLong', 'near_lat_long_example'),
                    ('Distance', 56),
                    ('InPostalCode', 'in_postal_code_example'),
                    ('InRegion', 'in_region_example'),
                    ('InRateCenter', 'in_rate_center_example'),
                    ('InLata', 'in_lata_example'),
                    ('InLocality', 'in_locality_example'),
                    ('FaxEnabled', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Mobile.json'.format(account_sid='account_sid_example', country_code='country_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_incoming_phone_number_mobile(client):
    """Test case for list_incoming_phone_number_mobile

    
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
        path='/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

