from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.paginated_response_of_change_log_entry import PaginatedResponseOfChangeLogEntry
from openapi_server import util


async def list_organization_change_log(request: web.Request, organization_id, message_mime_type=None, from_date=None, to_date=None, offset=None, limit=None) -> web.Response:
    """List change log entries of an organization

    Listing change log entries of the specified organization id.

    :param organization_id: The namespace identifying the organization whose change log entries are to be listed
    :type organization_id: str
    :param message_mime_type: The Mime-type for the message format that should be returned. e.g. &#39;text/plain&#39; or &#39;text/mustache&#39; 
    :type message_mime_type: str
    :param from_date: From date time as UTC Date-Time format
    :type from_date: str
    :param to_date: To date time as UTC Date-Time format
    :type to_date: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)
