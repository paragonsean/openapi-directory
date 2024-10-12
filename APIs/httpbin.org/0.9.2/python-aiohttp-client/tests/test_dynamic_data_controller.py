# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_base64_value_get(client):
    """Test case for base64_value_get

    Decodes base64url-encoded string.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/base64/{value}'.format(value='SFRUUEJJTiBpcyBhd2Vzb21l'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bytes_nget(client):
    """Test case for bytes_nget

    Returns n random bytes generated with given seed
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/bytes/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_delete(client):
    """Test case for delay_delay_delete

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_get(client):
    """Test case for delay_delay_get

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_patch(client):
    """Test case for delay_delay_patch

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='PATCH',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_post(client):
    """Test case for delay_delay_post

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_put(client):
    """Test case for delay_delay_put

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delay_delay_trace(client):
    """Test case for delay_delay_trace

    Returns a delayed response (max of 10 seconds).
    """
    headers = { 
    }
    response = await client.request(
        method='TRACE',
        path='/delay/{delay}'.format(delay=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drip_get(client):
    """Test case for drip_get

    Drips data over a duration after an optional initial delay.
    """
    params = [('duration', 2),
                    ('numbytes', 10),
                    ('code', 200),
                    ('delay', 2)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/drip',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_links_n_offset_get(client):
    """Test case for links_n_offset_get

    Generate a page containing n links to other pages which do the same.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/links/{n}/{offset}'.format(n=56, offset=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_range_numbytes_get(client):
    """Test case for range_numbytes_get

    Streams n random bytes generated with given seed, at given chunk size per packet.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/range/{numbytes}'.format(numbytes=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_bytes_nget(client):
    """Test case for stream_bytes_nget

    Streams n random bytes generated with given seed, at given chunk size per packet.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stream-bytes/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_nget(client):
    """Test case for stream_nget

    Stream n JSON responses
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/stream/{n}'.format(n=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uuid_get(client):
    """Test case for uuid_get

    Return a UUID4.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/uuid',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

