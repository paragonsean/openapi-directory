# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.observation_heading import ObservationHeading


pytestmark = pytest.mark.asyncio

async def test_get_available_observation_headings(client):
    """Test case for get_available_observation_headings

    Get Available Observations Types For a User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/availableobservationheadings'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_patient_entered_observation_headings(client):
    """Test case for get_patient_entered_observation_headings

    Get Available Patient Entered Observations Types For a User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/user/{user_id}/patiententeredobservationheadings'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

