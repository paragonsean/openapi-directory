from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_configuration import ManagedConfiguration
from openapi_server.models.managed_configurations_for_device_list_response import ManagedConfigurationsForDeviceListResponse
from openapi_server import util


async def androidenterprise_managedconfigurationsfordevice_delete(request: web.Request, enterprise_id, user_id, device_id, managed_configuration_for_device_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidenterprise_managedconfigurationsfordevice_delete

    Removes a per-device managed configuration for an app for the specified device.

    :param enterprise_id: The ID of the enterprise.
    :type enterprise_id: str
    :param user_id: The ID of the user.
    :type user_id: str
    :param device_id: The Android ID of the device.
    :type device_id: str
    :param managed_configuration_for_device_id: The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;.
    :type managed_configuration_for_device_id: str
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

    """
    return web.Response(status=200)


async def androidenterprise_managedconfigurationsfordevice_get(request: web.Request, enterprise_id, user_id, device_id, managed_configuration_for_device_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidenterprise_managedconfigurationsfordevice_get

    Retrieves details of a per-device managed configuration.

    :param enterprise_id: The ID of the enterprise.
    :type enterprise_id: str
    :param user_id: The ID of the user.
    :type user_id: str
    :param device_id: The Android ID of the device.
    :type device_id: str
    :param managed_configuration_for_device_id: The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;.
    :type managed_configuration_for_device_id: str
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

    """
    return web.Response(status=200)


async def androidenterprise_managedconfigurationsfordevice_list(request: web.Request, enterprise_id, user_id, device_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidenterprise_managedconfigurationsfordevice_list

    Lists all the per-device managed configurations for the specified device. Only the ID is set.

    :param enterprise_id: The ID of the enterprise.
    :type enterprise_id: str
    :param user_id: The ID of the user.
    :type user_id: str
    :param device_id: The Android ID of the device.
    :type device_id: str
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

    """
    return web.Response(status=200)


async def androidenterprise_managedconfigurationsfordevice_update(request: web.Request, enterprise_id, user_id, device_id, managed_configuration_for_device_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidenterprise_managedconfigurationsfordevice_update

    Adds or updates a per-device managed configuration for an app for the specified device.

    :param enterprise_id: The ID of the enterprise.
    :type enterprise_id: str
    :param user_id: The ID of the user.
    :type user_id: str
    :param device_id: The Android ID of the device.
    :type device_id: str
    :param managed_configuration_for_device_id: The ID of the managed configuration (a product ID), e.g. \&quot;app:com.google.android.gm\&quot;.
    :type managed_configuration_for_device_id: str
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
    body = ManagedConfiguration.from_dict(body)
    return web.Response(status=200)
