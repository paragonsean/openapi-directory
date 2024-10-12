from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_response import FetchHealthProfileResponse
from openapi_server.models.fetch_health_profiles_response import FetchHealthProfilesResponse
from openapi_server import util


async def fetch_health_profile(request: web.Request, id, include=None) -> web.Response:
    """Get a health profile

    Get a health profile by id

    :param id: Health profile identifier
    :type id: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def fetch_health_profiles(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, page_number=None, page_size=None, page_limit=None, page_cursor=None, include=None) -> web.Response:
    """List health profiles

    Get a list of health profiles

    :param filter_patient: Patient id to fetch health profile. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;. 
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
