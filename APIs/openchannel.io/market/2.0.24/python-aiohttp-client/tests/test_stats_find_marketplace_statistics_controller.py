# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.total import Total


pytestmark = pytest.mark.asyncio

async def test_stats_increment_field_post(client):
    """Test case for stats_increment_field_post

    Increments a statistics field
    """
    params = [('appId', 'app_id_example'),
                    ('userId', 'user_id_example'),
                    ('value', 56),
                    ('date', 56)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/stats/increment/{_field}'.format(_field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stats_series_period_fields_get(client):
    """Test case for stats_series_period_fields_get

    Return a timeseries for a particular field
    """
    params = [('start', 56),
                    ('end', 56),
                    ('query', 'query_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/stats/series/{period}/{fields}'.format(period='period_example', fields='fields_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stats_total_get(client):
    """Test case for stats_total_get

    Returns the total number of events for a particular field.
    """
    params = [('fields', 'fields_example'),
                    ('query', 'query_example'),
                    ('start', 56),
                    ('end', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/stats/total',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

