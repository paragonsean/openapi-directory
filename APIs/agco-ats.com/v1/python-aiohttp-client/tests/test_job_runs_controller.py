# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_job_run import APIPagedResponseBuildSystemSharedDTOJobRun
from openapi_server.models.build_system_shared_dto_job_run import BuildSystemSharedDTOJobRun


pytestmark = pytest.mark.asyncio

async def test_job_runs_delete_job_run(client):
    """Test case for job_runs_delete_job_run

    Delete a JobRun
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/jobRuns/{job_run_id}'.format(job_run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_runs_get_job_run(client):
    """Test case for job_runs_get_job_run

    Get a JobRun by ID
    """
    params = [('includeActivityRunDetails', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/jobRuns/{job_run_id}'.format(job_run_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_runs_get_job_runs(client):
    """Test case for job_runs_get_job_runs

    Get JobRuns
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('includeActivityRunDetails', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/jobRuns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_job_runs_post_job_run(client):
    """Test case for job_runs_post_job_run

    Create a JobRun
    """
    body = openapi_server.BuildSystemSharedDTOJobRun()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/jobRuns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_job_runs_put_job_run(client):
    """Test case for job_runs_put_job_run

    Update a JobRun
    """
    body = openapi_server.BuildSystemSharedDTOJobRun()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/jobRuns/{job_run_id}'.format(job_run_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

