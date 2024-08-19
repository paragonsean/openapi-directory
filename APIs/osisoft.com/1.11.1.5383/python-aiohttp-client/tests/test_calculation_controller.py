# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_summary_value import ItemsSummaryValue
from openapi_server.models.timed_values import TimedValues


pytestmark = pytest.mark.asyncio

async def test_calculation_get_at_intervals(client):
    """Test case for calculation_get_at_intervals

    Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.
    """
    params = [('expression', 'expression_example'),
                    ('endTime', 'end_time_example'),
                    ('sampleInterval', 'sample_interval_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('webId', 'web_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/calculation/intervals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculation_get_at_recorded(client):
    """Test case for calculation_get_at_recorded

    Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.
    """
    params = [('expression', 'expression_example'),
                    ('endTime', 'end_time_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('webId', 'web_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/calculation/recorded',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculation_get_at_times(client):
    """Test case for calculation_get_at_times

    Returns the result of evaluating the expression at the specified timestamps.
    """
    params = [('expression', 'expression_example'),
                    ('time', ['time_example']),
                    ('selectedFields', 'selected_fields_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('webId', 'web_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/calculation/times',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculation_get_summary(client):
    """Test case for calculation_get_summary

    Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.
    """
    params = [('expression', 'expression_example'),
                    ('calculationBasis', 'calculation_basis_example'),
                    ('endTime', 'end_time_example'),
                    ('sampleInterval', 'sample_interval_example'),
                    ('sampleType', 'sample_type_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startTime', 'start_time_example'),
                    ('summaryDuration', 'summary_duration_example'),
                    ('summaryType', ['summary_type_example']),
                    ('timeType', 'time_type_example'),
                    ('webId', 'web_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/calculation/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

