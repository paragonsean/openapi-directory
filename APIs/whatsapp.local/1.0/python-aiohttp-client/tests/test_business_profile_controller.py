# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_profile import BusinessProfile
from openapi_server.models.get_business_profile_response import GetBusinessProfileResponse


pytestmark = pytest.mark.asyncio

async def test_get_business_profile(client):
    """Test case for get_business_profile

    Get-Business-Profile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/business/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_business_profile(client):
    """Test case for update_business_profile

    Update-Business-Profile
    """
    body = {"address":"<Business Profile Address>","description":"<Business Profile Description>","email":"<Business Profile Email>","vertical":"<Business Profile Vertical>","websites":["https://www.whatsapp.com","https://www.facebook.com"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/settings/business/profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

