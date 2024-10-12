# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edited_pages import EditedPages
from openapi_server.models.new_pages import NewPages
from openapi_server.models.problem import Problem
from openapi_server.models.top_edited_pages_by_abs_bytes_diff import TopEditedPagesByAbsBytesDiff
from openapi_server.models.top_edited_pages_by_edits import TopEditedPagesByEdits
from openapi_server.models.top_edited_pages_by_net_bytes_diff import TopEditedPagesByNetBytesDiff


pytestmark = pytest.mark.asyncio

async def test_metrics_edited_pages_aggregate_project_editor_type_page_type_activity_level_granularity_start_end_get(client):
    """Test case for metrics_edited_pages_aggregate_project_editor_type_page_type_activity_level_granularity_start_end_get

    Get edited-pages counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edited-pages/aggregate/{project}/{editor_type}/{page_type}/{activity_level}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', activity_level='activity_level_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_edited_pages_new_project_editor_type_page_type_granularity_start_end_get(client):
    """Test case for metrics_edited_pages_new_project_editor_type_page_type_granularity_start_end_get

    Get new pages counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edited-pages/new/{project}/{editor_type}/{page_type}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_edited_pages_top_by_absolute_bytes_difference_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_edited_pages_top_by_absolute_bytes_difference_project_editor_type_page_type_year_month_day_get

    Get top 100 edited-pages by absolute bytes-difference.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edited-pages/top-by-absolute-bytes-difference/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_edited_pages_top_by_edits_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_edited_pages_top_by_edits_project_editor_type_page_type_year_month_day_get

    Get top 100 edited-pages by edits count.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edited-pages/top-by-edits/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_edited_pages_top_by_net_bytes_difference_project_editor_type_page_type_year_month_day_get(client):
    """Test case for metrics_edited_pages_top_by_net_bytes_difference_project_editor_type_page_type_year_month_day_get

    Get top 100 edited-pages by net bytes-difference.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/edited-pages/top-by-net-bytes-difference/{project}/{editor_type}/{page_type}/{year}/{month}/{day}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

