# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_journey_planner_itinerary_result import TflApiPresentationEntitiesJourneyPlannerItineraryResult
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode


pytestmark = pytest.mark.asyncio

async def test_journey_journey_results(client):
    """Test case for journey_journey_results

    Perform a Journey Planner search from the parameters specified in simple types
    """
    params = [('via', 'via_example'),
                    ('nationalSearch', True),
                    ('date', '_date_example'),
                    ('time', 'time_example'),
                    ('timeIs', 'time_is_example'),
                    ('journeyPreference', 'journey_preference_example'),
                    ('mode', ['mode_example']),
                    ('accessibilityPreference', ['accessibility_preference_example']),
                    ('fromName', 'from_name_example'),
                    ('toName', 'to_name_example'),
                    ('viaName', 'via_name_example'),
                    ('maxTransferMinutes', 'max_transfer_minutes_example'),
                    ('maxWalkingMinutes', 'max_walking_minutes_example'),
                    ('walkingSpeed', 'walking_speed_example'),
                    ('cyclePreference', 'cycle_preference_example'),
                    ('adjustment', 'adjustment_example'),
                    ('bikeProficiency', ['bike_proficiency_example']),
                    ('alternativeCycle', True),
                    ('alternativeWalking', True),
                    ('applyHtmlMarkup', True),
                    ('useMultiModalCall', True),
                    ('walkingOptimization', True),
                    ('taxiOnlyTrip', True),
                    ('routeBetweenEntrances', True),
                    ('useRealTimeLiveArrivals', True),
                    ('calcOneDirection', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Journey/JourneyResults/{_from}/to/{to}'.format(_from='_from_example', to='to_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_journey_meta(client):
    """Test case for journey_meta

    Gets a list of all of the available journey planner modes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Journey/Meta/Modes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

