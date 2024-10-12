# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_verification_attempt_response import ListVerificationAttemptResponse
from openapi_server.models.verification_attempt_enum_channels import VerificationAttemptEnumChannels
from openapi_server.models.verification_attempt_enum_conversion_status import VerificationAttemptEnumConversionStatus
from openapi_server.models.verify_v2_verification_attempt import VerifyV2VerificationAttempt


pytestmark = pytest.mark.asyncio

async def test_fetch_verification_attempt(client):
    """Test case for fetch_verification_attempt

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Attempts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_verification_attempt(client):
    """Test case for list_verification_attempt

    
    """
    params = [('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('ChannelData.To', 'channel_data_to_example'),
                    ('Country', 'country_example'),
                    ('Channel', openapi_server.VerificationAttemptEnumChannels()),
                    ('VerifyServiceSid', 'verify_service_sid_example'),
                    ('VerificationSid', 'verification_sid_example'),
                    ('Status', openapi_server.VerificationAttemptEnumConversionStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Attempts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

