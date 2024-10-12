from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_beta_detail_response import BuildBetaDetailResponse
from openapi_server.models.build_beta_detail_update_request import BuildBetaDetailUpdateRequest
from openapi_server.models.build_beta_details_response import BuildBetaDetailsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def build_beta_details_build_get_to_one_related(request: web.Request, id, fields_builds=None) -> web.Response:
    """build_beta_details_build_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def build_beta_details_get_collection(request: web.Request, filter_build=None, filter_id=None, fields_build_beta_details=None, limit=None, include=None, fields_builds=None) -> web.Response:
    """build_beta_details_get_collection

    

    :param filter_build: filter by id(s) of related &#39;build&#39;
    :type filter_build: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param fields_build_beta_details: the fields to include for returned resources of type buildBetaDetails
    :type fields_build_beta_details: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def build_beta_details_get_instance(request: web.Request, id, fields_build_beta_details=None, include=None, fields_builds=None) -> web.Response:
    """build_beta_details_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_build_beta_details: the fields to include for returned resources of type buildBetaDetails
    :type fields_build_beta_details: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def build_beta_details_update_instance(request: web.Request, id, body) -> web.Response:
    """build_beta_details_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BuildBetaDetail representation
    :type body: dict | bytes

    """
    body = BuildBetaDetailUpdateRequest.from_dict(body)
    return web.Response(status=200)
