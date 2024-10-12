# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_finance_countries_get(client):
    """Test case for api_finance_countries_get

    Get available countries
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Finance/Countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_finance_crypto_address_get(client):
    """Test case for api_finance_crypto_address_get

    Get crypto address
    """
    params = [('cryptoType', 'crypto_type_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Finance/CryptoAddress',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_finance_crypto_address_types_get(client):
    """Test case for api_finance_crypto_address_types_get

    Get available crypto types
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Finance/CryptoAddress/Types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_finance_iban_country_code_get(client):
    """Test case for api_finance_iban_country_code_get

    Get IBAN by countryCode
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Finance/Iban/{country_code}'.format(country_code='country_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_finance_vat_validator_post(client):
    """Test case for api_finance_vat_validator_post

    
    """
    params = [('country', 'country_example'),
                    ('vat', 'vat_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Finance/Vat/Validator',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

