from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_app_review_detail_response import BetaAppReviewDetailResponse
from openapi_server.models.beta_app_review_detail_update_request import BetaAppReviewDetailUpdateRequest
from openapi_server.models.beta_app_review_details_response import BetaAppReviewDetailsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_app_review_details_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """beta_app_review_details_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_review_details_get_collection(request: web.Request, filter_app, fields_beta_app_review_details=None, limit=None, include=None, fields_apps=None) -> web.Response:
    """beta_app_review_details_get_collection

    

    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param fields_beta_app_review_details: the fields to include for returned resources of type betaAppReviewDetails
    :type fields_beta_app_review_details: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_review_details_get_instance(request: web.Request, id, fields_beta_app_review_details=None, include=None, fields_apps=None) -> web.Response:
    """beta_app_review_details_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_review_details: the fields to include for returned resources of type betaAppReviewDetails
    :type fields_beta_app_review_details: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_review_details_update_instance(request: web.Request, id, body) -> web.Response:
    """beta_app_review_details_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BetaAppReviewDetail representation
    :type body: dict | bytes

    """
    body = BetaAppReviewDetailUpdateRequest.from_dict(body)
    return web.Response(status=200)
