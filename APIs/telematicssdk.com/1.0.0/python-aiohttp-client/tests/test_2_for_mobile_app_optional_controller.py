# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trips_trip_details200_response import TripsTripDetails200Response
from openapi_server.models.user_safe_scoring_accumulated_value_v1_scorings_individual200_response import UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
from openapi_server.models.user_safe_scoring_daily_value_v1_scorings_individual_daily200_response import UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response
from openapi_server.models.user_statistice_daily_value_v1_statistics_individual_daily200_response import UserStatisticeDailyValueV1StatisticsIndividualDaily200Response
from openapi_server.models.user_statistics_accumulated_value_v1_statistics_individual200_response import UserStatisticsAccumulatedValueV1StatisticsIndividual200Response


pytestmark = pytest.mark.asyncio

async def test_trips_trip_details(client):
    """Test case for trips_trip_details

    Trips - trip details
    """
    params = [('trackToken', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/mobilesdk/stage/track/get_track/v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_safe_scoring_accumulated_value_v1_scorings_individual(client):
    """Test case for user_safe_scoring_accumulated_value_v1_scorings_individual

    User safe scoring - Accumulated value - v1/Scorings/individual
    """
    params = [('startDate', '2021-01-01'),
                    ('endDate', '2021-01-30')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Scorings/individual/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_safe_scoring_daily_value_v1_scorings_individual_daily(client):
    """Test case for user_safe_scoring_daily_value_v1_scorings_individual_daily

    User safe scoring - daily value - /v1/Scorings/individual/daily
    """
    params = [('Tag', ''),
                    ('StartDate', '2021-01-01'),
                    ('EndDate', '2021-01-20')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Scorings/individual/daily',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_statistice_daily_value_v1_statistics_individual_daily(client):
    """Test case for user_statistice_daily_value_v1_statistics_individual_daily

    User statistice - Daily value - v1/Statistics/individual/daily
    """
    params = [('startDate', '2021-03-30'),
                    ('endDate', '2021-03-30')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Statistics/individual/daily/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_statistics_accumulated_value_v1_statistics_individual(client):
    """Test case for user_statistics_accumulated_value_v1_statistics_individual

    User statistics - Accumulated value - /v1/Statistics/individual
    """
    params = [('startDate', '2021-01-01'),
                    ('endDate', '2021-01-30')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics/v1/Statistics/individual/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

