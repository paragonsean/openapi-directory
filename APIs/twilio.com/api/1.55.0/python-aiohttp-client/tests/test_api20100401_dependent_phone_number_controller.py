# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_dependent_phone_number_response import ListDependentPhoneNumberResponse


pytestmark = pytest.mark.asyncio

async def test_list_dependent_phone_number(client):
    """Test case for list_dependent_phone_number

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json'.format(account_sid='account_sid_example', address_sid='address_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

