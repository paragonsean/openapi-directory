# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edits import Edits
from openapi_server.models.edits_per_page import EditsPerPage
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_metrics_edits_aggregate_project_editor_type_page_type_granularity_start_end_get(client):
    """Test case for metrics_edits_aggregate_project_editor_type_page_type_granularity_start_end_get

    Get edits counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edits/aggregate/{project}/{editor_type}/{page_type}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_edits_per_page_project_page_title_editor_type_granularity_start_end_get(client):
    """Test case for metrics_edits_per_page_project_page_title_editor_type_granularity_start_end_get

    Get edit counts for a page in a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edits/per-page/{project}/{page_title}/{editor_type}/{granularity}/{start}/{end}'.format(project='project_example', page_title='page_title_example', editor_type='editor_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

