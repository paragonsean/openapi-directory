# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server.models.queryjob import Queryjob
from openapi_server.models.queryjob_project_results import QueryjobProjectResults
from openapi_server.models.queryjob_results_overview import QueryjobResultsOverview


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_create_query_job(client):
    """Test case for create_query_job

    Run a CodeQL query on one or more projects
    """
    body = select "hello", "world"
    params = [('language', 'language_example'),
                    ('project-id', [56]),
                    ('projects-list', 'projects_list_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/queryjobs',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_job(client):
    """Test case for get_query_job

    Get the status of a query job
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/queryjobs/{queryjob_id}'.format(queryjob_id='queryjob_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_job_results_for_project(client):
    """Test case for get_query_job_results_for_project

    Fetch the results of a query job for a specific project
    """
    params = [('start', 56),
                    ('limit', 100),
                    ('nofilter', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/queryjobs/{queryjob_id}/results/{project_id}'.format(queryjob_id='queryjob_id_example', project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_job_results_overview(client):
    """Test case for get_query_job_results_overview

    Provide a summary of results for the projects in the query job
    """
    params = [('start', 'start_example'),
                    ('limit', 100),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/queryjobs/{queryjob_id}/results'.format(queryjob_id='queryjob_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

