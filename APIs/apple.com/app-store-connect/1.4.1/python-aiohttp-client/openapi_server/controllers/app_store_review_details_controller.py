from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_store_review_attachments_response import AppStoreReviewAttachmentsResponse
from openapi_server.models.app_store_review_detail_create_request import AppStoreReviewDetailCreateRequest
from openapi_server.models.app_store_review_detail_response import AppStoreReviewDetailResponse
from openapi_server.models.app_store_review_detail_update_request import AppStoreReviewDetailUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_store_review_details_app_store_review_attachments_get_to_many_related(request: web.Request, id, fields_app_store_review_details=None, fields_app_store_review_attachments=None, limit=None, include=None) -> web.Response:
    """app_store_review_details_app_store_review_attachments_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_review_details: the fields to include for returned resources of type appStoreReviewDetails
    :type fields_app_store_review_details: List[str]
    :param fields_app_store_review_attachments: the fields to include for returned resources of type appStoreReviewAttachments
    :type fields_app_store_review_attachments: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_review_details_create_instance(request: web.Request, body) -> web.Response:
    """app_store_review_details_create_instance

    

    :param body: AppStoreReviewDetail representation
    :type body: dict | bytes

    """
    body = AppStoreReviewDetailCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_review_details_get_instance(request: web.Request, id, fields_app_store_review_details=None, include=None, fields_app_store_review_attachments=None, limit_app_store_review_attachments=None) -> web.Response:
    """app_store_review_details_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_review_details: the fields to include for returned resources of type appStoreReviewDetails
    :type fields_app_store_review_details: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_store_review_attachments: the fields to include for returned resources of type appStoreReviewAttachments
    :type fields_app_store_review_attachments: List[str]
    :param limit_app_store_review_attachments: maximum number of related appStoreReviewAttachments returned (when they are included)
    :type limit_app_store_review_attachments: int

    """
    return web.Response(status=200)


async def app_store_review_details_update_instance(request: web.Request, id, body) -> web.Response:
    """app_store_review_details_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppStoreReviewDetail representation
    :type body: dict | bytes

    """
    body = AppStoreReviewDetailUpdateRequest.from_dict(body)
    return web.Response(status=200)
