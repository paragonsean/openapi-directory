from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.history_item import HistoryItem
from openapi_server.models.history_item_update import HistoryItemUpdate
from openapi_server.models.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from openapi_server.models.visibility import Visibility
from openapi_server import util


async def add_item(request: web.Request, id4n, body) -> web.Response:
    """Add history item

    Add a new history item

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param body: The history item to publish
    :type body: dict | bytes

    """
    body = HistoryItem.from_dict(body)
    return web.Response(status=200)


async def filtered_list(request: web.Request, id4n, include_private=None, organization=None, type=None, qualifier=None, from_date=None, to_date=None, offset=None, limit=None) -> web.Response:
    """List history

    Lists the history of a GUID

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param include_private: Also return private history entries
    :type include_private: bool
    :param organization: Show only entries created by one of the given organizations. This parameter can be used multiple times.
    :type organization: str
    :param type: Show only entries matching one of the given history item types. This parameter can be used multiple times.
    :type type: List[str]
    :param qualifier: Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.
    :type qualifier: List[str]
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


async def list(request: web.Request, id4n, organization_id, include_private=None, offset=None, limit=None) -> web.Response:
    """DEPRECATED - List history

    DEPRECATED - please use filteredList with organization parameter to achieve the same functionality

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param include_private: Also return private history entries
    :type include_private: bool
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def retrieve_item(request: web.Request, id4n, organization_id, sequence_id) -> web.Response:
    """Get history item

    

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param sequence_id: sequenceId
    :type sequence_id: int

    """
    return web.Response(status=200)


async def update_item(request: web.Request, id4n, organization_id, sequence_id, body) -> web.Response:
    """Update history item

    

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param sequence_id: sequenceId
    :type sequence_id: int
    :param body: update
    :type body: dict | bytes

    """
    body = HistoryItemUpdate.from_dict(body)
    return web.Response(status=200)


async def update_item_visibility(request: web.Request, id4n, organization_id, sequence_id, body) -> web.Response:
    """Set history item visibility

    

    :param id4n: GUID to retrieve the history for
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str
    :param sequence_id: sequenceId
    :type sequence_id: int
    :param body: History item visibility restrictions
    :type body: dict | bytes

    """
    body = Visibility.from_dict(body)
    return web.Response(status=200)
