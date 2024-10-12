# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_health_get(client):
    """Test case for health_get

    Get HTTP
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_anti_virus(client):
    """Test case for health_get_anti_virus

    Get Anti virus
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/anti-virus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_cache(client):
    """Test case for health_get_cache

    Get Cache
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/cache',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_db(client):
    """Test case for health_get_db

    Get DB
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/db',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_certificates(client):
    """Test case for health_get_queue_certificates

    Get Certificate Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/certificates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_functions(client):
    """Test case for health_get_queue_functions

    Get Functions Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/functions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_logs(client):
    """Test case for health_get_queue_logs

    Get Logs Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/logs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_tasks(client):
    """Test case for health_get_queue_tasks

    Get Tasks Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/tasks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_usage(client):
    """Test case for health_get_queue_usage

    Get Usage Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_queue_webhooks(client):
    """Test case for health_get_queue_webhooks

    Get Webhooks Queue
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/queue/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_storage_local(client):
    """Test case for health_get_storage_local

    Get Local Storage
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/storage/local',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_get_time(client):
    """Test case for health_get_time

    Get Time
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/health/time',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

