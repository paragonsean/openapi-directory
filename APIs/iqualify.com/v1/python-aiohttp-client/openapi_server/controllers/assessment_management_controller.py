from typing import List, Dict
from aiohttp import web

from openapi_server.models.assessment import Assessment
from openapi_server.models.assessment_pending_submission import AssessmentPendingSubmission
from openapi_server.models.assessment_response import AssessmentResponse
from openapi_server.models.assignments import Assignments
from openapi_server.models.error import Error
from openapi_server.models.offering_activities_response import OfferingActivitiesResponse
from openapi_server.models.offerings_offering_id_assessments_assessment_id_user_email_patch_request import OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest
from openapi_server import util


async def offerings_offering_id_activities_openresponse_get(request: web.Request, offering_id) -> web.Response:
    """Find offering&#39;s activities

    Responds with the activities in a specific offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_assessments_assessment_id_documents_document_id_delete(request: web.Request, offering_id, assessment_id, document_id) -> web.Response:
    """Remove assessment document

    Removes the assessment document file for a specified assessment in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str
    :param document_id: documents&#39;s id
    :type document_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_assessments_assessment_id_patch(request: web.Request, offering_id, assessment_id, body) -> web.Response:
    """Update assessment details

    Updates the assessment details for a specified assessment in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Assessment.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_assessments_assessment_id_user_email_patch(request: web.Request, offering_id, assessment_id, user_email, body) -> web.Response:
    """Update the due dates for a learner&#39;s quiz attempt

    Updates the due dates for a learner&#39;s quiz attempt specified by the assessmentId.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str
    :param user_email: user&#39;s email
    :type user_email: str
    :param body: 
    :type body: dict | bytes

    """
    body = OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_assessments_get(request: web.Request, offering_id) -> web.Response:
    """Find offering&#39;s assessments

    Responds with all assessments in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_learners_pending_submission_get(request: web.Request, offering_id, days=None) -> web.Response:
    """Find learners with assessments pending x days before due date within the specified offeringId

    Responds with learners who have one or more assessments due x days before the due date, with each assessment that is due, where x &#x3D; the number of days specified in the request. The default is 3 days.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param days: days to assessment due date. Default is 3 days
    :type days: str

    """
    return web.Response(status=200)


async def offerings_offering_id_users_user_email_assessments_assessment_id_delete(request: web.Request, offering_id, user_email, assessment_id) -> web.Response:
    """Reset user&#39;s assessment to draft state

    Resets the user&#39;s submitted assessment to a draft state.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param user_email: user&#39;s email
    :type user_email: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_users_user_email_submissions_open_response_get(request: web.Request, offering_id, user_email) -> web.Response:
    """Find learner&#39;s open response assessment submissions

    Responds with open response assessment submissions by a learner in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)
