# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_webinars_response import AccountWebinarsResponse
from openapi_server.models.attendee import Attendee
from openapi_server.models.audio import Audio
from openapi_server.models.audio_update import AudioUpdate
from openapi_server.models.created_webinar import CreatedWebinar
from openapi_server.models.date_time_range import DateTimeRange
from openapi_server.models.historical_webinar import HistoricalWebinar
from openapi_server.models.session_performance import SessionPerformance
from openapi_server.models.upcoming_webinar import UpcomingWebinar
from openapi_server.models.webinar import Webinar
from openapi_server.models.webinar_by_key import WebinarByKey
from openapi_server.models.webinar_req_create import WebinarReqCreate
from openapi_server.models.webinar_req_update import WebinarReqUpdate


pytestmark = pytest.mark.asyncio

async def test_cancel_webinar(client):
    """Test case for cancel_webinar

    Cancel webinar
    """
    params = [('sendCancellationEmails', True)]
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_webinar(client):
    """Test case for create_webinar

    Create webinar
    """
    body = {"times":[{"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00"},{"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00"}],"isPasswordProtected":False,"subject":"subject","description":"description","timeZone":"timeZone","type":"single_session"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars'.format(organizer_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_account_webinars(client):
    """Test case for get_all_account_webinars

    Get all webinars for an account
    """
    params = [('fromTime', '2013-10-20T19:20:30+01:00'),
                    ('toTime', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/accounts/{account_key}/webinars'.format(account_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_webinars(client):
    """Test case for get_all_webinars

    Get all webinars
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attendees_for_all_webinar_sessions(client):
    """Test case for get_attendees_for_all_webinar_sessions

    Get attendees for all webinar sessions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/attendees'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audio_information(client):
    """Test case for get_audio_information

    Get audio information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/audio'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_historical_webinars(client):
    """Test case for get_historical_webinars

    Get historical webinars
    """
    params = [('fromTime', '2013-10-20T19:20:30+01:00'),
                    ('toTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/historicalWebinars'.format(organizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_performance_for_all_webinar_sessions(client):
    """Test case for get_performance_for_all_webinar_sessions

    Get performance for all webinar sessions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/performance'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upcoming_webinars(client):
    """Test case for get_upcoming_webinars

    Get upcoming webinars
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/upcomingWebinars'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webinar(client):
    """Test case for get_webinar

    Get webinar
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webinar_meeting_times(client):
    """Test case for get_webinar_meeting_times

    Get webinar meeting times
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/meetingtimes'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_audio_information(client):
    """Test case for update_audio_information

    Update audio information
    """
    body = {"pstnInfo":{"tollFreeCountries":["AE","AE"],"tollCountries":["AT","AT"]},"type":"PSTN","privateInfo":{"panelist":"panelist","attendee":"attendee","organizer":"organizer"}}
    params = [('notifyParticipants', True)]
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}/audio'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webinar(client):
    """Test case for update_webinar

    Update webinar
    """
    body = {"times":[{"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00"},{"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00"}],"subject":"subject","description":"description","timeZone":"timeZone","locale":"en_US"}
    params = [('notifyParticipants', True)]
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2W/rest/organizers/{organizer_key}/webinars/{webinar_key}'.format(organizer_key=56, webinar_key=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

