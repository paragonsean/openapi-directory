from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.content_submission_shared_business_entities_content_submission_type import ContentSubmissionSharedBusinessEntitiesContentSubmissionType
from openapi_server import util


async def content_submission_types_delete_content_submission_type(request: web.Request, id) -> web.Response:
    """Remove a Content Submission Type

    No Documentation Found.

    :param id: The ID of the Content Submission Type
    :type id: int

    """
    return web.Response(status=200)


async def content_submission_types_get_content_submission_type(request: web.Request, id) -> web.Response:
    """Retrieves a Content Submission Type by its ID.

    No Documentation Found.

    :param id: The ID of the Content Submission Type
    :type id: int

    """
    return web.Response(status=200)


async def content_submission_types_get_content_submission_types(request: web.Request, enabled=None) -> web.Response:
    """Returns available Content Submission Types.

    No Documentation Found.

    :param enabled: 
    :type enabled: bool

    """
    return web.Response(status=200)


async def content_submission_types_post_content_submission_type(request: web.Request, body) -> web.Response:
    """Add a Content Submission Type

    No Documentation Found.

    :param body: The Content Submission Type
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmissionType.from_dict(body)
    return web.Response(status=200)


async def content_submission_types_put_content_submission_type(request: web.Request, id, body) -> web.Response:
    """Update a Content Submission Type

    No Documentation Found.

    :param id: The ID of the Content Submission Type
    :type id: int
    :param body: The Content Submission Type
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentSubmissionType.from_dict(body)
    return web.Response(status=200)
