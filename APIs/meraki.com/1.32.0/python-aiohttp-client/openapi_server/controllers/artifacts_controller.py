from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_camera_custom_analytics_artifact_request import CreateOrganizationCameraCustomAnalyticsArtifactRequest
from openapi_server import util


async def create_organization_camera_custom_analytics_artifact_2(request: web.Request, organization_id, body=None) -> web.Response:
    """Create custom analytics artifact

    Create custom analytics artifact. Returns an artifact upload URL with expiry time. Upload the artifact file with a put request to the returned upload URL before its expiry.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationCameraCustomAnalyticsArtifactRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_camera_custom_analytics_artifact_2(request: web.Request, organization_id, artifact_id) -> web.Response:
    """Delete Custom Analytics Artifact

    Delete Custom Analytics Artifact

    :param organization_id: 
    :type organization_id: str
    :param artifact_id: 
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_organization_camera_custom_analytics_artifact_2(request: web.Request, organization_id, artifact_id) -> web.Response:
    """Get Custom Analytics Artifact

    Get Custom Analytics Artifact

    :param organization_id: 
    :type organization_id: str
    :param artifact_id: 
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_organization_camera_custom_analytics_artifacts_2(request: web.Request, organization_id) -> web.Response:
    """List Custom Analytics Artifacts

    List Custom Analytics Artifacts

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
