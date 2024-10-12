from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_note_request import NewNoteRequest
from openapi_server import util


async def get_note(request: web.Request, accept, content_type, note_id, reason=None) -> web.Response:
    """Retrieve Note

    Retrieves a given note in VTEX DO, filtering by &#x60;noteId&#x60;.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param note_id: Note&#39;s ID.
    :type note_id: str
    :param reason: This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data.
    :type reason: str

    """
    return web.Response(status=200)


async def get_notesbyorder_id(request: web.Request, target_id, accept, content_type, per_page=None, page=None, reason=None) -> web.Response:
    """Get Notes by orderId

    Retrieves notes related to a specific &#x60;orderId&#x60;.

    :param target_id: ID of the order.
    :type target_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param per_page: Number of notes per page. Maximum: 30.
    :type per_page: int
    :param page: Number of the page to be retrieved.
    :type page: int
    :param reason: This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data.
    :type reason: str

    """
    return web.Response(status=200)


async def new_note(request: web.Request, accept, content_type, body=None) -> web.Response:
    """Create Note

    This endpoint creates a new note in VTEX DO. Be aware of the following limitations:    - The maximum number of notes for an order is 30.    - The maximum number of characters in a note&#39;s description is 2000.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewNoteRequest.from_dict(body)
    return web.Response(status=200)
