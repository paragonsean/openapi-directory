from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.jurisdiction import Jurisdiction
from openapi_server.models.jurisdiction_classification import JurisdictionClassification
from openapi_server.models.jurisdiction_include import JurisdictionInclude
from openapi_server.models.jurisdiction_list import JurisdictionList
from openapi_server import util


async def jurisdiction_detail_jurisdictions_jurisdiction_id_get(request: web.Request, jurisdiction_id, include=None, apikey=None, x_api_key=None) -> web.Response:
    """Jurisdiction Detail

    Get details on a single Jurisdiction (e.g. state or municipality).

    :param jurisdiction_id: 
    :type jurisdiction_id: str
    :param include: Additional includes for the Jurisdiction response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [JurisdictionInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def jurisdiction_list_jurisdictions_get(request: web.Request, classification=None, include=None, page=None, per_page=None, apikey=None, x_api_key=None) -> web.Response:
    """Jurisdiction List

    Get list of supported Jurisdictions, a Jurisdiction is a state or municipality.

    :param classification: Filter returned jurisdictions by type.
    :type classification: dict | bytes
    :param include: Additional information to include in response.
    :type include: list | bytes
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    classification = .from_dict(classification)
    include = [JurisdictionInclude.from_dict(d) for d in include]
    return web.Response(status=200)
