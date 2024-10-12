# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_get_0(client):
    """Test case for logs_app_id_drains_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_id_or_url_delete_0(client):
    """Test case for logs_app_id_drains_id_or_url_delete_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_id_or_url_get_0(client):
    """Test case for logs_app_id_drains_id_or_url_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_drains_post_0(client):
    """Test case for logs_app_id_drains_post_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_get_0(client):
    """Test case for logs_app_id_get_0

    
    """
    params = [('limit', 56),
                    ('order', desc),
                    ('after', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('filter', 'filter_example'),
                    ('deployment_id', 'deployment_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_app_id_sse_get_0(client):
    """Test case for logs_app_id_sse_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{app_id}/sse'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_drains_drain_id_put_0(client):
    """Test case for logs_drains_drain_id_put_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/logs/drains/{drain_id}'.format(drain_id='drain_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_drains_get_0(client):
    """Test case for logs_drains_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/drains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_logs_chunked_app_id_get_0(client):
    """Test case for logs_logs_chunked_app_id_get_0

    
    """
    params = [('download', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/logs-chunked/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_logs_socket_app_id_get_0(client):
    """Test case for logs_logs_socket_app_id_get_0

    
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('filter', 'filter_example'),
                    ('deployment_id', 'deployment_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/logs-socket/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_get_0(client):
    """Test case for v3_logs_app_id_drains_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_id_or_url_delete_0(client):
    """Test case for v3_logs_app_id_drains_id_or_url_delete_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/v3/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_id_or_url_get_0(client):
    """Test case for v3_logs_app_id_drains_id_or_url_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/drains/:idOrUrl'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_drains_post_0(client):
    """Test case for v3_logs_app_id_drains_post_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/v3/logs/{app_id}/drains'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_get_0(client):
    """Test case for v3_logs_app_id_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_logs_chunked_get_0(client):
    """Test case for v3_logs_app_id_logs_chunked_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/logs-chunked'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_logs_app_id_logs_socket_get_0(client):
    """Test case for v3_logs_app_id_logs_socket_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/v3/logs/{app_id}/logs-socket'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

