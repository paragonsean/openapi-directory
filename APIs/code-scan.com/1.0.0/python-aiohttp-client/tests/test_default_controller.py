# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.job import Job
from openapi_server.models.new_job import NewJob


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    Get the status of a job
    """
    params = [('jobId', 'job_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/job',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_post(client):
    """Test case for job_post

    Queues a job
    """
    job = {"projectBranch":"projectBranch","projectKey":"projectKey","analysisMode":"analysisMode","commitOverride":"commitOverride","emailReportTo":"emailReportTo","version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/job',
        headers=headers,
        json=job,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

