# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apple_mapping_create_request import AppleMappingCreateRequest
from openapi_server.models.apple_mapping_get200_response import AppleMappingGet200Response
from openapi_server.models.apple_mapping_test_flight_groups200_response_inner import AppleMappingTestFlightGroups200ResponseInner
from openapi_server.models.devices_get_release_update_devices_status200_response import DevicesGetReleaseUpdateDevicesStatus200Response
from openapi_server.models.devices_list200_response_inner import DevicesList200ResponseInner
from openapi_server.models.devices_register_user_for_device_request import DevicesRegisterUserForDeviceRequest
from openapi_server.models.distibution_releases_install_analytics_request import DistibutionReleasesInstallAnalyticsRequest
from openapi_server.models.organizations_list_administered_default_response_error import OrganizationsListAdministeredDefaultResponseError
from openapi_server.models.provisioning_profile_response import ProvisioningProfileResponse
from openapi_server.models.releases_add_distribution_group201_response import ReleasesAddDistributionGroup201Response
from openapi_server.models.releases_add_distribution_group_request import ReleasesAddDistributionGroupRequest
from openapi_server.models.releases_add_store201_response import ReleasesAddStore201Response
from openapi_server.models.releases_add_store_request import ReleasesAddStoreRequest
from openapi_server.models.releases_add_testers_request import ReleasesAddTestersRequest
from openapi_server.models.releases_create_release_upload201_response import ReleasesCreateReleaseUpload201Response
from openapi_server.models.releases_create_release_upload_request import ReleasesCreateReleaseUploadRequest
from openapi_server.models.releases_get_latest_by_distribution_group200_response import ReleasesGetLatestByDistributionGroup200Response
from openapi_server.models.releases_get_public_groups_for_release_by_hash200_response_inner import ReleasesGetPublicGroupsForReleaseByHash200ResponseInner
from openapi_server.models.releases_get_release_upload_status200_response import ReleasesGetReleaseUploadStatus200Response
from openapi_server.models.releases_list_by_distribution_group200_response_inner import ReleasesListByDistributionGroup200ResponseInner
from openapi_server.models.releases_list_latest200_response_inner import ReleasesListLatest200ResponseInner
from openapi_server.models.releases_put_distribution_group_request import ReleasesPutDistributionGroupRequest
from openapi_server.models.releases_update200_response import ReleasesUpdate200Response
from openapi_server.models.releases_update_details200_response import ReleasesUpdateDetails200Response
from openapi_server.models.releases_update_details400_response import ReleasesUpdateDetails400Response
from openapi_server.models.releases_update_details_request import ReleasesUpdateDetailsRequest
from openapi_server.models.releases_update_release_upload_status200_response import ReleasesUpdateReleaseUploadStatus200Response
from openapi_server.models.releases_update_release_upload_status_request import ReleasesUpdateReleaseUploadStatusRequest
from openapi_server.models.releases_update_request import ReleasesUpdateRequest
from openapi_server.models.store_notifications_get_notification_by_app_id200_response import StoreNotificationsGetNotificationByAppId200Response
from openapi_server.models.store_releases_get_latest200_response_inner import StoreReleasesGetLatest200ResponseInner
from openapi_server.models.store_releases_get_publish_error200_response import StoreReleasesGetPublishError200Response
from openapi_server.models.store_releases_get_real_time_status_by_release_id200_response import StoreReleasesGetRealTimeStatusByReleaseId200Response
from openapi_server.models.store_releases_list200_response_inner import StoreReleasesList200ResponseInner
from openapi_server.models.stores_create_request import StoresCreateRequest
from openapi_server.models.stores_list200_response_inner import StoresList200ResponseInner
from openapi_server.models.stores_patch_request import StoresPatchRequest


pytestmark = pytest.mark.asyncio

