# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.date_time_range import DateTimeRange
from openapi_server.models.session import Session


pytestmark = pytest.mark.asyncio

async def test_get_attendance_details(client):
    """Test case for get_attendance_details

    Get Attendance Details
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/reports/organizers/{organizer_key}/sessions/{session_key}/attendees'.format(organizer_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_details_for_date_range(client):
    """Test case for get_session_details_for_date_range

    Get Sessions by Date Range
    """
    body = {"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2T/rest/reports/organizers/{organizer_key}/sessions'.format(organizer_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session_details_for_training(client):
    """Test case for get_session_details_for_training

    Get Sessions By Training
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2T/rest/reports/organizers/{organizer_key}/trainings/{training_key}'.format(organizer_key=56, training_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

