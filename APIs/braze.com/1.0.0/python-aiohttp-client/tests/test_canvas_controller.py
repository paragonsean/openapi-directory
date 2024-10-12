# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_canvas_data_analytics_summary_0(client):
    """Test case for canvas_data_analytics_summary_0

    Canvas Data Analytics Summary
    """
    params = [('canvas_id', '{{canvas_id}}'),
                    ('ending_at', '2018-05-30T23:59:59-5:00'),
                    ('starting_at', '2018-05-28T23:59:59-5:00'),
                    ('length', '5'),
                    ('include_variant_breakdown', 'true'),
                    ('include_step_breakdown', 'true'),
                    ('include_deleted_step_data', 'true')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/data_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_data_series_analytics_0(client):
    """Test case for canvas_data_series_analytics_0

    Canvas Data Series Analytics
    """
    params = [('canvas_id', '{{canvas_id}}'),
                    ('ending_at', '2018-05-30T23:59:59-5:00'),
                    ('starting_at', '2018-05-28T23:59:59-5:00'),
                    ('length', '10'),
                    ('include_variant_breakdown', 'true'),
                    ('include_step_breakdown', 'true'),
                    ('include_deleted_step_data', 'true')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_details_0(client):
    """Test case for canvas_details_0

    Canvas Details
    """
    params = [('canvas_id', '{{canvas_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_canvas_list_0(client):
    """Test case for canvas_list_0

    Canvas List
    """
    params = [('page', '1'),
                    ('include_archived', 'false'),
                    ('sort_direction', 'desc'),
                    ('last_edit.time[gt]', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/canvas/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

