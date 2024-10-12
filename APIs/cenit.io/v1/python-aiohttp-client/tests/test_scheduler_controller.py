# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.scheduler import Scheduler


pytestmark = pytest.mark.asyncio

async def test_setup_scheduler_get(client):
    """Test case for setup_scheduler_get

    Returns a list of schedulers
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/scheduler/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_scheduler_id_delete(client):
    """Test case for setup_scheduler_id_delete

    Delete an schedule
    """
    headers = { 
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/setup/scheduler/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_scheduler_id_get(client):
    """Test case for setup_scheduler_id_get

    Retrieve an existing schedule
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/scheduler/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_scheduler_post(client):
    """Test case for setup_scheduler_post

    Create or update an scheduler
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/setup/scheduler/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

