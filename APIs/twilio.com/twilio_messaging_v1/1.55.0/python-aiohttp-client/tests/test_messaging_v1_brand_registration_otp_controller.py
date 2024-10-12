# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.messaging_v1_brand_registrations_brand_registration_otp import MessagingV1BrandRegistrationsBrandRegistrationOtp


pytestmark = pytest.mark.asyncio

async def test_create_brand_registration_otp(client):
    """Test case for create_brand_registration_otp

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/a2p/BrandRegistrations/{brand_registration_sid}/SmsOtp'.format(brand_registration_sid='brand_registration_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

