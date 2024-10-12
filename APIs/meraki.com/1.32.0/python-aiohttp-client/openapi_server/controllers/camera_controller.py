from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_camera_quality_retention_profile_request import CreateNetworkCameraQualityRetentionProfileRequest
from openapi_server.models.create_network_camera_wireless_profile_request import CreateNetworkCameraWirelessProfileRequest
from openapi_server.models.create_organization_camera_custom_analytics_artifact_request import CreateOrganizationCameraCustomAnalyticsArtifactRequest
from openapi_server.models.generate_device_camera_snapshot_request import GenerateDeviceCameraSnapshotRequest
from openapi_server.models.update_device_camera_custom_analytics_request import UpdateDeviceCameraCustomAnalyticsRequest
from openapi_server.models.update_device_camera_quality_and_retention_request import UpdateDeviceCameraQualityAndRetentionRequest
from openapi_server.models.update_device_camera_sense_request import UpdateDeviceCameraSenseRequest
from openapi_server.models.update_device_camera_video_settings_request import UpdateDeviceCameraVideoSettingsRequest
from openapi_server.models.update_device_camera_wireless_profiles_request import UpdateDeviceCameraWirelessProfilesRequest
from openapi_server.models.update_network_camera_quality_retention_profile_request import UpdateNetworkCameraQualityRetentionProfileRequest
from openapi_server.models.update_network_camera_wireless_profile_request import UpdateNetworkCameraWirelessProfileRequest
from openapi_server.models.update_organization_camera_onboarding_statuses_request import UpdateOrganizationCameraOnboardingStatusesRequest
from openapi_server import util


async def create_network_camera_quality_retention_profile(request: web.Request, network_id, body) -> web.Response:
    """Creates new quality retention profile for this network.

    Creates new quality retention profile for this network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkCameraQualityRetentionProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_camera_wireless_profile(request: web.Request, network_id, body) -> web.Response:
    """Creates a new camera wireless profile for this network.

    Creates a new camera wireless profile for this network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkCameraWirelessProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_camera_custom_analytics_artifact(request: web.Request, organization_id, body=None) -> web.Response:
    """Create custom analytics artifact

    Create custom analytics artifact. Returns an artifact upload URL with expiry time. Upload the artifact file with a put request to the returned upload URL before its expiry.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationCameraCustomAnalyticsArtifactRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_camera_quality_retention_profile(request: web.Request, network_id, quality_retention_profile_id) -> web.Response:
    """Delete an existing quality retention profile for this network.

    Delete an existing quality retention profile for this network.

    :param network_id: 
    :type network_id: str
    :param quality_retention_profile_id: 
    :type quality_retention_profile_id: str

    """
    return web.Response(status=200)


async def delete_network_camera_wireless_profile(request: web.Request, network_id, wireless_profile_id) -> web.Response:
    """Delete an existing camera wireless profile for this network.

    Delete an existing camera wireless profile for this network.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str

    """
    return web.Response(status=200)


async def delete_organization_camera_custom_analytics_artifact(request: web.Request, organization_id, artifact_id) -> web.Response:
    """Delete Custom Analytics Artifact

    Delete Custom Analytics Artifact

    :param organization_id: 
    :type organization_id: str
    :param artifact_id: 
    :type artifact_id: str

    """
    return web.Response(status=200)


async def generate_device_camera_snapshot(request: web.Request, serial, body=None) -> web.Response:
    """Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateDeviceCameraSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_camera_analytics_live(request: web.Request, serial) -> web.Response:
    """Returns live state from camera of analytics zones

    Returns live state from camera of analytics zones

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_overview(request: web.Request, serial, t0=None, t1=None, timespan=None, object_type=None) -> web.Response:
    """Returns an overview of aggregate analytics data for a timespan

    Returns an overview of aggregate analytics data for a timespan

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    :type timespan: float
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_recent(request: web.Request, serial, object_type=None) -> web.Response:
    """Returns most recent record for analytics zones

    Returns most recent record for analytics zones

    :param serial: 
    :type serial: str
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zone_history(request: web.Request, serial, zone_id, t0=None, t1=None, timespan=None, resolution=None, object_type=None) -> web.Response:
    """Return historical records for analytic zones

    Return historical records for analytic zones

    :param serial: 
    :type serial: str
    :param zone_id: 
    :type zone_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
    :type resolution: int
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zones(request: web.Request, serial) -> web.Response:
    """Returns all configured analytic zones for this camera

    Returns all configured analytic zones for this camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_custom_analytics(request: web.Request, serial) -> web.Response:
    """Return custom analytics settings for a camera

    Return custom analytics settings for a camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_quality_and_retention(request: web.Request, serial) -> web.Response:
    """Returns quality and retention settings for the given camera

    Returns quality and retention settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_sense(request: web.Request, serial) -> web.Response:
    """Returns sense settings for a given camera

    Returns sense settings for a given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_sense_object_detection_models(request: web.Request, serial) -> web.Response:
    """Returns the MV Sense object detection model list for the given camera

    Returns the MV Sense object detection model list for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_video_link(request: web.Request, serial, timestamp=None) -> web.Response:
    """Returns video link to the specified camera

    Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

    :param serial: 
    :type serial: str
    :param timestamp: [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
    :type timestamp: str

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)


