from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_dispute_request import AcceptDisputeRequest
from openapi_server.models.accept_dispute_response import AcceptDisputeResponse
from openapi_server.models.defend_dispute_request import DefendDisputeRequest
from openapi_server.models.defend_dispute_response import DefendDisputeResponse
from openapi_server.models.defense_reasons_request import DefenseReasonsRequest
from openapi_server.models.defense_reasons_response import DefenseReasonsResponse
from openapi_server.models.delete_defense_document_request import DeleteDefenseDocumentRequest
from openapi_server.models.delete_defense_document_response import DeleteDefenseDocumentResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.supply_defense_document_request import SupplyDefenseDocumentRequest
from openapi_server.models.supply_defense_document_response import SupplyDefenseDocumentResponse
from openapi_server import util


async def post_accept_dispute(request: web.Request, body=None) -> web.Response:
    """Accept a dispute

    Accepts a specific dispute.

    :param body: 
    :type body: dict | bytes

    """
    body = AcceptDisputeRequest.from_dict(body)
    return web.Response(status=200)


async def post_defend_dispute(request: web.Request, body=None) -> web.Response:
    """Defend a dispute

    Defends a specific dispute.

    :param body: 
    :type body: dict | bytes

    """
    body = DefendDisputeRequest.from_dict(body)
    return web.Response(status=200)


async def post_delete_dispute_defense_document(request: web.Request, body=None) -> web.Response:
    """Delete a defense document

    Deletes a specific dispute defense document that was supplied earlier.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteDefenseDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def post_retrieve_applicable_defense_reasons(request: web.Request, body=None) -> web.Response:
    """Get applicable defense reasons

    Returns a list of all applicable defense reasons to defend a specific dispute.

    :param body: 
    :type body: dict | bytes

    """
    body = DefenseReasonsRequest.from_dict(body)
    return web.Response(status=200)


async def post_supply_defense_document(request: web.Request, body=None) -> web.Response:
    """Supply a defense document

    Supplies a specific dispute defense document.

    :param body: 
    :type body: dict | bytes

    """
    body = SupplyDefenseDocumentRequest.from_dict(body)
    return web.Response(status=200)
