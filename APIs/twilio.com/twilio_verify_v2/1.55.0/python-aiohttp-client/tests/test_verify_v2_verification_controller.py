# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verification_enum_risk_check import VerificationEnumRiskCheck
from openapi_server.models.verification_enum_status import VerificationEnumStatus
from openapi_server.models.verify_v2_service_verification import VerifyV2ServiceVerification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_verification(client):
    """Test case for create_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'amount': 'amount_example',
        'app_hash': 'app_hash_example',
        'channel': 'channel_example',
        'channel_configuration': None,
        'custom_code': 'custom_code_example',
        'custom_friendly_name': 'custom_friendly_name_example',
        'custom_message': 'custom_message_example',
        'device_ip': 'device_ip_example',
        'locale': 'locale_example',
        'payee': 'payee_example',
        'rate_limits': None,
        'risk_check': openapi_server.VerificationEnumRiskCheck(),
        'send_digits': 'send_digits_example',
        'tags': 'tags_example',
        'template_custom_substitutions': 'template_custom_substitutions_example',
        'template_sid': 'template_sid_example',
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Verifications'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_verification(client):
    """Test case for fetch_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Verifications/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_verification(client):
    """Test case for update_verification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.VerificationEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Verifications/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

