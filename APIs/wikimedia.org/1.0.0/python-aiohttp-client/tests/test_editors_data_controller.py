# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.editors import Editors
from openapi_server.models.problem import Problem
from openapi_server.models.top_editors_by_abs_bytes_diff import TopEditorsByAbsBytesDiff
from openapi_server.models.top_editors_by_edits import TopEditorsByEdits
from openapi_server.models.top_editors_by_net_bytes_diff import TopEditorsByNetBytesDiff


pytestmark = pytest.mark.asyncio

async def test_metrics_editors_aggregate_project_editor_type_page_type_activity_level_granularity_start_end_get(client):
    """Test case for metrics_editors_aggregate_project_editor_type_page_type_activity_level_granularity_start_end_get

    Get editors counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/editors/aggregate/{project}/{editor_type}/{page_type}/{activity_level}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', activity_level='activity_level_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_editors_top_by_absolute_bytes_difference_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_editors_top_by_absolute_bytes_difference_project_editor_type_page_type_year_month_day_get

    Get top 100 editors by absolute bytes-difference.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/editors/top-by-absolute-bytes-difference/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_editors_top_by_edits_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_editors_top_by_edits_project_editor_type_page_type_year_month_day_get

    Get top 100 editors by edits count.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/editors/top-by-edits/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_editors_top_by_net_bytes_difference_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_editors_top_by_net_bytes_difference_project_editor_type_page_type_year_month_day_get

    Get top 100 editors by net bytes-difference.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/editors/top-by-net-bytes-difference/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

