from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_lines import BusinessLines
from openapi_server.models.data_review_confirmation_response import DataReviewConfirmationResponse
from openapi_server.models.legal_entity import LegalEntity
from openapi_server.models.legal_entity_info import LegalEntityInfo
from openapi_server.models.legal_entity_info_required_type import LegalEntityInfoRequiredType
from openapi_server.models.service_error import ServiceError
from openapi_server.models.verification_errors import VerificationErrors
from openapi_server import util


async def get_legal_entities_id(request: web.Request, id) -> web.Response:
    """Get a legal entity

    Returns a legal entity.

    :param id: The unique identifier of the legal entity.
    :type id: str

    """
    return web.Response(status=200)


async def get_legal_entities_id_business_lines(request: web.Request, id) -> web.Response:
    """Get all business lines under a legal entity

    Returns the business lines owned by a legal entity.

    :param id: The unique identifier of the legal entity.
    :type id: str

    """
    return web.Response(status=200)


async def patch_legal_entities_id(request: web.Request, id, x_requested_verification_code=None, body=None) -> web.Response:
    """Update a legal entity

    Updates a legal entity.   &gt;To change the legal entity type, include only the new &#x60;type&#x60; in your request. To update the &#x60;entityAssociations&#x60; array, you need to replace the entire array. For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

    :param id: The unique identifier of the legal entity.
    :type id: str
    :param x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = LegalEntityInfo.from_dict(body)
    return web.Response(status=200)


async def post_legal_entities(request: web.Request, x_requested_verification_code=None, body=None) -> web.Response:
    """Create a legal entity

    Creates a legal entity.   This resource contains information about the user that will be onboarded in your platform. Adyen uses this information to perform verification checks as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.   &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

    :param x_requested_verification_code: Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = LegalEntityInfoRequiredType.from_dict(body)
    return web.Response(status=200)


async def post_legal_entities_id_check_verification_errors(request: web.Request, id) -> web.Response:
    """Check a legal entity&#39;s verification errors

    Returns the verification errors for a legal entity and its supporting entities.

    :param id: The unique identifier of the legal entity.
    :type id: str

    """
    return web.Response(status=200)


async def post_legal_entities_id_confirm_data_review(request: web.Request, id) -> web.Response:
    """Confirm data review

    Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the timestamp of when Adyen received the request.

    :param id: The unique identifier of the legal entity.
    :type id: str

    """
    return web.Response(status=200)
