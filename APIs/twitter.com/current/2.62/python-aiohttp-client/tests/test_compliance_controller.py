# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_compliance_job_request import CreateComplianceJobRequest
from openapi_server.models.create_compliance_job_response import CreateComplianceJobResponse
from openapi_server.models.error import Error
from openapi_server.models.get2_compliance_jobs_id_response import Get2ComplianceJobsIdResponse
from openapi_server.models.get2_compliance_jobs_response import Get2ComplianceJobsResponse
from openapi_server.models.problem import Problem
from openapi_server.models.tweet_compliance_stream_response import TweetComplianceStreamResponse
from openapi_server.models.tweet_label_stream_response import TweetLabelStreamResponse
from openapi_server.models.user_compliance_stream_response import UserComplianceStreamResponse


pytestmark = pytest.mark.asyncio

async def test_create_batch_compliance_job(client):
    """Test case for create_batch_compliance_job

    Create compliance job
    """
    body = {"resumable":True,"name":"my-job","type":"tweets"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/2/compliance/jobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_compliance_job(client):
    """Test case for get_batch_compliance_job

    Get Compliance Job
    """
    params = [('compliance_job.fields', ['[\"created_at\",\"download_expires_at\",\"download_url\",\"id\",\"name\",\"resumable\",\"status\",\"type\",\"upload_expires_at\",\"upload_url\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/compliance/jobs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tweets_compliance_stream(client):
    """Test case for get_tweets_compliance_stream

    Tweets Compliance stream
    """
    params = [('backfill_minutes', 56),
                    ('partition', 56),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/compliance/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tweets_label_stream(client):
    """Test case for get_tweets_label_stream

    Tweets Label stream
    """
    params = [('backfill_minutes', 56),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-01T18:40:40.000Z')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/label/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_compliance_stream(client):
    """Test case for get_users_compliance_stream

    Users Compliance stream
    """
    params = [('backfill_minutes', 56),
                    ('partition', 56),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-01T18:40:40.000Z')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/users/compliance/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_batch_compliance_jobs(client):
    """Test case for list_batch_compliance_jobs

    List Compliance Jobs
    """
    params = [('type', 'type_example'),
                    ('status', 'status_example'),
                    ('compliance_job.fields', ['[\"created_at\",\"download_expires_at\",\"download_url\",\"id\",\"name\",\"resumable\",\"status\",\"type\",\"upload_expires_at\",\"upload_url\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/compliance/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

