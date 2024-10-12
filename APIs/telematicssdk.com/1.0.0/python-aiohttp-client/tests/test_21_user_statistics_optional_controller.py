# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_statistice_daily_value_v1_statistics_individual_daily200_response import UserStatisticeDailyValueV1StatisticsIndividualDaily200Response
from openapi_server.models.user_statistics_accumulated_value_v1_statistics_individual200_response import UserStatisticsAccumulatedValueV1StatisticsIndividual200Response


pytestmark = pytest.mark.asyncio

async def test_user_statistice_daily_value_v1_statistics_individual_daily_0(client):
    """Test case for user_statistice_daily_value_v1_statistics_individual_daily_0

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

async def test_user_statistics_accumulated_value_v1_statistics_individual_0(client):
    """Test case for user_statistics_accumulated_value_v1_statistics_individual_0

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

