# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee import Attendee
from openapi_server.models.attendee_question import AttendeeQuestion
from openapi_server.models.poll import Poll
from openapi_server.models.session import Session
from openapi_server.models.session_performance import SessionPerformance


pytestmark = pytest.mark.asyncio

async def test_get_all_sessions(client):
    """Test case for get_all_sessions

    Get webinar sessions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizer_sessions(client):
    """Test case for get_organizer_sessions

    Get organizer sessions
    """
    params = [('fromTime', '2013-10-20T19:20:30+01:00'),
                    ('toTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/sessions'.format(organizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_performance(client):
    """Test case for get_performance

    Get session performance
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/performance'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_polls(client):
    """Test case for get_polls

    Get session polls
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/polls'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_questions(client):
    """Test case for get_questions

    Get session questions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/questions'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_surveys(client):
    """Test case for get_surveys

    Get session surveys
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}/surveys'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webinar_session(client):
    """Test case for get_webinar_session

    Get webinar session
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/sessions/{session_key}'.format(organizer_key=56, webinar_key=56, session_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

