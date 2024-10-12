# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lookups_v2_phone_number import LookupsV2PhoneNumber


pytestmark = pytest.mark.asyncio

async def test_fetch_phone_number(client):
    """Test case for fetch_phone_number

    
    """
    params = [('Fields', 'fields_example'),
                    ('CountryCode', 'country_code_example'),
                    ('FirstName', 'first_name_example'),
                    ('LastName', 'last_name_example'),
                    ('AddressLine1', 'address_line1_example'),
                    ('AddressLine2', 'address_line2_example'),
                    ('City', 'city_example'),
                    ('State', 'state_example'),
                    ('PostalCode', 'postal_code_example'),
                    ('AddressCountryCode', 'address_country_code_example'),
                    ('NationalId', 'national_id_example'),
                    ('DateOfBirth', 'date_of_birth_example'),
                    ('LastVerifiedDate', 'last_verified_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/PhoneNumbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

