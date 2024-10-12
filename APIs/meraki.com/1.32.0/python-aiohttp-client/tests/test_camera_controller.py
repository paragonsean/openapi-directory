# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_create_network_camera_quality_retention_profile(client):
    """Test case for create_network_camera_quality_retention_profile

    Creates new quality retention profile for this network.
    """
    body = openapi_server.CreateNetworkCameraQualityRetentionProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/camera/qualityRetentionProfiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_camera_wireless_profile(client):
    """Test case for create_network_camera_wireless_profile

    Creates a new camera wireless profile for this network.
    """
    body = openapi_server.CreateNetworkCameraWirelessProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_camera_custom_analytics_artifact(client):
    """Test case for create_organization_camera_custom_analytics_artifact

    Create custom analytics artifact
    """
    body = openapi_server.CreateOrganizationCameraCustomAnalyticsArtifactRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_camera_quality_retention_profile(client):
    """Test case for delete_network_camera_quality_retention_profile

    Delete an existing quality retention profile for this network.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_camera_wireless_profile(client):
    """Test case for delete_network_camera_wireless_profile

    Delete an existing camera wireless profile for this network.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_camera_custom_analytics_artifact(client):
    """Test case for delete_organization_camera_custom_analytics_artifact

    Delete Custom Analytics Artifact
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}'.format(organization_id='organization_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_device_camera_snapshot(client):
    """Test case for generate_device_camera_snapshot

    Generate a snapshot of what the camera sees at the specified time and return a link to that image.
    """
    body = openapi_server.GenerateDeviceCameraSnapshotRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/camera/generateSnapshot'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_live(client):
    """Test case for get_device_camera_analytics_live

    Returns live state from camera of analytics zones
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/live'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_overview(client):
    """Test case for get_device_camera_analytics_overview

    Returns an overview of aggregate analytics data for a timespan
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/overview'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_recent(client):
    """Test case for get_device_camera_analytics_recent

    Returns most recent record for analytics zones
    """
    params = [('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/recent'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_zone_history(client):
    """Test case for get_device_camera_analytics_zone_history

    Return historical records for analytic zones
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('objectType', 'object_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/zones/{zone_id}/history'.format(serial='serial_example', zone_id='zone_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_analytics_zones(client):
    """Test case for get_device_camera_analytics_zones

    Returns all configured analytic zones for this camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/analytics/zones'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_custom_analytics(client):
    """Test case for get_device_camera_custom_analytics

    Return custom analytics settings for a camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/customAnalytics'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_quality_and_retention(client):
    """Test case for get_device_camera_quality_and_retention

    Returns quality and retention settings for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/qualityAndRetention'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_sense(client):
    """Test case for get_device_camera_sense

    Returns sense settings for a given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/sense'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_sense_object_detection_models(client):
    """Test case for get_device_camera_sense_object_detection_models

    Returns the MV Sense object detection model list for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/sense/objectDetectionModels'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_video_link(client):
    """Test case for get_device_camera_video_link

    Returns video link to the specified camera
    """
    params = [('timestamp', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/videoLink'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_video_settings(client):
    """Test case for get_device_camera_video_settings

    Returns video settings for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_wireless_profiles(client):
    """Test case for get_device_camera_wireless_profiles

    Returns wireless profile assigned to the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/wirelessProfiles'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_quality_retention_profile(client):
    """Test case for get_network_camera_quality_retention_profile

    Retrieve a single quality retention profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_quality_retention_profiles(client):
    """Test case for get_network_camera_quality_retention_profiles

    List the quality retention profiles for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/qualityRetentionProfiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_schedules(client):
    """Test case for get_network_camera_schedules

    Returns a list of all camera recording schedules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/schedules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_wireless_profile(client):
    """Test case for get_network_camera_wireless_profile

    Retrieve a single camera wireless profile.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_camera_wireless_profiles(client):
    """Test case for get_network_camera_wireless_profiles

    List the camera wireless profiles for this network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_custom_analytics_artifact(client):
    """Test case for get_organization_camera_custom_analytics_artifact

    Get Custom Analytics Artifact
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}'.format(organization_id='organization_id_example', artifact_id='artifact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_custom_analytics_artifacts(client):
    """Test case for get_organization_camera_custom_analytics_artifacts

    List Custom Analytics Artifacts
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/customAnalytics/artifacts'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_camera_onboarding_statuses(client):
    """Test case for get_organization_camera_onboarding_statuses

    Fetch onboarding status of cameras
    """
    params = [('serials', ['serials_example']),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/camera/onboarding/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_custom_analytics(client):
    """Test case for update_device_camera_custom_analytics

    Update custom analytics settings for a camera
    """
    body = openapi_server.UpdateDeviceCameraCustomAnalyticsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/customAnalytics'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_quality_and_retention(client):
    """Test case for update_device_camera_quality_and_retention

    Update quality and retention settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraQualityAndRetentionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/qualityAndRetention'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_sense(client):
    """Test case for update_device_camera_sense

    Update sense settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraSenseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/sense'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_video_settings(client):
    """Test case for update_device_camera_video_settings

    Update video settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraVideoSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_wireless_profiles(client):
    """Test case for update_device_camera_wireless_profiles

    Assign wireless profiles to the given camera
    """
    body = openapi_server.UpdateDeviceCameraWirelessProfilesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/wirelessProfiles'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_camera_quality_retention_profile(client):
    """Test case for update_network_camera_quality_retention_profile

    Update an existing quality retention profile for this network.
    """
    body = openapi_server.UpdateNetworkCameraQualityRetentionProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}'.format(network_id='network_id_example', quality_retention_profile_id='quality_retention_profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_camera_wireless_profile(client):
    """Test case for update_network_camera_wireless_profile

    Update an existing camera wireless profile in this network.
    """
    body = openapi_server.UpdateNetworkCameraWirelessProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}'.format(network_id='network_id_example', wireless_profile_id='wireless_profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_camera_onboarding_statuses(client):
    """Test case for update_organization_camera_onboarding_statuses

    Notify that credential handoff to camera has completed
    """
    body = openapi_server.UpdateOrganizationCameraOnboardingStatusesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/camera/onboarding/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

