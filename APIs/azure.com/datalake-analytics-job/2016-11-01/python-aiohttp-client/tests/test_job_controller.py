# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_job_parameters import BuildJobParameters
from openapi_server.models.create_job_parameters import CreateJobParameters
from openapi_server.models.job_data_path import JobDataPath
from openapi_server.models.job_info_list_result import JobInfoListResult
from openapi_server.models.job_information import JobInformation
from openapi_server.models.job_statistics import JobStatistics


pytestmark = pytest.mark.asyncio

async def test_job_build(client):
    """Test case for job_build

    
    """
    parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/BuildJob',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_cancel(client):
    """Test case for job_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/Jobs/{job_identity}/CancelJob'.format(job_identity='job_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_create(client):
    """Test case for job_create

    
    """
    parameters = {"degreeOfParallelismPercent":6.027456183070403,"related":{"pipelineName":"pipelineName","recurrenceName":"recurrenceName","pipelineUri":"pipelineUri","runId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","recurrenceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pipelineId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"name":"name","priority":1,"degreeOfParallelism":0,"logFilePatterns":["logFilePatterns","logFilePatterns"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Jobs/{job_identity}'.format(job_identity='job_identity_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/{job_identity}'.format(job_identity='job_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_debug_data_path(client):
    """Test case for job_get_debug_data_path

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/{job_identity}/GetDebugDataPath'.format(job_identity='job_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_statistics(client):
    """Test case for job_get_statistics

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/{job_identity}/GetStatistics'.format(job_identity='job_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list(client):
    """Test case for job_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('$select', 'select_example'),
                    ('$orderby', 'orderby_example'),
                    ('$count', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

