# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.blend_response import BlendResponse
from openapi_server.models.button_response import ButtonResponse
from openapi_server.models.button_response_error_upscaled import ButtonResponseErrorUpscaled
from openapi_server.models.describe_response import DescribeResponse
from openapi_server.models.imagine_response import ImagineResponse
from openapi_server.models.imagine_response_moderated import ImagineResponseModerated
from openapi_server.models.job_cancel_response import JobCancelResponse
from openapi_server.models.job_response import JobResponse
from openapi_server.models.jobs_blend_post_request import JobsBlendPostRequest
from openapi_server.models.jobs_button_post_request import JobsButtonPostRequest
from openapi_server.models.jobs_describe_post_request import JobsDescribePostRequest
from openapi_server.models.jobs_imagine_post_request import JobsImaginePostRequest
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_max_jobs import ResponseMaxJobs


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_blend_post(client):
    """Test case for jobs_blend_post

    
    """
    body = openapi_server.JobsBlendPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/blend',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_button_post(client):
    """Test case for jobs_button_post

    
    """
    body = openapi_server.JobsButtonPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/button',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_cancel_get(client):
    """Test case for jobs_cancel_get

    
    """
    params = [('jobid', 'jobid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/cancel/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_describe_post(client):
    """Test case for jobs_describe_post

    
    """
    body = openapi_server.JobsDescribePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/describe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get_0(client):
    """Test case for jobs_get_0

    
    """
    params = [('jobid', 'jobid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/jobs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_imagine_post(client):
    """Test case for jobs_imagine_post

    
    """
    body = openapi_server.JobsImaginePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/jobs/imagine',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

