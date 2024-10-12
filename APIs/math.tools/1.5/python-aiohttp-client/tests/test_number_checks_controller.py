# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_numbers_is_cube_get(client):
    """Test case for numbers_is_cube_get

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/is-cube',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_is_palindrome_get(client):
    """Test case for numbers_is_palindrome_get

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/is-palindrome',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_is_square_get(client):
    """Test case for numbers_is_square_get

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/is-square',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_is_triangle_get(client):
    """Test case for numbers_is_triangle_get

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/is-triangle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_fermat_prime_get_0(client):
    """Test case for numbers_prime_is_fermat_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-fermat-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_fibonacci_prime_get_0(client):
    """Test case for numbers_prime_is_fibonacci_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-fibonacci-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_mersenne_prime_get_0(client):
    """Test case for numbers_prime_is_mersenne_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-mersenne-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_partition_prime_get_0(client):
    """Test case for numbers_prime_is_partition_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-partition-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_pell_prime_get_0(client):
    """Test case for numbers_prime_is_pell_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-pell-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_perfect_get_0(client):
    """Test case for numbers_prime_is_perfect_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-perfect',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_numbers_prime_is_prime_get_0(client):
    """Test case for numbers_prime_is_prime_get_0

    
    """
    params = [('number', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/prime/is-prime',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

