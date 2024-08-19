# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_get_alerts(client):
    """Test case for get_alerts

    Get detailed alert information
    """
    params = [('sarif-version', 'sarif_version_example'),
                    ('excluded-files', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/analyses/{analysis_id}/alerts'.format(analysis_id='analysis_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analysis(client):
    """Test case for get_analysis

    Get analysis summary
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/analyses/{analysis_id}'.format(analysis_id='analysis_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analysis_for_commit(client):
    """Test case for get_analysis_for_commit

    Get analysis summary for a specific commit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/analyses/{project_id}/commits/{commit_id}'.format(project_id=56, commit_id='commit_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_analysis(client):
    """Test case for request_analysis

    Run analysis of a specific commit
    """
    params = [('commit', 'commit_example'),
                    ('language', ['language_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0/analyses/{project_id}'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

