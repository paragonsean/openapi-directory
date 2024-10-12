# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offerings_offering_id_analytics_pulses_responses_get_response_time_parameter import OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter
from openapi_server.models.pulse_response import PulseResponse


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_pulses_get(client):
    """Test case for offerings_offering_id_analytics_pulses_get

    Find all pulse IDs in the specified offering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/pulses'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_pulses_pulse_id_responses_get(client):
    """Test case for offerings_offering_id_analytics_pulses_pulse_id_responses_get

    Find pulses by offeringId and pulseId
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/pulses/{pulse_id}/responses'.format(offering_id='offering_id_example', pulse_id='pulse_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_pulses_responses_get(client):
    """Test case for offerings_offering_id_analytics_pulses_responses_get

    Find pulses by offeringId
    """
    params = [('pulseType', 'pulse_type_example'),
                    ('responseTime', openapi_server.OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/pulses/responses'.format(offering_id='offering_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