async def get_device_camera_video_settings(request: web.Request, serial) -> web.Response:
    """Returns video settings for the given camera

    Returns video settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_wireless_profiles(request: web.Request, serial) -> web.Response:
    """Returns wireless profile assigned to the given camera

    Returns wireless profile assigned to the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_camera_quality_retention_profile(request: web.Request, network_id, quality_retention_profile_id) -> web.Response:
    """Retrieve a single quality retention profile

    Retrieve a single quality retention profile

    :param network_id: 
    :type network_id: str
    :param quality_retention_profile_id: 
    :type quality_retention_profile_id: str

    """
    return web.Response(status=200)


async def get_network_camera_quality_retention_profiles(request: web.Request, network_id) -> web.Response:
    """List the quality retention profiles for this network

    List the quality retention profiles for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_camera_schedules(request: web.Request, network_id) -> web.Response:
    """Returns a list of all camera recording schedules.

    Returns a list of all camera recording schedules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_camera_wireless_profile(request: web.Request, network_id, wireless_profile_id) -> web.Response:
    """Retrieve a single camera wireless profile.

    Retrieve a single camera wireless profile.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str

    """
    return web.Response(status=200)


async def get_network_camera_wireless_profiles(request: web.Request, network_id) -> web.Response:
    """List the camera wireless profiles for this network.

    List the camera wireless profiles for this network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_camera_custom_analytics_artifact(request: web.Request, organization_id, artifact_id) -> web.Response:
    """Get Custom Analytics Artifact

    Get Custom Analytics Artifact

    :param organization_id: 
    :type organization_id: str
    :param artifact_id: 
    :type artifact_id: str

    """
    return web.Response(status=200)


async def get_organization_camera_custom_analytics_artifacts(request: web.Request, organization_id) -> web.Response:
    """List Custom Analytics Artifacts

    List Custom Analytics Artifacts

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_camera_onboarding_statuses(request: web.Request, organization_id, serials=None, network_ids=None) -> web.Response:
    """Fetch onboarding status of cameras

    Fetch onboarding status of cameras

    :param organization_id: 
    :type organization_id: str
    :param serials: A list of serial numbers. The returned cameras will be filtered to only include these serials.
    :type serials: List[str]
    :param network_ids: A list of network IDs. The returned cameras will be filtered to only include these networks.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def update_device_camera_custom_analytics(request: web.Request, serial, body=None) -> web.Response:
    """Update custom analytics settings for a camera

    Update custom analytics settings for a camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraCustomAnalyticsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_camera_quality_and_retention(request: web.Request, serial, body=None) -> web.Response:
    """Update quality and retention settings for the given camera

    Update quality and retention settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraQualityAndRetentionRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_camera_sense(request: web.Request, serial, body=None) -> web.Response:
    """Update sense settings for the given camera

    Update sense settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraSenseRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_camera_video_settings(request: web.Request, serial, body=None) -> web.Response:
    """Update video settings for the given camera

    Update video settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraVideoSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_camera_wireless_profiles(request: web.Request, serial, body) -> web.Response:
    """Assign wireless profiles to the given camera

    Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraWirelessProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_camera_quality_retention_profile(request: web.Request, network_id, quality_retention_profile_id, body=None) -> web.Response:
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


async def update_network_camera_wireless_profile(request: web.Request, network_id, wireless_profile_id, body=None) -> web.Response:
    """Update an existing camera wireless profile in this network.

    Update an existing camera wireless profile in this network.

    :param network_id: 
    :type network_id: str
    :param wireless_profile_id: 
    :type wireless_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCameraWirelessProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_camera_onboarding_statuses(request: web.Request, organization_id, body=None) -> web.Response:
    """Notify that credential handoff to camera has completed

    Notify that credential handoff to camera has completed

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationCameraOnboardingStatusesRequest.from_dict(body)
    return web.Response(status=200)
