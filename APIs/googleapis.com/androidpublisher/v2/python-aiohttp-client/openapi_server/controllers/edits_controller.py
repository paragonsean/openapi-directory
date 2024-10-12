from typing import List, Dict
from aiohttp import web

from openapi_server.models.apk import Apk
from openapi_server.models.apk_listing import ApkListing
from openapi_server.models.apk_listings_list_response import ApkListingsListResponse
from openapi_server.models.apks_add_externally_hosted_request import ApksAddExternallyHostedRequest
from openapi_server.models.apks_add_externally_hosted_response import ApksAddExternallyHostedResponse
from openapi_server.models.apks_list_response import ApksListResponse
from openapi_server.models.app_details import AppDetails
from openapi_server.models.app_edit import AppEdit
from openapi_server.models.bundle import Bundle
from openapi_server.models.bundles_list_response import BundlesListResponse
from openapi_server.models.deobfuscation_files_upload_response import DeobfuscationFilesUploadResponse
from openapi_server.models.expansion_file import ExpansionFile
from openapi_server.models.expansion_files_upload_response import ExpansionFilesUploadResponse
from openapi_server.models.images_delete_all_response import ImagesDeleteAllResponse
from openapi_server.models.images_list_response import ImagesListResponse
from openapi_server.models.images_upload_response import ImagesUploadResponse
from openapi_server.models.listing import Listing
from openapi_server.models.listings_list_response import ListingsListResponse
from openapi_server.models.testers import Testers
from openapi_server.models.track import Track
from openapi_server.models.tracks_list_response import TracksListResponse
from openapi_server import util


