# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_available_phone_number_country import ApiV2010AccountAvailablePhoneNumberCountry
from openapi_server.models.list_available_phone_number_country_response import ListAvailablePhoneNumberCountryResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_available_phone_number_country(client):
    """Test case for fetch_available_phone_number_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code_jso}'.format(account_sid='account_sid_example', country_code='country_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_available_phone_number_country(client):
    """Test case for list_available_phone_number_country

    
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
        path='/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

