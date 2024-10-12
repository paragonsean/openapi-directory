from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_store_review_attachment_create_request import AppStoreReviewAttachmentCreateRequest
from openapi_server.models.app_store_review_attachment_response import AppStoreReviewAttachmentResponse
from openapi_server.models.app_store_review_attachment_update_request import AppStoreReviewAttachmentUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_store_review_attachments_create_instance(request: web.Request, body) -> web.Response:
    """app_store_review_attachments_create_instance

    

    :param body: AppStoreReviewAttachment representation
    :type body: dict | bytes

    """
    body = AppStoreReviewAttachmentCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_review_attachments_delete_instance(request: web.Request, id) -> web.Response:
    """app_store_review_attachments_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_store_review_attachments_get_instance(request: web.Request, id, fields_app_store_review_attachments=None, include=None) -> web.Response:
    """app_store_review_attachments_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_review_attachments: the fields to include for returned resources of type appStoreReviewAttachments
    :type fields_app_store_review_attachments: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_review_attachments_update_instance(request: web.Request, id, body) -> web.Response:
    """app_store_review_attachments_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppStoreReviewAttachment representation
    :type body: dict | bytes

    """
    body = AppStoreReviewAttachmentUpdateRequest.from_dict(body)
    return web.Response(status=200)
