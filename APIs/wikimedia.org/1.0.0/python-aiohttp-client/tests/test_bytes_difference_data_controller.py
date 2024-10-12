# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.absolute_bytes_difference import AbsoluteBytesDifference
from openapi_server.models.absolute_bytes_difference_per_page import AbsoluteBytesDifferencePerPage
from openapi_server.models.net_bytes_difference import NetBytesDifference
from openapi_server.models.net_bytes_difference_per_page import NetBytesDifferencePerPage
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_metrics_bytes_difference_absolute_aggregate_project_editor_type_page_type_granularity_start_end_get(client):
    """Test case for metrics_bytes_difference_absolute_aggregate_project_editor_type_page_type_granularity_start_end_get

    Get the sum of absolute value of text bytes difference between current edit and previous one. 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/bytes-difference/absolute/aggregate/{project}/{editor_type}/{page_type}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_bytes_difference_absolute_per_page_project_page_title_editor_type_granularity_start_end_get(client):
    """Test case for metrics_bytes_difference_absolute_per_page_project_page_title_editor_type_granularity_start_end_get

    Get the sum of absolute text bytes difference per page.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/bytes-difference/absolute/per-page/{project}/{page_title}/{editor_type}/{granularity}/{start}/{end}'.format(project='project_example', page_title='page_title_example', editor_type='editor_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_bytes_difference_net_aggregate_project_editor_type_page_type_granularity_start_end_get(client):
    """Test case for metrics_bytes_difference_net_aggregate_project_editor_type_page_type_granularity_start_end_get

    Get the sum of net text bytes difference between current edit and previous one.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/bytes-difference/net/aggregate/{project}/{editor_type}/{page_type}/{granularity}/{start}/{end}'.format(project='project_example', editor_type='editor_type_example', page_type='page_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_bytes_difference_net_per_page_project_page_title_editor_type_granularity_start_end_get(client):
    """Test case for metrics_bytes_difference_net_per_page_project_page_title_editor_type_granularity_start_end_get

    Get the sum of net text bytes difference per page.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/bytes-difference/net/per-page/{project}/{page_title}/{editor_type}/{granularity}/{start}/{end}'.format(project='project_example', page_title='page_title_example', editor_type='editor_type_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

