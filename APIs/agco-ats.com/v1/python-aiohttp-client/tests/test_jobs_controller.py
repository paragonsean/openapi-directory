# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_job import APIPagedResponseBuildSystemSharedDTOJob
from openapi_server.models.build_system_shared_dto_job import BuildSystemSharedDTOJob


pytestmark = pytest.mark.asyncio

async def test_jobs_delete_job(client):
    """Test case for jobs_delete_job

    Mark the delete flag for the Job
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/jobs/{job_id}'.format(job_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get_job(client):
    """Test case for jobs_get_job

    Get a Job by ID
    """
    params = [('isIncludeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/jobs/{job_id}'.format(job_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get_jobs(client):
    """Test case for jobs_get_jobs

    Get Jobs
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('isIncludeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_jobs_post_job(client):
    """Test case for jobs_post_job

    Create a Job
    """
    body = openapi_server.BuildSystemSharedDTOJob()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/jobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_jobs_put_job(client):
    """Test case for jobs_put_job

    Update a Job
    """
    body = openapi_server.BuildSystemSharedDTOJob()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/jobs/{job_id}'.format(job_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

