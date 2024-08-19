# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_attempt_open_response import ActivityAttemptOpenResponse
from openapi_server.models.assignment_mark_response import AssignmentMarkResponse
from openapi_server.models.error import Error
from openapi_server.models.quiz_mark_response import QuizMarkResponse
from openapi_server.models.submission_mark_response import SubmissionMarkResponse


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_activities_responses_get(client):
    """Test case for offerings_offering_id_analytics_activities_responses_get

    Find open response activity attempts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/activities/responses'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_marks_assignments_get(client):
    """Test case for offerings_offering_id_analytics_marks_assignments_get

    Find assessment marks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/marks/assignments'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_marks_quizzes_get(client):
    """Test case for offerings_offering_id_analytics_marks_quizzes_get

    Find quiz marks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/marks/quizzes'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_submissions_assignments_get(client):
    """Test case for offerings_offering_id_analytics_submissions_assignments_get

    Find submissions to assessments, including marks if any
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/submissions/assignments'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_submissions_open_response_assessment_id_get(client):
    """Test case for offerings_offering_id_analytics_submissions_open_response_assessment_id_get

    Find submissions to a specified open response assessment, including marks if any
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/submissions/open-response/{assessment_id}'.format(offering_id='offering_id_example', assessment_id='assessment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_analytics_submissions_user_email_assignments_assessment_id_get(client):
    """Test case for offerings_offering_id_analytics_submissions_user_email_assignments_assessment_id_get

    Find a learner's submission to a specified assessment, including marks if any
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/analytics/submissions/{user_email}/assignments/{assessment_id}'.format(offering_id='offering_id_example', user_email='user_email_example', assessment_id='assessment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

