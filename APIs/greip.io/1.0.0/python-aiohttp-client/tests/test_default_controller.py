# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_a_sn_lookup_get(client):
    """Test case for a_sn_lookup_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('asn', '15169'),
                    ('isList', 'false'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/ASNLookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_b_in_lookup_get(client):
    """Test case for b_in_lookup_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('bin', '489022'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BINLookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bad_words_get(client):
    """Test case for bad_words_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('text', 'This is a sample text without profanity!'),
                    ('listBadWords', 'false'),
                    ('scoreOnly', 'false'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/badWords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_lookup_get(client):
    """Test case for bulk_lookup_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('ips', '1.1.1.1'),
                    ('params', 'currency'),
                    ('lang', 'AR'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BulkLookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_country_get(client):
    """Test case for country_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('CountryCode', 'PS'),
                    ('params', 'language'),
                    ('lang', 'AR'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/Country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geo_ipget(client):
    """Test case for geo_ipget

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('params', 'currency'),
                    ('lang', 'AR'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/GeoIP',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_i_p_lookup_get(client):
    """Test case for i_p_lookup_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('ip', '1.1.1.1'),
                    ('params', 'currency'),
                    ('lang', 'AR'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/IPLookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_email_get(client):
    """Test case for validate_email_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('email', 'name@domain.com'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/validateEmail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_phone_get(client):
    """Test case for validate_phone_get

    
    """
    params = [('key', '2517bc4fc3f790e8f09bc808bb63b899'),
                    ('phone', '1234567890'),
                    ('countryCode', 'US'),
                    ('format', 'JSON')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/validatePhone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

