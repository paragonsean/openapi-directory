from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_license_agreement_response import BetaLicenseAgreementResponse
from openapi_server.models.beta_license_agreement_update_request import BetaLicenseAgreementUpdateRequest
from openapi_server.models.beta_license_agreements_response import BetaLicenseAgreementsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_license_agreements_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """beta_license_agreements_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_license_agreements_get_collection(request: web.Request, filter_app=None, fields_beta_license_agreements=None, limit=None, include=None, fields_apps=None) -> web.Response:
    """beta_license_agreements_get_collection

    

    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param fields_beta_license_agreements: the fields to include for returned resources of type betaLicenseAgreements
    :type fields_beta_license_agreements: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_license_agreements_get_instance(request: web.Request, id, fields_beta_license_agreements=None, include=None, fields_apps=None) -> web.Response:
    """beta_license_agreements_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_license_agreements: the fields to include for returned resources of type betaLicenseAgreements
    :type fields_beta_license_agreements: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_license_agreements_update_instance(request: web.Request, id, body) -> web.Response:
    """beta_license_agreements_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BetaLicenseAgreement representation
    :type body: dict | bytes

    """
    body = BetaLicenseAgreementUpdateRequest.from_dict(body)
    return web.Response(status=200)
