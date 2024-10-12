from typing import List, Dict
from aiohttp import web

from openapi_server.models.end_user_license_agreement_create_request import EndUserLicenseAgreementCreateRequest
from openapi_server.models.end_user_license_agreement_response import EndUserLicenseAgreementResponse
from openapi_server.models.end_user_license_agreement_update_request import EndUserLicenseAgreementUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territories_response import TerritoriesResponse
from openapi_server import util


async def end_user_license_agreements_create_instance(request: web.Request, body) -> web.Response:
    """end_user_license_agreements_create_instance

    

    :param body: EndUserLicenseAgreement representation
    :type body: dict | bytes

    """
    body = EndUserLicenseAgreementCreateRequest.from_dict(body)
    return web.Response(status=200)


async def end_user_license_agreements_delete_instance(request: web.Request, id) -> web.Response:
    """end_user_license_agreements_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def end_user_license_agreements_get_instance(request: web.Request, id, fields_end_user_license_agreements=None, include=None, fields_territories=None, limit_territories=None) -> web.Response:
    """end_user_license_agreements_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_end_user_license_agreements: the fields to include for returned resources of type endUserLicenseAgreements
    :type fields_end_user_license_agreements: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param limit_territories: maximum number of related territories returned (when they are included)
    :type limit_territories: int

    """
    return web.Response(status=200)


async def end_user_license_agreements_territories_get_to_many_related(request: web.Request, id, fields_territories=None, limit=None) -> web.Response:
    """end_user_license_agreements_territories_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def end_user_license_agreements_update_instance(request: web.Request, id, body) -> web.Response:
    """end_user_license_agreements_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: EndUserLicenseAgreement representation
    :type body: dict | bytes

    """
    body = EndUserLicenseAgreementUpdateRequest.from_dict(body)
    return web.Response(status=200)
