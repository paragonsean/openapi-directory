# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verification_attempts_summary_enum_channels import VerificationAttemptsSummaryEnumChannels
from openapi_server.models.verify_v2_verification_attempts_summary import VerifyV2VerificationAttemptsSummary


pytestmark = pytest.mark.asyncio

async def test_fetch_verification_attempts_summary(client):
    """Test case for fetch_verification_attempts_summary

    
    """
    params = [('VerifyServiceSid', 'verify_service_sid_example'),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('Country', 'country_example'),
                    ('Channel', openapi_server.VerificationAttemptsSummaryEnumChannels()),
                    ('DestinationPrefix', 'destination_prefix_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Attempts/Summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

