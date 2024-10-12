from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_attempt_open_response import ActivityAttemptOpenResponse
from openapi_server.models.assignment_mark_response import AssignmentMarkResponse
from openapi_server.models.error import Error
from openapi_server.models.quiz_mark_response import QuizMarkResponse
from openapi_server.models.submission_mark_response import SubmissionMarkResponse
from openapi_server import util


async def offerings_offering_id_analytics_activities_responses_get(request: web.Request, offering_id) -> web.Response:
    """Find open response activity attempts

    Responds with all learner activity attempts for open response activities in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_marks_assignments_get(request: web.Request, offering_id) -> web.Response:
    """Find assessment marks

    Responds with all learner assessment marks in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_marks_quizzes_get(request: web.Request, offering_id) -> web.Response:
    """Find quiz marks

    Responds with all learner quiz marks in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_submissions_assignments_get(request: web.Request, offering_id) -> web.Response:
    """Find submissions to assessments, including marks if any

    Responds with all learner assessment submissions and marks, if any, in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_submissions_open_response_assessment_id_get(request: web.Request, offering_id, assessment_id) -> web.Response:
    """Find submissions to a specified open response assessment, including marks if any

    Responds with all learner assessment submissions and marks, if any, in a specified open response assessment.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_submissions_user_email_assignments_assessment_id_get(request: web.Request, offering_id, user_email, assessment_id) -> web.Response:
    """Find a learner&#39;s submission to a specified assessment, including marks if any

    Responds with the learner&#39;s assessment submission and any marks for the submission.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param user_email: user&#39;s email
    :type user_email: str
    :param assessment_id: assessment&#39;s id
    :type assessment_id: str

    """
    return web.Response(status=200)
