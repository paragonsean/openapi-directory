# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hosted_number_order_enum_status import HostedNumberOrderEnumStatus
from openapi_server.models.hosted_number_order_enum_verification_type import HostedNumberOrderEnumVerificationType
from openapi_server.models.list_hosted_numbers_hosted_number_order_response import ListHostedNumbersHostedNumberOrderResponse
from openapi_server.models.preview_hosted_numbers_hosted_number_order import PreviewHostedNumbersHostedNumberOrder


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_hosted_numbers_hosted_number_order(client):
    """Test case for create_hosted_numbers_hosted_number_order

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'account_sid': 'account_sid_example',
        'address_sid': 'address_sid_example',
        'cc_emails': ['cc_emails_example'],
        'email': 'email_example',
        'friendly_name': 'friendly_name_example',
        'phone_number': 'phone_number_example',
        'sms_application_sid': 'sms_application_sid_example',
        'sms_capability': True,
        'sms_fallback_method': 'sms_fallback_method_example',
        'sms_fallback_url': 'sms_fallback_url_example',
        'sms_method': 'sms_method_example',
        'sms_url': 'sms_url_example',
        'status_callback_method': 'status_callback_method_example',
        'status_callback_url': 'status_callback_url_example',
        'unique_name': 'unique_name_example',
        'verification_document_sid': 'verification_document_sid_example',
        'verification_type': openapi_server.HostedNumberOrderEnumVerificationType()
        }
    response = await client.request(
        method='POST',
        path='/HostedNumbers/HostedNumberOrders',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hosted_numbers_hosted_number_order(client):
    """Test case for delete_hosted_numbers_hosted_number_order

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/HostedNumbers/HostedNumberOrders/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_hosted_numbers_hosted_number_order(client):
    """Test case for fetch_hosted_numbers_hosted_number_order

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/HostedNumbers/HostedNumberOrders/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hosted_numbers_hosted_number_order(client):
    """Test case for list_hosted_numbers_hosted_number_order

    
    """
    params = [('Status', openapi_server.HostedNumberOrderEnumStatus()),
                    ('PhoneNumber', 'phone_number_example'),
                    ('IncomingPhoneNumberSid', 'incoming_phone_number_sid_example'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('UniqueName', 'unique_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/HostedNumbers/HostedNumberOrders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_hosted_numbers_hosted_number_order(client):
    """Test case for update_hosted_numbers_hosted_number_order

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_delay': 56,
        'cc_emails': ['cc_emails_example'],
        'email': 'email_example',
        'extension': 'extension_example',
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.HostedNumberOrderEnumStatus(),
        'unique_name': 'unique_name_example',
        'verification_code': 'verification_code_example',
        'verification_document_sid': 'verification_document_sid_example',
        'verification_type': openapi_server.HostedNumberOrderEnumVerificationType()
        }
    response = await client.request(
        method='POST',
        path='/HostedNumbers/HostedNumberOrders/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

