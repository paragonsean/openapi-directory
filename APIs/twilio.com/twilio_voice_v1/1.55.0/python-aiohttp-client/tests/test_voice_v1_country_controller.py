# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_dialing_permissions_country_response import ListDialingPermissionsCountryResponse
from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_country_instance import VoiceV1DialingPermissionsDialingPermissionsCountryInstance


pytestmark = pytest.mark.asyncio

async def test_fetch_dialing_permissions_country(client):
    """Test case for fetch_dialing_permissions_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/DialingPermissions/Countries/{iso_code}'.format(iso_code='iso_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_dialing_permissions_country(client):
    """Test case for list_dialing_permissions_country

    
    """
    params = [('IsoCode', 'iso_code_example'),
                    ('Continent', 'continent_example'),
                    ('CountryCode', 'country_code_example'),
                    ('LowRiskNumbersEnabled', True),
                    ('HighRiskSpecialNumbersEnabled', True),
                    ('HighRiskTollfraudNumbersEnabled', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/DialingPermissions/Countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

