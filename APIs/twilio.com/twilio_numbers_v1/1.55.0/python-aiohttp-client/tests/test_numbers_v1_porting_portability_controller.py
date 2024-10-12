# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v1_porting_portability import NumbersV1PortingPortability


pytestmark = pytest.mark.asyncio

async def test_fetch_porting_portability(client):
    """Test case for fetch_porting_portability

    
    """
    params = [('TargetAccountSid', 'target_account_sid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Porting/Portability/PhoneNumber/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

