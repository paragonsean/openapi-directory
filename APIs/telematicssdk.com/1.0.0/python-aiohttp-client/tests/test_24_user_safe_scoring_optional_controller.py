# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_safe_scoring_accumulated_value_v1_scorings_individual200_response import UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response
from openapi_server.models.user_safe_scoring_daily_value_v1_scorings_individual_daily200_response import UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response


pytestmark = pytest.mark.asyncio

async def test_user_safe_scoring_accumulated_value_v1_scorings_individual_0(client):
    """Test case for user_safe_scoring_accumulated_value_v1_scorings_individual_0

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

async def test_user_safe_scoring_daily_value_v1_scorings_individual_daily_0(client):
    """Test case for user_safe_scoring_daily_value_v1_scorings_individual_daily_0

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

