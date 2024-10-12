# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_available_phone_number_national_response import ListAvailablePhoneNumberNationalResponse


pytestmark = pytest.mark.asyncio

async def test_list_available_phone_number_national(client):
    """Test case for list_available_phone_number_national

    
    """
    params = [('AreaCode', 56),
                    ('Contains', 'contains_example'),
                    ('SmsEnabled', True),
                    ('MmsEnabled', True),
                    ('VoiceEnabled', True),
                    ('ExcludeAllAddressRequired', True),
                    ('ExcludeLocalAddressRequired', True),
                    ('ExcludeForeignAddressRequired', True),
                    ('Beta', True),
                    ('NearNumber', 'near_number_example'),
                    ('NearLatLong', 'near_lat_long_example'),
                    ('Distance', 56),
                    ('InPostalCode', 'in_postal_code_example'),
                    ('InRegion', 'in_region_example'),
                    ('InRateCenter', 'in_rate_center_example'),
                    ('InLata', 'in_lata_example'),
                    ('InLocality', 'in_locality_example'),
                    ('FaxEnabled', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/National.json'.format(account_sid='account_sid_example', country_code='country_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

