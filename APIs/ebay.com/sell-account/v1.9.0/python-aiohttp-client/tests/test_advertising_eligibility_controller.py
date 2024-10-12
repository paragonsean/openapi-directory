# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.seller_eligibility_multi_program_response import SellerEligibilityMultiProgramResponse


pytestmark = pytest.mark.asyncio

async def test_get_advertising_eligibility(client):
    """Test case for get_advertising_eligibility

    
    """
    params = [('program_types', 'program_types_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/advertising_eligibility',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

