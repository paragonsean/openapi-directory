# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_job import BulkJob


pytestmark = pytest.mark.asyncio

async def test_v2_bulk_jobs_get(client):
    """Test case for v2_bulk_jobs_get

    List bulk jobs
    """
    params = [('state', ['state_example']),
                    ('id', None),
                    ('per_page', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/bulk_jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_bulk_jobs_id_get(client):
    """Test case for v2_bulk_jobs_id_get

    Fetch a bulk job
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/bulk_jobs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_bulk_jobs_id_put(client):
    """Test case for v2_bulk_jobs_id_put

    Update a bulk job
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'name': 'name_example',
        'ready_to_execute': True
        }
    response = await client.request(
        method='PUT',
        path='/v2/bulk_jobs/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_bulk_jobs_post(client):
    """Test case for v2_bulk_jobs_post

    Create a bulk job
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'name': 'name_example',
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/bulk_jobs',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

