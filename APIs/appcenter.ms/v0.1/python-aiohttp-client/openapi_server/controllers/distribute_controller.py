from typing import List, Dict
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
from openapi_server import util


async def apple_mapping_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """apple_mapping_create

    Create a mapping for an existing app in apple store for the specified application.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The apple app mapping object
    :type body: dict | bytes

    """
    body = AppleMappingCreateRequest.from_dict(body)
    return web.Response(status=200)


async def apple_mapping_delete(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """apple_mapping_delete

    Delete mapping of apple app to an existing app in apple store.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def apple_mapping_get(request: web.Request, owner_name, app_name) -> web.Response:
    """apple_mapping_get

    Get mapping of apple app to an existing app in apple store.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def apple_mapping_test_flight_groups(request: web.Request, owner_name, app_name) -> web.Response:
    """apple_mapping_test_flight_groups

    Fetch all apple test flight groups

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def devices_device_details(request: web.Request, device_udid) -> web.Response:
    """devices_device_details

    Returns the device details.

    :param device_udid: The UDID of the device
    :type device_udid: str

    """
    return web.Response(status=200)


async def devices_get_release_update_devices_status(request: web.Request, release_id, resign_id, owner_name, app_name, include_provisioning_profile=None) -> web.Response:
    """devices_get_release_update_devices_status

    Returns the resign status to the caller

    :param release_id: The ID of the release.
    :type release_id: str
    :param resign_id: The ID of the resign operation.
    :type resign_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param include_provisioning_profile: A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is &#39;complete&#39; or &#39;preparing_for_testers&#39;.
    :type include_provisioning_profile: bool

    """
    return web.Response(status=200)


async def devices_list(request: web.Request, distribution_group_name, owner_name, app_name, release_id=None) -> web.Response:
    """devices_list

    Returns all devices associated with the given distribution group

    :param distribution_group_name: The name of the distribution group.
    :type distribution_group_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param release_id: when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release.
    :type release_id: 

    """
    return web.Response(status=200)


async def devices_list_csv_format(request: web.Request, distribution_group_name, owner_name, app_name, unprovisioned_only=None, udids=None) -> web.Response:
    """devices_list_csv_format

    Returns all devices associated with the given distribution group.

    :param distribution_group_name: The name of the distribution group.
    :type distribution_group_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param unprovisioned_only: when true, filters out provisioned devices
    :type unprovisioned_only: bool
    :param udids: multiple UDIDs which should be part of the resulting CSV.
    :type udids: List[str]

    """
    return web.Response(status=200)


async def devices_register_user_for_device(request: web.Request, user_id, body) -> web.Response:
    """devices_register_user_for_device

    Registers a user for an existing device

    :param user_id: The ID of the user
    :type user_id: str
    :param body: The device info.
    :type body: dict | bytes

    """
    body = DevicesRegisterUserForDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def devices_remove_user_device(request: web.Request, device_udid) -> web.Response:
    """devices_remove_user_device

    Removes an existing device from a user

    :param device_udid: The UDID of the device
    :type device_udid: str

    """
    return web.Response(status=200)


async def devices_user_devices_list(request: web.Request, ) -> web.Response:
    """devices_user_devices_list

    Returns all devices associated with the given user.


    """
    return web.Response(status=200)


async def distibution_releases_install_analytics(request: web.Request, owner_name, app_name, body) -> web.Response:
    """distibution_releases_install_analytics

    Notify download(s) for the provided distribution release(s).

    :param owner_name: The name of the app owner
    :type owner_name: str
    :param app_name: The name of the app
    :type app_name: str
    :param body: The install analytics request payload
    :type body: dict | bytes

    """
    body = DistibutionReleasesInstallAnalyticsRequest.from_dict(body)
    return web.Response(status=200)


async def provisioning_profile(request: web.Request, release_id, owner_name, app_name) -> web.Response:
    """provisioning_profile

    Return information about the provisioning profile. Only available for iOS.

    :param release_id: The release_id
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_add_distribution_group(request: web.Request, release_id, owner_name, app_name, body) -> web.Response:
    """releases_add_distribution_group

    Distributes a release to a group

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release information.
    :type body: dict | bytes

    """
    body = ReleasesAddDistributionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def releases_add_store(request: web.Request, release_id, owner_name, app_name, body) -> web.Response:
    """releases_add_store

    Distributes a release to a store

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release information.
    :type body: dict | bytes

    """
    body = ReleasesAddStoreRequest.from_dict(body)
    return web.Response(status=200)


async def releases_add_testers(request: web.Request, release_id, owner_name, app_name, body) -> web.Response:
    """releases_add_testers

    Distributes a release to a user

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release information.
    :type body: dict | bytes

    """
    body = ReleasesAddTestersRequest.from_dict(body)
    return web.Response(status=200)


async def releases_available_to_tester(request: web.Request, owner_name, app_name, published_only=None) -> web.Response:
    """releases_available_to_tester

    Return detailed information about releases avaiable to a tester.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param published_only: when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
    :type published_only: bool

    """
    return web.Response(status=200)


async def releases_create_release_upload(request: web.Request, owner_name, app_name, body=None) -> web.Response:
    """releases_create_release_upload

    Initiate a new release upload. This API is part of multi-step upload process.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Optional parameters to create releases with user defined metadata
    :type body: dict | bytes

    """
    body = ReleasesCreateReleaseUploadRequest.from_dict(body)
    return web.Response(status=200)


async def releases_delete(request: web.Request, release_id, owner_name, app_name) -> web.Response:
    """releases_delete

    Deletes a release.

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_delete_distribution_group(request: web.Request, release_id, group_id, owner_name, app_name) -> web.Response:
    """releases_delete_distribution_group

    Delete the given distribution group from the release

    :param release_id: The ID of the release
    :type release_id: int
    :param group_id: The id of the distribution group
    :type group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_delete_distribution_store(request: web.Request, release_id, store_id, owner_name, app_name) -> web.Response:
    """releases_delete_distribution_store

    Delete the given distribution store from the release

    :param release_id: The ID of the release
    :type release_id: int
    :param store_id: The id of the distribution store
    :type store_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_delete_distribution_tester(request: web.Request, release_id, tester_id, owner_name, app_name) -> web.Response:
    """releases_delete_distribution_tester

    Delete the given tester from the release

    :param release_id: The ID of the release
    :type release_id: int
    :param tester_id: The id of the tester
    :type tester_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_delete_tester_from_destinations(request: web.Request, tester_id, owner_name, app_name) -> web.Response:
    """releases_delete_tester_from_destinations

    Delete the given tester from the all releases

    :param tester_id: The id of the tester
    :type tester_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_delete_with_distribution_group_id(request: web.Request, owner_name, app_name, distribution_group_name, release_id) -> web.Response:
    """releases_delete_with_distribution_group_id

    Deletes a release with id &#39;release_id&#39; in a given distribution group.

    :param owner_name: The name of the app owner
    :type owner_name: str
    :param app_name: The name of the app
    :type app_name: str
    :param distribution_group_name: The name of the distribution group.
    :type distribution_group_name: str
    :param release_id: The ID identifying the unique release.
    :type release_id: int

    """
    return web.Response(status=200)


async def releases_get_ios_manifest(request: web.Request, app_id, release_id, token) -> web.Response:
    """releases_get_ios_manifest

    Returns the manifest.plist in XML format for installing the release on a device. Only available for iOS.

    :param app_id: The ID of the application
    :type app_id: str
    :param release_id: The release_id
    :type release_id: int
    :param token: A hash that authorizes the download if it matches the release info.
    :type token: str

    """
    return web.Response(status=200)


async def releases_get_latest_by_distribution_group(request: web.Request, owner_name, app_name, distribution_group_name, release_id, is_install_page=None) -> web.Response:
    """releases_get_latest_by_distribution_group

    Return detailed information about a distributed release in a given distribution group.

    :param owner_name: The name of the app owner
    :type owner_name: str
    :param app_name: The name of the app
    :type app_name: str
    :param distribution_group_name: The name of the distribution group.
    :type distribution_group_name: str
    :param release_id: Also supports the constant &#x60;latest&#x60;, which will return the latest release in the distribution group.
    :type release_id: str
    :param is_install_page: The check if the request is from Install page
    :type is_install_page: bool

    """
    return web.Response(status=200)


async def releases_get_latest_by_hash(request: web.Request, app_secret, release_hash, udid=None) -> web.Response:
    """releases_get_latest_by_hash

    If &#39;latest&#39; is not specified then it will return the specified release if it&#39;s enabled. If &#39;latest&#39; is specified, regardless of whether a release hash is provided, the latest enabled release is returned.

    :param app_secret: The secret of the target application
    :type app_secret: str
    :param release_hash: The hash of the release or &#39;latest&#39; to get the latest release from all the distribution groups assigned to the current user.
    :type release_hash: str
    :param udid: When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
    :type udid: str

    """
    return web.Response(status=200)


async def releases_get_latest_by_public_distribution_group(request: web.Request, app_secret, distribution_group_id, is_install_page=None) -> web.Response:
    """releases_get_latest_by_public_distribution_group

    Get a release with &#39;latest&#39; for the given public group.

    :param app_secret: The secret of the target application
    :type app_secret: str
    :param distribution_group_id: the id for destination
    :type distribution_group_id: str
    :param is_install_page: The check if the request is from Install page
    :type is_install_page: bool

    """
    return web.Response(status=200)


async def releases_get_latest_by_user(request: web.Request, release_id, owner_name, app_name, udid=None, is_install_page=None) -> web.Response:
    """releases_get_latest_by_user

    Get a release with id &#x60;release_id&#x60;. If &#x60;release_id&#x60; is &#x60;latest&#x60;, return the latest release that was distributed to the current user (from all the distribution groups).

    :param release_id: The ID of the release, or &#x60;latest&#x60; to get the latest release from all the distribution groups assigned to the current user.
    :type release_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param udid: when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned.
    :type udid: str
    :param is_install_page: The check if the request is from Install page
    :type is_install_page: bool

    """
    return web.Response(status=200)


async def releases_get_latest_private_release(request: web.Request, app_secret, udid=None) -> web.Response:
    """releases_get_latest_private_release

    Get the latest release distributed to a private group the given user is a member of for the given app.

    :param app_secret: The secret of the target application
    :type app_secret: str
    :param udid: When passing &#x60;udid&#x60; in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms.
    :type udid: str

    """
    return web.Response(status=200)


async def releases_get_latest_public_release(request: web.Request, app_secret) -> web.Response:
    """releases_get_latest_public_release

    Get the latest public release for the given app.

    :param app_secret: The secret of the target application
    :type app_secret: str

    """
    return web.Response(status=200)


async def releases_get_public_groups_for_release_by_hash(request: web.Request, app_secret, release_hash) -> web.Response:
    """releases_get_public_groups_for_release_by_hash

    Get all public distribution groups that a given release has been distributed to

    :param app_secret: The secret of the target application
    :type app_secret: str
    :param release_hash: The hash of the release
    :type release_hash: str

    """
    return web.Response(status=200)


async def releases_get_release_upload_status(request: web.Request, upload_id, owner_name, app_name) -> web.Response:
    """releases_get_release_upload_status

    Get the current status of the release upload.

    :param upload_id: The ID of the release upload
    :type upload_id: str
    :type upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_get_sparkle_feed(request: web.Request, app_secret) -> web.Response:
    """releases_get_sparkle_feed

    Gets the sparkle feed of the releases that are distributed to all the public distribution groups.

    :param app_secret: The secret of the application.
    :type app_secret: str

    """
    return web.Response(status=200)


async def releases_list(request: web.Request, owner_name, app_name, published_only=None, scope=None, top=None, release_id=None) -> web.Response:
    """releases_list

    Return basic information about releases.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param published_only: When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out.
    :type published_only: bool
    :param scope: When the scope is &#39;tester&#39;, only includes releases that have been distributed to groups that the user belongs to.
    :type scope: str
    :param top: The number of releases to return
    :type top: 
    :param release_id: The id of a release
    :type release_id: 

    """
    return web.Response(status=200)


async def releases_list_by_distribution_group(request: web.Request, distribution_group_name, owner_name, app_name) -> web.Response:
    """releases_list_by_distribution_group

    Return basic information about distributed releases in a given distribution group.

    :param distribution_group_name: The name of the distribution group.
    :type distribution_group_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_list_latest(request: web.Request, owner_name, app_name) -> web.Response:
    """releases_list_latest

    Get the latest release from every distribution group associated with an application.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def releases_put_distribution_group(request: web.Request, release_id, group_id, owner_name, app_name, body=None) -> web.Response:
    """releases_put_distribution_group

    Update details about the specified distribution group associated with the release

    :param release_id: The ID of the release
    :type release_id: int
    :param group_id: The id of the releases destination
    :type group_id: str
    :type group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReleasesPutDistributionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def releases_put_distribution_tester(request: web.Request, release_id, tester_id, owner_name, app_name, body=None) -> web.Response:
    """releases_put_distribution_tester

    Update details about the specified tester associated with the release

    :param release_id: The ID of the release
    :type release_id: int
    :param tester_id: The id of the tester
    :type tester_id: str
    :type tester_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReleasesPutDistributionGroupRequest.from_dict(body)
    return web.Response(status=200)


async def releases_update(request: web.Request, release_id, owner_name, app_name, body) -> web.Response:
    """releases_update

    Updates a release.

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release information.
    :type body: dict | bytes

    """
    body = ReleasesUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def releases_update_details(request: web.Request, release_id, owner_name, app_name, body) -> web.Response:
    """releases_update_details

    Update details of a release.

    :param release_id: The ID of the release
    :type release_id: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release information.
    :type body: dict | bytes

    """
    body = ReleasesUpdateDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def releases_update_release_upload_status(request: web.Request, upload_id, owner_name, app_name, body, extract=None) -> web.Response:
    """releases_update_release_upload_status

    Update the current status of the release upload.

    :param upload_id: The ID of the release upload
    :type upload_id: str
    :type upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The release upload status information.
    :type body: dict | bytes
    :param extract: A flag that indicates to extract release or not, true by default
    :type extract: bool

    """
    body = ReleasesUpdateReleaseUploadStatusRequest.from_dict(body)
    return web.Response(status=200)


async def store_notifications_get_notification_by_app_id(request: web.Request, owner_name, app_name) -> web.Response:
    """store_notifications_get_notification_by_app_id

    Application specific store service status

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_release_publish_logs_get(request: web.Request, store_name, release_id, owner_name, app_name) -> web.Response:
    """store_release_publish_logs_get

    Returns publish logs for a particular release published to a particular store

    :param store_name: The name of the store
    :type store_name: str
    :param release_id: The ID of the realease
    :type release_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_releases_delete(request: web.Request, store_name, release_id, owner_name, app_name, body=None) -> web.Response:
    """store_releases_delete

    delete the release with release Id

    :param store_name: The name of the store
    :type store_name: str
    :param release_id: The id of the release
    :type release_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def store_releases_get(request: web.Request, store_name, release_id, owner_name, app_name) -> web.Response:
    """store_releases_get

    Return releases published in a store for releaseId and storeId

    :param store_name: The name of the store
    :type store_name: str
    :param release_id: The name of the store
    :type release_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_releases_get_latest(request: web.Request, store_name, owner_name, app_name) -> web.Response:
    """store_releases_get_latest

    Returns the latest release published in a store.

    :param store_name: The name of the store
    :type store_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_releases_get_publish_error(request: web.Request, store_name, release_id, owner_name, app_name) -> web.Response:
    """store_releases_get_publish_error

    Return the Error Details of release which failed in publishing.

    :param store_name: The name of the store
    :type store_name: str
    :param release_id: The id of the release
    :type release_id: 
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_releases_get_real_time_status_by_release_id(request: web.Request, store_name, release_id, owner_name, app_name) -> web.Response:
    """store_releases_get_real_time_status_by_release_id

    Return the Real time Status publishing of release from store.

    :param store_name: The name of the store
    :type store_name: str
    :param release_id: The id of the release
    :type release_id: 
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def store_releases_list(request: web.Request, store_name, owner_name, app_name) -> web.Response:
    """store_releases_list

    Return all releases published  in a store

    :param store_name: The name of the store
    :type store_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def stores_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """stores_create

    Create a new external store for the specified application.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The store request
    :type body: dict | bytes

    """
    body = StoresCreateRequest.from_dict(body)
    return web.Response(status=200)


async def stores_delete(request: web.Request, store_name, owner_name, app_name, body=None) -> web.Response:
    """stores_delete

    delete the store based on specific store name.

    :param store_name: The name of the store
    :type store_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def stores_get(request: web.Request, store_name, owner_name, app_name) -> web.Response:
    """stores_get

    Return the store details for specified store name.

    :param store_name: The name of the store
    :type store_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def stores_list(request: web.Request, owner_name, app_name) -> web.Response:
    """stores_list

    Get all the store details from Storage store table for a particular application.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def stores_patch(request: web.Request, store_name, owner_name, app_name, body) -> web.Response:
    """stores_patch

    Update the store.

    :param store_name: The name of the store
    :type store_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Store update request
    :type body: dict | bytes

    """
    body = StoresPatchRequest.from_dict(body)
    return web.Response(status=200)
