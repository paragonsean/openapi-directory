# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel


pytestmark = pytest.mark.asyncio

async def test_activities_delete_activity(client):
    """Test case for activities_delete_activity

    Delete an activity
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/activities/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_delete_exceptions(client):
    """Test case for activities_delete_exceptions

    Resets exceptions from a recurring activity.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/activities/{guid}/exceptions'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_participants_delete_activity_participant(client):
    """Test case for activity_participants_delete_activity_participant

    Delete activity participant.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/activities/{activity_guid}/activityparticipants/{activity_participant_guid}'.format(activity_guid='activity_guid_example', activity_participant_guid='activity_participant_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

