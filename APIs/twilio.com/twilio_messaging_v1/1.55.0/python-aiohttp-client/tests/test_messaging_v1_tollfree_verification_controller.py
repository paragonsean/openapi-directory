# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_tollfree_verification_response import ListTollfreeVerificationResponse
from openapi_server.models.messaging_v1_tollfree_verification import MessagingV1TollfreeVerification
from openapi_server.models.tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInType
from openapi_server.models.tollfree_verification_enum_status import TollfreeVerificationEnumStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_tollfree_verification(client):
    """Test case for create_tollfree_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'additional_information': 'additional_information_example',
        'business_city': 'business_city_example',
        'business_contact_email': 'business_contact_email_example',
        'business_contact_first_name': 'business_contact_first_name_example',
        'business_contact_last_name': 'business_contact_last_name_example',
        'business_contact_phone': 'business_contact_phone_example',
        'business_country': 'business_country_example',
        'business_name': 'business_name_example',
        'business_postal_code': 'business_postal_code_example',
        'business_state_province_region': 'business_state_province_region_example',
        'business_street_address': 'business_street_address_example',
        'business_street_address2': 'business_street_address2_example',
        'business_website': 'business_website_example',
        'customer_profile_sid': 'customer_profile_sid_example',
        'external_reference_id': 'external_reference_id_example',
        'message_volume': 'message_volume_example',
        'notification_email': 'notification_email_example',
        'opt_in_image_urls': ['opt_in_image_urls_example'],
        'opt_in_type': openapi_server.TollfreeVerificationEnumOptInType(),
        'production_message_sample': 'production_message_sample_example',
        'tollfree_phone_number_sid': 'tollfree_phone_number_sid_example',
        'use_case_categories': ['use_case_categories_example'],
        'use_case_summary': 'use_case_summary_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Tollfree/Verifications',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tollfree_verification(client):
    """Test case for delete_tollfree_verification

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Tollfree/Verifications/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_tollfree_verification(client):
    """Test case for fetch_tollfree_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Tollfree/Verifications/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tollfree_verification(client):
    """Test case for list_tollfree_verification

    
    """
    params = [('TollfreePhoneNumberSid', 'tollfree_phone_number_sid_example'),
                    ('Status', openapi_server.TollfreeVerificationEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Tollfree/Verifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_tollfree_verification(client):
    """Test case for update_tollfree_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'additional_information': 'additional_information_example',
        'business_city': 'business_city_example',
        'business_contact_email': 'business_contact_email_example',
        'business_contact_first_name': 'business_contact_first_name_example',
        'business_contact_last_name': 'business_contact_last_name_example',
        'business_contact_phone': 'business_contact_phone_example',
        'business_country': 'business_country_example',
        'business_name': 'business_name_example',
        'business_postal_code': 'business_postal_code_example',
        'business_state_province_region': 'business_state_province_region_example',
        'business_street_address': 'business_street_address_example',
        'business_street_address2': 'business_street_address2_example',
        'business_website': 'business_website_example',
        'edit_reason': 'edit_reason_example',
        'message_volume': 'message_volume_example',
        'notification_email': 'notification_email_example',
        'opt_in_image_urls': ['opt_in_image_urls_example'],
        'opt_in_type': openapi_server.TollfreeVerificationEnumOptInType(),
        'production_message_sample': 'production_message_sample_example',
        'use_case_categories': ['use_case_categories_example'],
        'use_case_summary': 'use_case_summary_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Tollfree/Verifications/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

