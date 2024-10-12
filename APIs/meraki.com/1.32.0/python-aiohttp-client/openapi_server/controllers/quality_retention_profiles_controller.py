from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_camera_quality_retention_profile_request import CreateNetworkCameraQualityRetentionProfileRequest
from openapi_server.models.update_network_camera_quality_retention_profile_request import UpdateNetworkCameraQualityRetentionProfileRequest
from openapi_server import util


async def create_network_camera_quality_retention_profile_1(request: web.Request, network_id, body) -> web.Response:
    """Creates new quality retention profile for this network.

    Creates new quality retention profile for this network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkCameraQualityRetentionProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_camera_quality_retention_profile_1(request: web.Request, network_id, quality_retention_profile_id) -> web.Response:
    """Delete an existing quality retention profile for this network.

    Delete an existing quality retention profile for this network.

    :param network_id: 
    :type network_id: str
    :param quality_retention_profile_id: 
    :type quality_retention_profile_id: str

    """
    return web.Response(status=200)


async def get_network_camera_quality_retention_profile_1(request: web.Request, network_id, quality_retention_profile_id) -> web.Response:
    """Retrieve a single quality retention profile

    Retrieve a single quality retention profile

    :param network_id: 
    :type network_id: str
    :param quality_retention_profile_id: 
    :type quality_retention_profile_id: str

    """
    return web.Response(status=200)


async def get_network_camera_quality_retention_profiles_1(request: web.Request, network_id) -> web.Response:
    """List the quality retention profiles for this network

    List the quality retention profiles for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_camera_quality_retention_profile_1(request: web.Request, network_id, quality_retention_profile_id, body=None) -> web.Response:
    """Update an existing quality retention profile for this network.

    Update an existing quality retention profile for this network.

    :param network_id: 
    :type network_id: str
    :param quality_retention_profile_id: 
    :type quality_retention_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCameraQualityRetentionProfileRequest.from_dict(body)
    return web.Response(status=200)
