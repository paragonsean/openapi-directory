from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.received_document import ReceivedDocument
from openapi_server.models.received_document_create import ReceivedDocumentCreate
from openapi_server import util


async def get_received_document(request: web.Request, guid, syntax, format) -> web.Response:
    """Get a new ReceivedDocument

    EXPERIMENTAL: use only for orders. Get a new ReceivedDocument.

    :param guid: The guid of the document that was received. This is the \&quot;document_guid\&quot; property of the \&quot;received_document\&quot; webhook.
    :type guid: str
    :type guid: str
    :param syntax: The syntax in which to receive the received document.
    :type syntax: str
    :param format: Automatically added
    :type format: str

    """
    return web.Response(status=200)


async def receive_document(request: web.Request, legal_entity_id, body) -> web.Response:
    """Receive a new Document

    Receive a new Document.

    :param legal_entity_id: The id of the LegalEntity for which the document was received.
    :type legal_entity_id: int
    :param body: Received document to process.
    :type body: dict | bytes

    """
    body = ReceivedDocumentCreate.from_dict(body)
    return web.Response(status=200)
