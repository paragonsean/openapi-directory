# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_child(client):
    """Test case for get_child

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/child/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_generate_uuid(client):
    """Test case for get_generate_uuid

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/generate/uuid',
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

async def test_get_list_project(client):
    """Test case for get_list_project

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/list/project/{start}/{end}'.format(start=56, end=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_publisher(client):
    """Test case for get_list_publisher

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/list/publisher/{start}/{end}'.format(start=56, end=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lookup(client):
    """Test case for get_lookup

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/lookup/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespacefinduuid(client):
    """Test case for get_namespacefinduuid

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/namespace/finduuid/{namespace}/{namespaceid}'.format(namespace='namespace_example', namespaceid='namespaceid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespacegetall(client):
    """Test case for get_namespacegetall

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/namespace/getall',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespacegetid(client):
    """Test case for get_namespacegetid

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/namespace/getid/{namespace}'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_parent(client):
    """Test case for get_parent

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/parent/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relationships(client):
    """Test case for get_relationships

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/relationships/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_relationshipsexpanded(client):
    """Test case for get_relationshipsexpanded

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/relationships/expanded/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/search/{searchquery}'.format(searchquery='searchquery_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_propose(client):
    """Test case for post_propose

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/propose',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

