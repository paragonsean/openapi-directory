# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.attendee_question import AttendeeQuestion
from openapi_server.models.poll_answer import PollAnswer
from openapi_server.models.registrant import Registrant


pytestmark = pytest.mark.asyncio

async def test_get_attendee(client):
    """Test case for get_attendee

    Get attendee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/attendees/{registrant_key}'.format(organizer_key=56, webinar_key=56, session_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attendee_poll_answers(client):
    """Test case for get_attendee_poll_answers

    Get attendee poll answers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/attendees/{registrant_key}/polls'.format(organizer_key=56, webinar_key=56, session_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attendee_questions(client):
    """Test case for get_attendee_questions

    Get attendee questions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/attendees/{registrant_key}/questions'.format(organizer_key=56, webinar_key=56, session_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attendee_survey_answers(client):
    """Test case for get_attendee_survey_answers

    Get attendee survey answers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/attendees/{registrant_key}/surveys'.format(organizer_key=56, webinar_key=56, session_key=56, registrant_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attendees(client):
    """Test case for get_attendees

    Get session attendees
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/attendees'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

