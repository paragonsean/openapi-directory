# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.find_seller_standards_profiles_response import FindSellerStandardsProfilesResponse
from openapi_server.models.standards_profile import StandardsProfile


pytestmark = pytest.mark.asyncio

async def test_find_seller_standards_profiles(client):
    """Test case for find_seller_standards_profiles

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/analytics/v1/seller_standards_profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_seller_standards_profile(client):
    """Test case for get_seller_standards_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/analytics/v1/seller_standards_profile/{program}/{cycle}'.format(cycle='cycle_example', program='program_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

