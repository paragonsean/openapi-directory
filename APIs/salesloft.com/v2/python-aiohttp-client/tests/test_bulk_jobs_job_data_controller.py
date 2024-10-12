# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_job_result import BulkJobResult
from openapi_server.models.job_data_creation_result import JobDataCreationResult


pytestmark = pytest.mark.asyncio

async def test_v2_bulk_jobs_bulk_jobs_id_job_data_get(client):
    """Test case for v2_bulk_jobs_bulk_jobs_id_job_data_get

    List job data for a bulk job
    """
    params = [('status', ['status_example']),
                    ('id', None),
                    ('per_page', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/bulk_jobs/{bulk_jobs_id}/job_data'.format(bulk_jobs_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_bulk_jobs_bulk_jobs_id_job_data_post(client):
    """Test case for v2_bulk_jobs_bulk_jobs_id_job_data_post

    Create job data for a bulk job
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'data': ['data_example']
        }
    response = await client.request(
        method='POST',
        path='/v2/bulk_jobs/{bulk_jobs_id}/job_data'.format(bulk_jobs_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