async def androidpublisher_edits_apklistings_delete(request: web.Request, package_name, edit_id, apk_version_code, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apklistings_delete

    Deletes the APK-specific localized listing for a specified APK and language code.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
    :param language: The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_apklistings_deleteall(request: web.Request, package_name, edit_id, apk_version_code, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apklistings_deleteall

    Deletes all the APK-specific localized listings for a specified APK.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_apklistings_get(request: web.Request, package_name, edit_id, apk_version_code, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apklistings_get

    Fetches the APK-specific localized listing for a specified APK and language code.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
    :param language: The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_apklistings_list(request: web.Request, package_name, edit_id, apk_version_code, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apklistings_list

    Lists all the APK-specific localized listings for a specified APK.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_apklistings_patch(request: web.Request, package_name, edit_id, apk_version_code, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_apklistings_patch

    Updates or creates the APK-specific localized listing for a specified APK and language code. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
    :param language: The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApkListing.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_apklistings_update(request: web.Request, package_name, edit_id, apk_version_code, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_apklistings_update

    Updates or creates the APK-specific localized listing for a specified APK and language code.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The APK version code whose APK-specific listings should be read or modified.
    :type apk_version_code: int
    :param language: The language code (a BCP-47 language tag) of the APK-specific localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApkListing.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_apks_addexternallyhosted(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_apks_addexternallyhosted

    Creates a new APK without uploading the APK itself to Google Play, instead hosting the APK at a specified URL. This function is only available to enterprises using Google Play for Work whose application is configured to restrict distribution to the enterprise domain.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApksAddExternallyHostedRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_apks_list(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apks_list

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_apks_upload(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_apks_upload

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_bundles_list(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_bundles_list

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_bundles_upload(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, ack_bundle_installation_warning=None) -> web.Response:
    """androidpublisher_edits_bundles_upload

    Uploads a new Android App Bundle to this edit. If you are using the Google API client libraries, please increase the timeout of the http request before calling this endpoint (a timeout of 2 minutes is recommended). See: https://developers.google.com/api-client-library/java/google-api-java-client/errors for an example in java.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param ack_bundle_installation_warning: Must be set to true if the bundle installation may trigger a warning on user devices (for example, if installation size may be over a threshold, typically 100 MB).
    :type ack_bundle_installation_warning: bool

    """
    return web.Response(status=200)


async def androidpublisher_edits_commit(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_commit

    Commits/applies the changes made in this edit back to the app.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_delete(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_delete

    Deletes an edit for an app. Creating a new edit will automatically delete any of your previous edits so this method need only be called if you want to preemptively abandon an edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_deobfuscationfiles_upload(request: web.Request, package_name, edit_id, apk_version_code, deobfuscation_file_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_deobfuscationfiles_upload

    Uploads the deobfuscation file of the specified APK. If a deobfuscation or symbolication file already exists, it will be replaced. See https://developer.android.com/studio/build/shrink-code to learn more about deobfuscation files.

    :param package_name: Unique identifier of the Android app for which the deobfuscation files are being uploaded; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The version code of the APK whose deobfuscation file is being uploaded.
    :type apk_version_code: int
    :param deobfuscation_file_type: 
    :type deobfuscation_file_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_details_get(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_details_get

    Fetches app details for this edit. This includes the default language and developer support contact information.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_details_patch(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_details_patch

    Updates app details for this edit. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppDetails.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_details_update(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_details_update

    Updates app details for this edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppDetails.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_expansionfiles_get(request: web.Request, package_name, edit_id, apk_version_code, expansion_file_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_expansionfiles_get

    Fetches the Expansion File configuration for the APK specified.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The version code of the APK whose Expansion File configuration is being read or modified.
    :type apk_version_code: int
    :param expansion_file_type: 
    :type expansion_file_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_expansionfiles_patch(request: web.Request, package_name, edit_id, apk_version_code, expansion_file_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_expansionfiles_patch

    Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The version code of the APK whose Expansion File configuration is being read or modified.
    :type apk_version_code: int
    :param expansion_file_type: 
    :type expansion_file_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExpansionFile.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_expansionfiles_update(request: web.Request, package_name, edit_id, apk_version_code, expansion_file_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_expansionfiles_update

    Updates the APK&#39;s Expansion File configuration to reference another APK&#39;s Expansion Files. To add a new Expansion File use the Upload method.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The version code of the APK whose Expansion File configuration is being read or modified.
    :type apk_version_code: int
    :param expansion_file_type: 
    :type expansion_file_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExpansionFile.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_expansionfiles_upload(request: web.Request, package_name, edit_id, apk_version_code, expansion_file_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_expansionfiles_upload

    Uploads and attaches a new Expansion File to the APK specified.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param apk_version_code: The version code of the APK whose Expansion File configuration is being read or modified.
    :type apk_version_code: int
    :param expansion_file_type: 
    :type expansion_file_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_get(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_get

    Returns information about the edit specified. Calls will fail if the edit is no long active (e.g. has been deleted, superseded or expired).

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_images_delete(request: web.Request, package_name, edit_id, language, image_type, image_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_images_delete

    Deletes the image (specified by id) from the edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
    :param image_type: 
    :type image_type: str
    :param image_id: Unique identifier an image within the set of images attached to this edit.
    :type image_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_images_deleteall(request: web.Request, package_name, edit_id, language, image_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_images_deleteall

    Deletes all images for the specified language and image type.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
    :param image_type: 
    :type image_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_images_list(request: web.Request, package_name, edit_id, language, image_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_images_list

    Lists all images for the specified language and image type.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
    :param image_type: 
    :type image_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_images_upload(request: web.Request, package_name, edit_id, language, image_type, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_images_upload

    Uploads a new image and adds it to the list of images for the specified language and image type.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing whose images are to read or modified. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
    :param image_type: 
    :type image_type: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_insert(request: web.Request, package_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_insert

    Creates a new edit for an app, populated with the app&#39;s current state.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppEdit.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_listings_delete(request: web.Request, package_name, edit_id, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_listings_delete

    Deletes the specified localized store listing from an edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_listings_deleteall(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_listings_deleteall

    Deletes all localized listings from an edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_listings_get(request: web.Request, package_name, edit_id, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_listings_get

    Fetches information about a localized store listing.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_listings_list(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_listings_list

    Returns all of the localized store listings attached to this edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_listings_patch(request: web.Request, package_name, edit_id, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_listings_patch

    Creates or updates a localized store listing. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Listing.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_listings_update(request: web.Request, package_name, edit_id, language, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_listings_update

    Creates or updates a localized store listing.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param language: The language code (a BCP-47 language tag) of the localized listing to read or modify. For example, to select Austrian German, pass \&quot;de-AT\&quot;.
    :type language: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Listing.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_testers_get(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_testers_get

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_testers_patch(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_testers_patch

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Testers.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_testers_update(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_testers_update

    

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Testers.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_tracks_get(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_tracks_get

    Fetches the track configuration for the specified track type. Includes the APK version codes that are in this track.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_tracks_list(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_tracks_list

    Lists all the track configurations for this edit.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def androidpublisher_edits_tracks_patch(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_tracks_patch

    Updates the track configuration for the specified track type. This method supports patch semantics.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Track.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_tracks_update(request: web.Request, package_name, edit_id, track, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """androidpublisher_edits_tracks_update

    Updates the track configuration for the specified track type.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
    :param track: The track to read or modify.
    :type track: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Track.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_edits_validate(request: web.Request, package_name, edit_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """androidpublisher_edits_validate

    Checks that the edit can be successfully committed. The edit&#39;s changes are not applied to the live app.

    :param package_name: Unique identifier for the Android app that is being updated; for example, \&quot;com.spiffygame\&quot;.
    :type package_name: str
    :param edit_id: Unique identifier for this edit.
    :type edit_id: str
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
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)
