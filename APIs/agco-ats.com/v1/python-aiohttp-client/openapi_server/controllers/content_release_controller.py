from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_release_version import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion
from openapi_server.models.content_submission_shared_business_entities_content_release_version import ContentSubmissionSharedBusinessEntitiesContentReleaseVersion
from openapi_server import util


async def api_v2_content_releases_content_release_id_get(request: web.Request, content_release_id) -> web.Response:
    """Get a Content Release Version by ID

    Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

    :param content_release_id: The ID of the ContentReleaseVersion to get.
    :type content_release_id: int

    """
    return web.Response(status=200)


async def content_release_delete_content_release_versionn(request: web.Request, content_release_id) -> web.Response:
    """Delete a ContentReleaseVersion

    Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

    :param content_release_id: The ID of the ContentReleaseVersion to delete
    :type content_release_id: int

    """
    return web.Response(status=200)


async def content_release_get_content_release_version(request: web.Request, limit=None, offset=None, deleted=None, release_id=None, user_id=None, content_definition_id=None, version=None) -> web.Response:
    """Get ContentReleaseVersion

    Gets a collection of ContentReleaseVersion. When successful, the response is a PagedResponse of ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param deleted: Optional. Filter by deleted.
    :type deleted: bool
    :param release_id: Optional. Filter by releaseID.
    :type release_id: int
    :param user_id: Optional. Filter by UserID.
    :type user_id: int
    :param content_definition_id: Optional. Filter by ContentDefinitionID.
    :type content_definition_id: int
    :param version: Optional. Filter by Version.
    :type version: int

    """
    return web.Response(status=200)


async def content_release_post_content_release(request: web.Request, body) -> web.Response:
    """Create a ContentReleaseVersion

    Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.              The ContentReleaseId will be assigned on creation of the Job.  When successful, the response              is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.

    :param body: The ContentReleaseVersion to create.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.from_dict(body)
    return web.Response(status=200)


async def content_release_put_content_definition(request: web.Request, content_release_id, body) -> web.Response:
    """Update a ContentReleaseVersion

    Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param content_release_id: The ID of the ContentReleaseVersion to update
    :type content_release_id: int
    :param body: The updated ContentReleaseVersion
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.from_dict(body)
    return web.Response(status=200)
