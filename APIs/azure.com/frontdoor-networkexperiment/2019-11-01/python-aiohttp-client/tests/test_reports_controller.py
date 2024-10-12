# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.latency_scorecard import LatencyScorecard
from openapi_server.models.timeseries import Timeseries


pytestmark = pytest.mark.asyncio

async def test_reports_get_latency_scorecards(client):
    """Test case for reports_get_latency_scorecards

    Gets a Latency Scorecard for a given Experiment
    """
    params = [('api-version', 'api_version_example'),
                    ('endDateTimeUTC', 'end_date_time_utc_example'),
                    ('country', 'country_example'),
                    ('aggregationInterval', 'aggregation_interval_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}/LatencyScorecard'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_get_timeseries(client):
    """Test case for reports_get_timeseries

    Gets a Timeseries for a given Experiment
    """
    params = [('api-version', 'api_version_example'),
                    ('startDateTimeUTC', '2013-10-20T19:20:30+01:00'),
                    ('endDateTimeUTC', '2013-10-20T19:20:30+01:00'),
                    ('aggregationInterval', 'aggregation_interval_example'),
                    ('timeseriesType', 'timeseries_type_example'),
                    ('endpoint', 'endpoint_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}/Timeseries'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

