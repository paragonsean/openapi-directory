# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assessment import Assessment
from openapi_server.models.assessment_pending_submission import AssessmentPendingSubmission
from openapi_server.models.assessment_response import AssessmentResponse
from openapi_server.models.assignments import Assignments
from openapi_server.models.error import Error
from openapi_server.models.offering_activities_response import OfferingActivitiesResponse
from openapi_server.models.offerings_offering_id_assessments_assessment_id_user_email_patch_request import OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_activities_openresponse_get(client):
    """Test case for offerings_offering_id_activities_openresponse_get

    Find offering's activities
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/activities/openresponse'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_assessments_assessment_id_documents_document_id_delete(client):
    """Test case for offerings_offering_id_assessments_assessment_id_documents_document_id_delete

    Remove assessment document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/assessments/{assessment_id}/documents/{document_id}'.format(offering_id='offering_id_example', assessment_id='assessment_id_example', document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_assessments_assessment_id_patch(client):
    """Test case for offerings_offering_id_assessments_assessment_id_patch

    Update assessment details
    """
    body = {"dueDate":"2000-01-23T04:56:07.000+00:00","markNumber":"markNumber","markType":"markType","openDate":"2000-01-23T04:56:07.000+00:00","content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/offerings/{offering_id}/assessments/{assessment_id}'.format(offering_id='offering_id_example', assessment_id='assessment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_assessments_assessment_id_user_email_patch(client):
    """Test case for offerings_offering_id_assessments_assessment_id_user_email_patch

    Update the due dates for a learner's quiz attempt
    """
    body = openapi_server.OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/offerings/{offering_id}/assessments/{assessment_id}/{user_email}'.format(offering_id='offering_id_example', assessment_id='assessment_id_example', user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_assessments_get(client):
    """Test case for offerings_offering_id_assessments_get

    Find offering's assessments
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/assessments'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_learners_pending_submission_get(client):
    """Test case for offerings_offering_id_learners_pending_submission_get

    Find learners with assessments pending x days before due date within the specified offeringId
    """
    params = [('days', 'days_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/learners/pending-submission'.format(offering_id='offering_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_user_email_assessments_assessment_id_delete(client):
    """Test case for offerings_offering_id_users_user_email_assessments_assessment_id_delete

    Reset user's assessment to draft state
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/users/{user_email}/assessments/{assessment_id}'.format(offering_id='offering_id_example', user_email='user_email_example', assessment_id='assessment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_user_email_submissions_open_response_get(client):
    """Test case for offerings_offering_id_users_user_email_submissions_open_response_get

    Find learner's open response assessment submissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/users/{user_email}/submissions/open-response'.format(offering_id='offering_id_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

