# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attempt_normalization_status_read_list import AttemptNormalizationStatusReadList
from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.job_debug_info_read import JobDebugInfoRead
from openapi_server.models.job_id_request_body import JobIdRequestBody
from openapi_server.models.job_info_light_read import JobInfoLightRead
from openapi_server.models.job_info_read import JobInfoRead
from openapi_server.models.job_list_request_body import JobListRequestBody
from openapi_server.models.job_optional_read import JobOptionalRead
from openapi_server.models.job_read_list import JobReadList
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo


pytestmark = pytest.mark.asyncio

async def test_cancel_job(client):
    """Test case for cancel_job

    Cancels a job
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attempt_normalization_statuses_for_job(client):
    """Test case for get_attempt_normalization_statuses_for_job

    Get normalization status to determine if we can bypass normalization phase
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get_normalization_status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_debug_info(client):
    """Test case for get_job_debug_info

    Gets all information needed to debug this job
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get_debug_info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_info(client):
    """Test case for get_job_info

    Get information about a job
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_info_light(client):
    """Test case for get_job_info_light

    Get information about a job excluding attempt info and logs
    """
    body = {"id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get_light',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_replication_job(client):
    """Test case for get_last_replication_job

    
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/get_last_replication_job',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_jobs_for(client):
    """Test case for list_jobs_for

    Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.
    """
    body = {"includingJobId":0,"pagination":{"rowOffset":1,"pageSize":6},"configTypes":["check_connection_source","check_connection_source"],"configId":"configId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

