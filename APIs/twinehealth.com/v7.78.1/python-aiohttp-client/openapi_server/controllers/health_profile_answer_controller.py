from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_answer_response import FetchHealthProfileAnswerResponse
from openapi_server.models.fetch_health_profile_answers_response import FetchHealthProfileAnswersResponse
from openapi_server import util


async def fetch_health_profile_answer(request: web.Request, id, include=None) -> web.Response:
    """Get a health profile answer

    Get a health profile answer by id

    :param id: Health profile answer identifier
    :type id: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def fetch_health_profile_answers(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, page_number=None, page_size=None, page_limit=None, page_cursor=None, include=None) -> web.Response:
    """List health profile answers

    Get a list of health profile answers

    :param filter_patient: Patient id to fetch healt profile answers. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
    :type filter_organization: str
    :param page_number: Page number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param page_limit: Page limit
    :type page_limit: int
    :param page_cursor: Page cursor
    :type page_cursor: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)
