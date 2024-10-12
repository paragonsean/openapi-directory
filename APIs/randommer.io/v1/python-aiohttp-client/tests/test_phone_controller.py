# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_phone_countries_get(client):
    """Test case for api_phone_countries_get

    Get available countries
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Phone/Countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_phone_generate_get(client):
    """Test case for api_phone_generate_get

    Get bulk telephone numbers for a country
    """
    params = [('CountryCode', 'country_code_example'),
                    ('Quantity', 56)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Phone/Generate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_phone_imeiget(client):
    """Test case for api_phone_imeiget

    Get bulk imeis
    """
    params = [('Quantity', 56)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Phone/IMEI',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_phone_validate_get(client):
    """Test case for api_phone_validate_get

    Validate a phone number
    """
    params = [('telephone', 'telephone_example'),
                    ('CountryCode', 'country_code_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Phone/Validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

