# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.hlr_lookup_response import HLRLookupResponse
from openapi_server.models.phone_playback_response import PhonePlaybackResponse
from openapi_server.models.phone_verify_response import PhoneVerifyResponse
from openapi_server.models.sms_verify_response import SMSVerifyResponse
from openapi_server.models.verify_security_code_response import VerifySecurityCodeResponse


pytestmark = pytest.mark.asyncio

async def test_h_lr_lookup(client):
    """Test case for h_lr_lookup

    HLR Lookup
    """
    params = [('number', 'number_example'),
                    ('country-code', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/hlr-lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_phone_playback(client):
    """Test case for phone_playback

    Phone Playback
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'audio_url': 'audio_url_example',
        'limit': 3,
        'limit_ttl': 1,
        'number': 'number_example'
        }
    response = await client.request(
        method='POST',
        path='/phone-playback',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_phone_verify(client):
    """Test case for phone_verify

    Phone Verify
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'code_length': 6,
        'country_code': 'country_code_example',
        'language_code': 'en',
        'limit': 3,
        'limit_ttl': 1,
        'number': 'number_example',
        'playback_delay': 800,
        'security_code': 56
        }
    response = await client.request(
        method='POST',
        path='/phone-verify',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_s_ms_verify(client):
    """Test case for s_ms_verify

    SMS Verify
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'code_length': 5,
        'country_code': 'country_code_example',
        'language_code': 'en',
        'limit': 10,
        'limit_ttl': 1,
        'number': 'number_example',
        'security_code': 56
        }
    response = await client.request(
        method='POST',
        path='/sms-verify',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_security_code(client):
    """Test case for verify_security_code

    Verify Security Code
    """
    params = [('security-code', 'security_code_example'),
                    ('limit-by', 'limit_by_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/verify-security-code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

