from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_apps_cloudidentity_devices_v1_approve_device_user_request import GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest
from openapi_server.models.google_apps_cloudidentity_devices_v1_block_device_user_request import GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest
from openapi_server.models.google_apps_cloudidentity_devices_v1_cancel_wipe_device_user_request import GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest
from openapi_server.models.google_apps_cloudidentity_devices_v1_device import GoogleAppsCloudidentityDevicesV1Device
from openapi_server.models.google_apps_cloudidentity_devices_v1_list_client_states_response import GoogleAppsCloudidentityDevicesV1ListClientStatesResponse
from openapi_server.models.google_apps_cloudidentity_devices_v1_list_device_users_response import GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse
from openapi_server.models.google_apps_cloudidentity_devices_v1_list_devices_response import GoogleAppsCloudidentityDevicesV1ListDevicesResponse
from openapi_server.models.google_apps_cloudidentity_devices_v1_lookup_self_device_users_response import GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse
from openapi_server.models.google_apps_cloudidentity_devices_v1_wipe_device_user_request import GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudidentity_devices_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, body=None) -> web.Response:
    """cloudidentity_devices_create

    Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer: Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs.
    :type customer: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsCloudidentityDevicesV1Device.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_devices_device_users_approve(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_devices_device_users_approve

    Approves device to access user data.

    :param name: Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_devices_device_users_block(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_devices_device_users_block

    Blocks device from accessing user data

    :param name: Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_devices_device_users_cancel_wipe(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_devices_device_users_cancel_wipe

    Cancels an unfinished user account wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped.

    :param name: Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_devices_device_users_client_states_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, filter=None, order_by=None, page_token=None) -> web.Response:
    """cloudidentity_devices_device_users_client_states_list

    Lists the client states for the given search query.

    :param parent: Required. To list all ClientStates, set this to \&quot;devices/-/deviceUsers/-\&quot;. To list all ClientStates owned by a DeviceUser, set this to the resource name of the DeviceUser. Format: devices/{device}/deviceUsers/{deviceUser}
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer: Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs.
    :type customer: str
    :param filter: Optional. Additional restrictions when fetching list of client states.
    :type filter: str
    :param order_by: Optional. Order specification for client states in the response.
    :type order_by: str
    :param page_token: Optional. A page token, received from a previous &#x60;ListClientStates&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListClientStates&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_devices_device_users_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_devices_device_users_list

    Lists/Searches DeviceUsers.

    :param parent: Required. To list all DeviceUsers, set this to \&quot;devices/-\&quot;. To list all DeviceUsers owned by a device, set this to the resource name of the device. Format: devices/{device}
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer: Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs.
    :type customer: str
    :param filter: Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character.
    :type filter: str
    :param order_by: Optional. Order specification for devices in the response.
    :type order_by: str
    :param page_size: Optional. The maximum number of DeviceUsers to return. If unspecified, at most 5 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListDeviceUsers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBooks&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_devices_device_users_lookup(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, android_id=None, page_size=None, page_token=None, raw_resource_id=None, user_id=None) -> web.Response:
    """cloudidentity_devices_device_users_lookup

    Looks up resource names of the DeviceUsers associated with the caller&#39;s credentials, as well as the properties provided in the request. This method must be called with end-user credentials with the scope: https://www.googleapis.com/auth/cloud-identity.devices.lookup If multiple properties are provided, only DeviceUsers having all of these properties are considered as matches - i.e. the query behaves like an AND. Different platforms require different amounts of information from the caller to ensure that the DeviceUser is uniquely identified. - iOS: No properties need to be passed, the caller&#39;s credentials are sufficient to identify the corresponding DeviceUser. - Android: Specifying the &#39;android_id&#39; field is required. - Desktop: Specifying the &#39;raw_resource_id&#39; field is required.

    :param parent: Must be set to \&quot;devices/-/deviceUsers\&quot; to search across all DeviceUser belonging to the user.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param android_id: Android Id returned by [Settings.Secure#ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID).
    :type android_id: str
    :param page_size: The maximum number of DeviceUsers to return. If unspecified, at most 20 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;LookupDeviceUsers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;LookupDeviceUsers&#x60; must match the call that provided the page token.
    :type page_token: str
    :param raw_resource_id: Raw Resource Id used by Google Endpoint Verification. If the user is enrolled into Google Endpoint Verification, this id will be saved as the &#39;device_resource_id&#39; field in the following platform dependent files. * macOS: ~/.secureConnect/context_aware_config.json * Windows: %USERPROFILE%\\AppData\\Local\\Google\\Endpoint Verification\\accounts.json * Linux: ~/.secureConnect/context_aware_config.json
    :type raw_resource_id: str
    :param user_id: The user whose DeviceUser&#39;s resource name will be fetched. Must be set to &#39;me&#39; to fetch the DeviceUser&#39;s resource name for the calling user.
    :type user_id: str

    """
    return web.Response(status=200)


async def cloudidentity_devices_device_users_wipe(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_devices_device_users_wipe

    Wipes the user&#39;s account on a device. Other data on the device that is not associated with the user&#39;s work account is not affected. For example, if a Gmail app is installed on a device that is used for personal and work purposes, and the user is logged in to the Gmail app with their personal account as well as their work account, wiping the \&quot;deviceUser\&quot; by their work administrator will not affect their personal account within Gmail or other apps such as Photos.

    :param name: Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_devices_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, filter=None, order_by=None, page_size=None, page_token=None, view=None) -> web.Response:
    """cloudidentity_devices_list

    Lists/Searches devices.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param customer: Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer in the format: &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60;. If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs.
    :type customer: str
    :param filter: Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character.
    :type filter: str
    :param order_by: Optional. Order specification for devices in the response. Only one of the following field names may be used to specify the order: &#x60;create_time&#x60;, &#x60;last_sync_time&#x60;, &#x60;model&#x60;, &#x60;os_version&#x60;, &#x60;device_type&#x60; and &#x60;serial_number&#x60;. &#x60;desc&#x60; may be specified optionally at the end to specify results to be sorted in descending order. Default order is ascending.
    :type order_by: str
    :param page_size: Optional. The maximum number of Devices to return. If unspecified, at most 20 Devices will be returned. The maximum value is 100; values above 100 will be coerced to 100.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListDevices&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListDevices&#x60; must match the call that provided the page token.
    :type page_token: str
    :param view: Optional. The view to use for the List request.
    :type view: str

    """
    return web.Response(status=200)
