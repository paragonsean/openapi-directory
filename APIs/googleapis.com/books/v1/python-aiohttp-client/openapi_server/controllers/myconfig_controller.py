from typing import List, Dict
from aiohttp import web

from openapi_server.models.download_accesses import DownloadAccesses
from openapi_server.models.request_access_data import RequestAccessData
from openapi_server.models.usersettings import Usersettings
from openapi_server.models.volumes import Volumes
from openapi_server import util


async def books_myconfig_get_user_settings(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, country=None) -> web.Response:
    """books_myconfig_get_user_settings

    Gets the current settings for the user.

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
    :param country: Unused. Added only to workaround TEX mandatory request template requirement
    :type country: str

    """
    return web.Response(status=200)


async def books_myconfig_release_download_access(request: web.Request, cpksver, volume_ids, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, locale=None, source=None) -> web.Response:
    """books_myconfig_release_download_access

    Release downloaded content access restriction.

    :param cpksver: The device/version ID from which to release the restriction.
    :type cpksver: str
    :param volume_ids: The volume(s) to release restrictions for.
    :type volume_ids: List[str]
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
    :param locale: ISO-639-1, ISO-3166-1 codes for message localization, i.e. en_US.
    :type locale: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_myconfig_request_access(request: web.Request, cpksver, nonce, source, volume_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, license_types=None, locale=None) -> web.Response:
    """books_myconfig_request_access

    Request concurrent and download access restrictions.

    :param cpksver: The device/version ID from which to request the restrictions.
    :type cpksver: str
    :param nonce: The client nonce value.
    :type nonce: str
    :param source: String to identify the originator of this request.
    :type source: str
    :param volume_id: The volume to request concurrent/download restrictions for.
    :type volume_id: str
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
    :param license_types: The type of access license to request. If not specified, the default is BOTH.
    :type license_types: str
    :param locale: ISO-639-1, ISO-3166-1 codes for message localization, i.e. en_US.
    :type locale: str

    """
    return web.Response(status=200)


async def books_myconfig_sync_volume_licenses(request: web.Request, cpksver, nonce, source, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, features=None, include_non_comics_series=None, locale=None, show_preorders=None, volume_ids=None) -> web.Response:
    """books_myconfig_sync_volume_licenses

    Request downloaded content access for specified volumes on the My eBooks shelf.

    :param cpksver: The device/version ID from which to release the restriction.
    :type cpksver: str
    :param nonce: The client nonce value.
    :type nonce: str
    :param source: String to identify the originator of this request.
    :type source: str
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
    :param features: List of features supported by the client, i.e., &#39;RENTALS&#39;
    :type features: List[str]
    :param include_non_comics_series: Set to true to include non-comics series. Defaults to false.
    :type include_non_comics_series: bool
    :param locale: ISO-639-1, ISO-3166-1 codes for message localization, i.e. en_US.
    :type locale: str
    :param show_preorders: Set to true to show pre-ordered books. Defaults to false.
    :type show_preorders: bool
    :param volume_ids: The volume(s) to request download restrictions for.
    :type volume_ids: List[str]

    """
    return web.Response(status=200)


async def books_myconfig_update_user_settings(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """books_myconfig_update_user_settings

    Sets the settings for the user. If a sub-object is specified, it will overwrite the existing sub-object stored in the server. Unspecified sub-objects will retain the existing value.

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
    body = Usersettings.from_dict(body)
    return web.Response(status=200)
