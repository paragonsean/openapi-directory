# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lookups_v1_phone_number import LookupsV1PhoneNumber


pytestmark = pytest.mark.asyncio

async def test_fetch_phone_number(client):
    """Test case for fetch_phone_number

    
    """
    params = [('CountryCode', 'country_code_example'),
                    ('Type', ['type_example']),
                    ('AddOns', ['add_ons_example']),
                    ('AddOnsData', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/PhoneNumbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

