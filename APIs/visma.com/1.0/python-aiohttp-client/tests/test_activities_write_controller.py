# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_model import ActivityModel
from openapi_server.models.activity_participant_model import ActivityParticipantModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation


pytestmark = pytest.mark.asyncio

async def test_activities_patch_activity(client):
    """Test case for activities_patch_activity

    Update (Patch) a activity or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/activities/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_post_activity(client):
    """Test case for activities_post_activity

    Insert a activity
    """
    body = {"phase":{"isLocked":True,"projectGuid":"projectGuid","projectNumber":6,"name":"name","guid":"guid","projectOwnerGuid":"projectOwnerGuid","projectName":"projectName"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"notes":"notes","isUnassigned":True,"createdDateTime":"2000-01-23T04:56:07.000+00:00","recurrenceRule":"recurrenceRule","hasHours":True,"endDateTime":"2000-01-23T04:56:07.000+00:00","recurrenceType":"None","projectTaskStatus":{"name":"name","guid":"guid"},"recurrence":{"lastOccurrenceDateTime":"2000-01-23T04:56:07.000+00:00","pattern":{"daily":{"everyWeekday":True,"interval":1},"monthly":{"dayOfMonth":5,"dayOrdinal":"First","dayOrdinalOption":"Sunday","interval":5},"yearly":{"month":"January","dayOfMonth":7},"weekly":{"sunday":True,"saturday":True,"tuesday":True,"friday":True,"thursday":True,"wednesday":True,"interval":2,"monday":True}},"range":{"recursUntilDate":"2000-01-23","maxOccurrences":9},"exceptions":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"frequency":"Daily"},"isAllDay":True,"ownerUser":{"code":"code","keywords":[{"guid":"guid","value":"value"},{"guid":"guid","value":"value"}],"name":"name","guid":"guid"},"recurrenceParentActivityGuid":"recurrenceParentActivityGuid","startDateTime":"2000-01-23T04:56:07.000+00:00","isClosed":True,"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"hasDuration":True,"name":"name","guid":"guid","location":"location","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","activityType":{"name":"name","guid":"guid","category":"Personal"},"customer":{"number":0,"name":"name","guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_participants_patch_activity_participants(client):
    """Test case for activity_participants_patch_activity_participants

    Update (Patch) a activity participant or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/activityparticipants/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_participants_post_activity_participant(client):
    """Test case for activity_participants_post_activity_participant

    Adds an activity participant
    """
    body = {"participantGuid":"participantGuid","mobilePhone":"mobilePhone","phone":"phone","activityGuid":"activityGuid","name":"name","guid":"guid","isActive":True,"type":"User","email":"email","status":"Unknown"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/activityparticipants',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