async def test_apple_mapping_create(client):
    """Test case for apple_mapping_create

    
    """
    body = openapi_server.AppleMappingCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/apple_mapping'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apple_mapping_delete(client):
    """Test case for apple_mapping_delete

    
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/apple_mapping'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apple_mapping_get(client):
    """Test case for apple_mapping_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/apple_mapping'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apple_mapping_test_flight_groups(client):
    """Test case for apple_mapping_test_flight_groups

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/apple_test_flight_groups'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_device_details(client):
    """Test case for devices_device_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/devices/{device_udid}'.format(device_udid='device_udid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get_release_update_devices_status(client):
    """Test case for devices_get_release_update_devices_status

    
    """
    params = [('include_provisioning_profile', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/update_devices/{resign_id}'.format(release_id='release_id_example', resign_id='resign_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_list(client):
    """Test case for devices_list

    
    """
    params = [('release_id', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices'.format(distribution_group_name='distribution_group_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_list_csv_format(client):
    """Test case for devices_list_csv_format

    
    """
    params = [('unprovisioned_only', False),
                    ('udids', ['udids_example'])]
    headers = { 
        'Accept': 'text/csv',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices/download_devices_list'.format(distribution_group_name='distribution_group_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_register_user_for_device(client):
    """Test case for devices_register_user_for_device

    
    """
    body = openapi_server.DevicesRegisterUserForDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/users/{user_id}/devices/register'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_remove_user_device(client):
    """Test case for devices_remove_user_device

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/user/devices/{device_udid}'.format(device_udid='device_udid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_user_devices_list(client):
    """Test case for devices_user_devices_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/devices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distibution_releases_install_analytics(client):
    """Test case for distibution_releases_install_analytics

    
    """
    body = openapi_server.DistibutionReleasesInstallAnalyticsRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/public/apps/{owner_name}/{app_name}/install_analytics'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provisioning_profile(client):
    """Test case for provisioning_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/provisioning_profile'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_add_distribution_group(client):
    """Test case for releases_add_distribution_group

    
    """
    body = openapi_server.ReleasesAddDistributionGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_add_store(client):
    """Test case for releases_add_store

    
    """
    body = openapi_server.ReleasesAddStoreRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_add_testers(client):
    """Test case for releases_add_testers

    
    """
    body = openapi_server.ReleasesAddTestersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_available_to_tester(client):
    """Test case for releases_available_to_tester

    
    """
    params = [('published_only', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/filter_by_tester'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_create_release_upload(client):
    """Test case for releases_create_release_upload

    
    """
    body = openapi_server.ReleasesCreateReleaseUploadRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/uploads/releases'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete(client):
    """Test case for releases_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete_distribution_group(client):
    """Test case for releases_delete_distribution_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id}'.format(release_id=56, group_id='group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete_distribution_store(client):
    """Test case for releases_delete_distribution_store

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores/{store_id}'.format(release_id=56, store_id='store_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete_distribution_tester(client):
    """Test case for releases_delete_distribution_tester

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id}'.format(release_id=56, tester_id='tester_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete_tester_from_destinations(client):
    """Test case for releases_delete_tester_from_destinations

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/testers/{tester_id}'.format(tester_id='tester_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_delete_with_distribution_group_id(client):
    """Test case for releases_delete_with_distribution_group_id

    
    """
    headers = { 
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id}'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example', release_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_ios_manifest(client):
    """Test case for releases_get_ios_manifest

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/apps/{app_id}/releases/{release_id}/ios_manifest'.format(app_id='app_id_example', release_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_by_distribution_group(client):
    """Test case for releases_get_latest_by_distribution_group

    
    """
    params = [('is_install_page', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id}'.format(owner_name='owner_name_example', app_name='app_name_example', distribution_group_name='distribution_group_name_example', release_id='release_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_by_hash(client):
    """Test case for releases_get_latest_by_hash

    
    """
    params = [('udid', 'udid_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/sdk/apps/{app_secret}/releases/{release_hash}'.format(app_secret='app_secret_example', release_hash='release_hash_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_by_public_distribution_group(client):
    """Test case for releases_get_latest_by_public_distribution_group

    
    """
    params = [('is_install_page', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/sdk/apps/{app_secret}/distribution_groups/{distribution_group_id}/releases/latest'.format(app_secret='app_secret_example', distribution_group_id='distribution_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_by_user(client):
    """Test case for releases_get_latest_by_user

    
    """
    params = [('udid', 'udid_example'),
                    ('is_install_page', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}'.format(release_id='release_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_private_release(client):
    """Test case for releases_get_latest_private_release

    
    """
    params = [('udid', 'udid_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/sdk/apps/{app_secret}/releases/private/latest'.format(app_secret='app_secret_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_latest_public_release(client):
    """Test case for releases_get_latest_public_release

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/sdk/apps/{app_secret}/releases/latest'.format(app_secret='app_secret_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_public_groups_for_release_by_hash(client):
    """Test case for releases_get_public_groups_for_release_by_hash

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/sdk/apps/{app_secret}/releases/{release_hash}/public_distribution_groups'.format(app_secret='app_secret_example', release_hash='release_hash_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_release_upload_status(client):
    """Test case for releases_get_release_upload_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id}'.format(upload_id='upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_get_sparkle_feed(client):
    """Test case for releases_get_sparkle_feed

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/public/sparkle/apps/{app_secret}'.format(app_secret='app_secret_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_list(client):
    """Test case for releases_list

    
    """
    params = [('published_only', True),
                    ('scope', 'scope_example'),
                    ('top', 3.4),
                    ('releaseId', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/releases'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_list_by_distribution_group(client):
    """Test case for releases_list_by_distribution_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases'.format(distribution_group_name='distribution_group_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_list_latest(client):
    """Test case for releases_list_latest

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/recent_releases'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_put_distribution_group(client):
    """Test case for releases_put_distribution_group

    
    """
    body = openapi_server.ReleasesPutDistributionGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id}'.format(release_id=56, group_id='group_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_put_distribution_tester(client):
    """Test case for releases_put_distribution_tester

    
    """
    body = openapi_server.ReleasesPutDistributionGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id}'.format(release_id=56, tester_id='tester_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_releases_update(client):
    """Test case for releases_update

    
    """
    body = openapi_server.ReleasesUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_update_details(client):
    """Test case for releases_update_details

    
    """
    body = openapi_server.ReleasesUpdateDetailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/releases/{release_id}'.format(release_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_releases_update_release_upload_status(client):
    """Test case for releases_update_release_upload_status

    
    """
    body = openapi_server.ReleasesUpdateReleaseUploadStatusRequest()
    params = [('extract', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/uploads/releases/{upload_id}'.format(upload_id='upload_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_notifications_get_notification_by_app_id(client):
    """Test case for store_notifications_get_notification_by_app_id

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/store_service_status'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_release_publish_logs_get(client):
    """Test case for store_release_publish_logs_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_logs'.format(store_name='store_name_example', release_id='release_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_delete(client):
    """Test case for store_releases_delete

    
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}'.format(store_name='store_name_example', release_id='release_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_get(client):
    """Test case for store_releases_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}'.format(store_name='store_name_example', release_id='release_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_get_latest(client):
    """Test case for store_releases_get_latest

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/latest_release'.format(store_name='store_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_get_publish_error(client):
    """Test case for store_releases_get_publish_error

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_error_details'.format(store_name='store_name_example', release_id=3.4, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_get_real_time_status_by_release_id(client):
    """Test case for store_releases_get_real_time_status_by_release_id

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/realtimestatus'.format(store_name='store_name_example', release_id=3.4, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_releases_list(client):
    """Test case for store_releases_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases'.format(store_name='store_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_create(client):
    """Test case for stores_create

    
    """
    body = openapi_server.StoresCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_delete(client):
    """Test case for stores_delete

    
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}'.format(store_name='store_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_get(client):
    """Test case for stores_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}'.format(store_name='store_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_list(client):
    """Test case for stores_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_patch(client):
    """Test case for stores_patch

    
    """
    body = openapi_server.StoresPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}'.format(store_name='store_name_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

