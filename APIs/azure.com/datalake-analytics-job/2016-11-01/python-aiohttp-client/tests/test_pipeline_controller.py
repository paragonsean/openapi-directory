# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_pipeline_information import JobPipelineInformation
from openapi_server.models.job_pipeline_information_list_result import JobPipelineInformationListResult


pytestmark = pytest.mark.asyncio

async def test_pipeline_get(client):
    """Test case for pipeline_get

    
    """
    params = [('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pipelines/{pipeline_identity}'.format(pipeline_identity='pipeline_identity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipeline_list(client):
    """Test case for pipeline_list

    
    """
    params = [('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pipelines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

