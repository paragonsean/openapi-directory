# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_category import ActivityCategory
from openapi_server.models.activity_model import ActivityModel
from openapi_server.models.activity_participant_model import ActivityParticipantModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.recurrence_type import RecurrenceType


pytestmark = pytest.mark.asyncio

async def test_activities_get_activities(client):
    """Test case for activities_get_activities

    Get all activities of an organization
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('closed', True),
                    ('activityCategories', [openapi_server.ActivityCategory()]),
                    ('customerGuids', ['customer_guids_example']),
                    ('includeTasksWithNoCustomer', True),
                    ('projectGuids', ['project_guids_example']),
                    ('includeTasksWithNoProject', True),
                    ('projectBusinessUnitGuids', ['project_business_unit_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('userGuids', ['user_guids_example']),
                    ('includeAsMember', False),
                    ('userKeywordGuids', ['user_keyword_guids_example']),
                    ('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('projectTaskStatusGuids', ['project_task_status_guids_example']),
                    ('phaseGuids', ['phase_guids_example']),
                    ('includeSubPhases', False),
                    ('contactGuids', ['contact_guids_example']),
                    ('hasDuration', True),
                    ('hasHours', True),
                    ('isUnassigned', True),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('useStrictStartAndEndDateTime', False),
                    ('activityTypeGuids', ['activity_type_guids_example']),
                    ('recurrenceType', openapi_server.RecurrenceType())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_get_activity(client):
    """Test case for activities_get_activity

    Get activity by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activities/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_participants_get_activity_participant(client):
    """Test case for activity_participants_get_activity_participant

    Get activity participant
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activityparticipants/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_participants_get_activity_participants(client):
    """Test case for activity_participants_get_activity_participants

    Get participants for an activity
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/activities/{activity_guid}/activityparticipants'.format(activity_guid='activity_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

