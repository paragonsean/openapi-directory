from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_conference import InsightsV1Conference
from openapi_server.models.list_conference_response import ListConferenceResponse
from openapi_server import util


async def fetch_conference(request: web.Request, conference_sid) -> web.Response:
    """fetch_conference

    Get a specific Conference Summary.

    :param conference_sid: The unique SID identifier of the Conference.
    :type conference_sid: str

    """
    return web.Response(status=200)


async def list_conference(request: web.Request, conference_sid=None, friendly_name=None, status=None, created_after=None, created_before=None, mixer_region=None, tags=None, subaccount=None, detected_issues=None, end_reason=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_conference

    Get a list of Conference Summaries.

    :param conference_sid: The SID of the conference.
    :type conference_sid: str
    :param friendly_name: Custom label for the conference resource, up to 64 characters.
    :type friendly_name: str
    :param status: Conference status.
    :type status: str
    :param created_after: Conferences created after the provided timestamp specified in ISO 8601 format
    :type created_after: str
    :param created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
    :type created_before: str
    :param mixer_region: Twilio region where the conference media was mixed.
    :type mixer_region: str
    :param tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
    :type tags: str
    :param subaccount: Account SID for the subaccount whose resources you wish to retrieve.
    :type subaccount: str
    :param detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
    :type detected_issues: str
    :param end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
    :type end_reason: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
