from typing import List, Dict
from aiohttp import web

from openapi_server.models.hmac_key import HmacKey
from openapi_server.models.hmac_key_metadata import HmacKeyMetadata
from openapi_server.models.hmac_keys_metadata import HmacKeysMetadata
from openapi_server.models.service_account import ServiceAccount
from openapi_server import util


async def storage_projects_hmac_keys_create(request: web.Request, project_id, service_account_email, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_projects_hmac_keys_create

    Creates a new HMAC key for the specified service account.

    :param project_id: Project ID owning the service account.
    :type project_id: str
    :param service_account_email: Email address of the service account.
    :type service_account_email: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_projects_hmac_keys_delete(request: web.Request, project_id, access_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_projects_hmac_keys_delete

    Deletes an HMAC key.

    :param project_id: Project ID owning the requested key
    :type project_id: str
    :param access_id: Name of the HMAC key to be deleted.
    :type access_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_projects_hmac_keys_get(request: web.Request, project_id, access_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_projects_hmac_keys_get

    Retrieves an HMAC key&#39;s metadata

    :param project_id: Project ID owning the service account of the requested key.
    :type project_id: str
    :param access_id: Name of the HMAC key.
    :type access_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_projects_hmac_keys_list(request: web.Request, project_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, max_results=None, page_token=None, service_account_email=None, show_deleted_keys=None, user_project=None) -> web.Response:
    """storage_projects_hmac_keys_list

    Retrieves a list of HMAC keys matching the criteria.

    :param project_id: Name of the project in which to look for HMAC keys.
    :type project_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum number of items to return in a single page of responses. The service uses this parameter or 250 items, whichever is smaller. The max number of items per page will also be limited by the number of distinct service accounts in the response. If the number of service accounts in a single response is too high, the page will truncated and a next page token will be returned.
    :type max_results: int
    :param page_token: A previously-returned page token representing part of the larger set of results to view.
    :type page_token: str
    :param service_account_email: If present, only keys for the given service account are returned.
    :type service_account_email: str
    :param show_deleted_keys: Whether or not to show keys in the DELETED state.
    :type show_deleted_keys: bool
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)


async def storage_projects_hmac_keys_update(request: web.Request, project_id, access_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None, body=None) -> web.Response:
    """storage_projects_hmac_keys_update

    Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states.

    :param project_id: Project ID owning the service account of the updated key.
    :type project_id: str
    :param access_id: Name of the HMAC key being updated.
    :type access_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param user_project: The project to be billed for this request.
    :type user_project: str
    :param body: 
    :type body: dict | bytes

    """
    body = HmacKeyMetadata.from_dict(body)
    return web.Response(status=200)


async def storage_projects_service_account_get(request: web.Request, project_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_type=None, user_ip=None, user_project=None) -> web.Response:
    """storage_projects_service_account_get

    Get the email address of this project&#39;s Google Cloud Storage service account.

    :param project_id: Project ID
    :type project_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param upload_type: Upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;, \&quot;resumable\&quot;).
    :type upload_type: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param user_project: The project to be billed for this request.
    :type user_project: str

    """
    return web.Response(status=200)
