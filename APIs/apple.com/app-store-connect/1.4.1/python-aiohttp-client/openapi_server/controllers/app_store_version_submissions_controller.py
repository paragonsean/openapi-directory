from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_store_version_submission_create_request import AppStoreVersionSubmissionCreateRequest
from openapi_server.models.app_store_version_submission_response import AppStoreVersionSubmissionResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_store_version_submissions_create_instance(request: web.Request, body) -> web.Response:
    """app_store_version_submissions_create_instance

    

    :param body: AppStoreVersionSubmission representation
    :type body: dict | bytes

    """
    body = AppStoreVersionSubmissionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_version_submissions_delete_instance(request: web.Request, id) -> web.Response:
    """app_store_version_submissions_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)
