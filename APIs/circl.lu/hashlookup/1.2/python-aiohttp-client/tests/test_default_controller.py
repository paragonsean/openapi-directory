# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_children(client):
    """Test case for get_children

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/children/{sha1}/{count}/{cursor}'.format(sha1='sha1_example', count=56, cursor='cursor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lookup_md5(client):
    """Test case for get_lookup_md5

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/lookup/md5/{md5}'.format(md5='md5_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lookup_sha1(client):
    """Test case for get_lookup_sha1

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/lookup/sha1/{sha1}'.format(sha1='sha1_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lookup_sha256(client):
    """Test case for get_lookup_sha256

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/lookup/sha256/{sha256}'.format(sha256='sha256_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_parents(client):
    """Test case for get_parents

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/parents/{sha1}/{count}/{cursor}'.format(sha1='sha1_example', count=56, cursor='cursor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_create(client):
    """Test case for get_session_create

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/session/create/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_matches(client):
    """Test case for get_session_matches

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/session/get/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stattop(client):
    """Test case for get_stattop

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stats/top',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_bulkmd5(client):
    """Test case for post_bulkmd5

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/bulk/md5',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_bulksha1(client):
    """Test case for post_bulksha1

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/bulk/sha1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

