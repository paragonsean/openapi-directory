from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_release import APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease
from openapi_server.models.content_submission_shared_business_entities_release import ContentSubmissionSharedBusinessEntitiesRelease
from openapi_server import util


async def release_delete_release_bundle(request: web.Request, release_id, bundle_id) -> web.Response:
    """Deletes the association between a release and a bundle.

    No Documentation Found.

    :param release_id: The release identifier.
    :type release_id: int
    :param bundle_id: The bundle identifier.
    :type bundle_id: str

    """
    return web.Response(status=200)


async def release_get_releases(request: web.Request, limit=None, offset=None, visible=None, bundle_id=None) -> web.Response:
    """Get Release

    Gets a collection of Release. When successful, the response is a PagedResponse of Release.              If unsuccessful, an appropriate ApiError is returned.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param visible: Optional. Filter by visible.
    :type visible: bool
    :param bundle_id: Optional. Filter by BundleID.
    :type bundle_id: str

    """
    return web.Response(status=200)


async def release_post_release(request: web.Request, body) -> web.Response:
    """Create a Release

    Creates a Release.  The body of the POST is the Release to create.              The ReleaseId will be assigned on creation of the Job.  When successful, the response              is the Release Id.  If unsuccessful, an appropriate ApiError is returned.

    :param body: The Release to create.
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesRelease.from_dict(body)
    return web.Response(status=200)


async def release_post_release_bundle(request: web.Request, release_id, bundle_id) -> web.Response:
    """Associates the release with a bundle.

    No Documentation Found.

    :param release_id: The release identifier.
    :type release_id: int
    :param bundle_id: The bundle identifier.
    :type bundle_id: str

    """
    return web.Response(status=200)


async def release_put_content_definition(request: web.Request, release_id, body) -> web.Response:
    """Update a Release

    Updates a Release.  The body of the PUT is the updated Release.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

    :param release_id: The ID of the Release to update
    :type release_id: int
    :param body: The updated Release
    :type body: dict | bytes

    """
    body = ContentSubmissionSharedBusinessEntitiesRelease.from_dict(body)
    return web.Response(status=200)
