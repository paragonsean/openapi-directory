# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.application_summary import ApplicationSummary
from openapi_server.models.batch_error import BatchError


pytestmark = pytest.mark.asyncio

async def test_application_get(client):
    """Test case for application_get

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/applications/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_list(client):
    """Test case for application_list

    
    """
    params = [('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

