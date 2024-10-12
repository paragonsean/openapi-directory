# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.bad_word_filter_response import BadWordFilterResponse
from openapi_server.models.email_validate_response import EmailValidateResponse
from openapi_server.models.phone_validate_response import PhoneValidateResponse
from openapi_server.models.ua_lookup_response import UALookupResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_bad_word_filter(client):
    """Test case for bad_word_filter

    Bad Word Filter
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    data = {
        'catalog': 'strict',
        'censor_character': 'censor_character_example',
        'content': 'content_example'
        }
    response = await client.request(
        method='POST',
        path='/bad-word-filter',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_validate(client):
    """Test case for email_validate

    Email Validate
    """
    params = [('email', 'email_example'),
                    ('fix-typos', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/email-validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_validate(client):
    """Test case for phone_validate

    Phone Validate
    """
    params = [('number', 'number_example'),
                    ('country-code', 'country_code_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/phone-validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_u_a_lookup(client):
    """Test case for u_a_lookup

    UA Lookup
    """
    params = [('ua', 'ua_example'),
                    ('ua-version', 'ua_version_example'),
                    ('ua-platform', 'ua_platform_example'),
                    ('ua-platform-version', 'ua_platform_version_example'),
                    ('ua-mobile', 'ua_mobile_example'),
                    ('device-model', 'device_model_example'),
                    ('device-brand', 'device_brand_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ua-lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

