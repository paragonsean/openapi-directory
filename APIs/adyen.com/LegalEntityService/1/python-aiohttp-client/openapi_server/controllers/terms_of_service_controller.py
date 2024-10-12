from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_terms_of_service_request import AcceptTermsOfServiceRequest
from openapi_server.models.accept_terms_of_service_response import AcceptTermsOfServiceResponse
from openapi_server.models.calculate_terms_of_service_status_response import CalculateTermsOfServiceStatusResponse
from openapi_server.models.get_terms_of_service_acceptance_infos_response import GetTermsOfServiceAcceptanceInfosResponse
from openapi_server.models.get_terms_of_service_document_request import GetTermsOfServiceDocumentRequest
from openapi_server.models.get_terms_of_service_document_response import GetTermsOfServiceDocumentResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_legal_entities_id_terms_of_service_acceptance_infos(request: web.Request, id) -> web.Response:
    """Get Terms of Service information for a legal entity

    Returns Terms of Service information for a legal entity.

    :param id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    :type id: str

    """
    return web.Response(status=200)


async def get_legal_entities_id_terms_of_service_status(request: web.Request, id) -> web.Response:
    """Get Terms of Service status

    Returns the required types of Terms of Service that need to be accepted by a legal entity.

    :param id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    :type id: str

    """
    return web.Response(status=200)


async def patch_legal_entities_id_terms_of_service_termsofservicedocumentid(request: web.Request, id, termsofservicedocumentid, body=None) -> web.Response:
    """Accept Terms of Service

    Accepts Terms of Service.

    :param id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    :type id: str
    :param termsofservicedocumentid: The unique identifier of the Terms of Service document.
    :type termsofservicedocumentid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AcceptTermsOfServiceRequest.from_dict(body)
    return web.Response(status=200)


async def post_legal_entities_id_terms_of_service(request: web.Request, id, body=None) -> web.Response:
    """Get Terms of Service document

    Returns the Terms of Service document for a legal entity.

    :param id: The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetTermsOfServiceDocumentRequest.from_dict(body)
    return web.Response(status=200)
