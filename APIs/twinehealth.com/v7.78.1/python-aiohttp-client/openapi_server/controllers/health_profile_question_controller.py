from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_question_response import FetchHealthProfileQuestionResponse
from openapi_server.models.fetch_health_profile_questions_response import FetchHealthProfileQuestionsResponse
from openapi_server import util


async def fetch_health_profile_question(request: web.Request, id, include=None) -> web.Response:
    """Get a health profile question

    Get a health profile by id

    :param id: Health profile question identifier
    :type id: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def fetch_health_profile_questions(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, include=None) -> web.Response:
    """List health profile questions

    Get a list of health profile questions

    :param filter_patient: Patient id to fetch healt profile questions. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_organization: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)
