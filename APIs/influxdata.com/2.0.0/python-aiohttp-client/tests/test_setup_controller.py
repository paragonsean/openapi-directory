# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.is_onboarding import IsOnboarding
from openapi_server.models.onboarding_request import OnboardingRequest
from openapi_server.models.onboarding_response import OnboardingResponse


pytestmark = pytest.mark.asyncio

async def test_get_setup(client):
    """Test case for get_setup

    Check if database has default user, org, bucket
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/setup',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_setup(client):
    """Test case for post_setup

    Set up initial user, org and bucket
    """
    body = {"bucket":"bucket","password":"password","org":"org","retentionPeriodSeconds":6,"retentionPeriodHrs":0,"token":"token","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/setup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

