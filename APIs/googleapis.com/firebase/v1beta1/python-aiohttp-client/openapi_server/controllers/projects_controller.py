from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_firebase_request import AddFirebaseRequest
from openapi_server.models.add_google_analytics_request import AddGoogleAnalyticsRequest
from openapi_server.models.android_app import AndroidApp
from openapi_server.models.finalize_default_location_request import FinalizeDefaultLocationRequest
from openapi_server.models.ios_app import IosApp
from openapi_server.models.list_android_apps_response import ListAndroidAppsResponse
from openapi_server.models.list_available_locations_response import ListAvailableLocationsResponse
from openapi_server.models.list_firebase_projects_response import ListFirebaseProjectsResponse
from openapi_server.models.list_ios_apps_response import ListIosAppsResponse
from openapi_server.models.list_sha_certificates_response import ListShaCertificatesResponse
from openapi_server.models.list_web_apps_response import ListWebAppsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.remove_analytics_request import RemoveAnalyticsRequest
from openapi_server.models.remove_web_app_request import RemoveWebAppRequest
from openapi_server.models.search_firebase_apps_response import SearchFirebaseAppsResponse
from openapi_server.models.sha_certificate import ShaCertificate
from openapi_server.models.undelete_web_app_request import UndeleteWebAppRequest
from openapi_server.models.web_app import WebApp
from openapi_server.models.web_app_config import WebAppConfig
from openapi_server import util


async def firebase_projects_add_firebase(request: web.Request, project, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_add_firebase

    Adds Firebase resources to the specified existing [Google Cloud Platform (GCP) &#x60;Project&#x60;] (https://cloud.google.com/resource-manager/reference/rest/v1/projects). Since a FirebaseProject is actually also a GCP &#x60;Project&#x60;, a &#x60;FirebaseProject&#x60; has the same underlying GCP identifiers (&#x60;projectNumber&#x60; and &#x60;projectId&#x60;). This allows for easy interop with Google APIs. The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations). Poll the &#x60;Operation&#x60; to track the provisioning process by calling GetOperation until [&#x60;done&#x60;](../../v1beta1/operations#Operation.FIELDS.done) is &#x60;true&#x60;. When &#x60;done&#x60; is &#x60;true&#x60;, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) is set to a FirebaseProject; if the &#x60;Operation&#x60; failed, its [&#x60;error&#x60;](../../v1beta1/operations#Operation.FIELDS.error) is set to a google.rpc.Status. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call DeleteOperation. This method does not modify any billing account information on the underlying GCP &#x60;Project&#x60;. To call &#x60;AddFirebase&#x60;, a project member or service account must have the following permissions (the IAM roles of Editor and Owner contain these permissions): &#x60;firebase.projects.update&#x60;, &#x60;resourcemanager.projects.get&#x60;, &#x60;serviceusage.services.enable&#x60;, and &#x60;serviceusage.services.get&#x60;.

    :param project: The resource name of the GCP &#x60;Project&#x60; to which Firebase resources will be added, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. After calling &#x60;AddFirebase&#x60;, the unique Project identifiers ( [&#x60;projectNumber&#x60;](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_number) and [&#x60;projectId&#x60;](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_id)) of the underlying GCP &#x60;Project&#x60; are also the identifiers of the FirebaseProject.
    :type project: str
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
    body = AddFirebaseRequest.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_add_google_analytics(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_add_google_analytics

    Links the specified FirebaseProject with an existing [Google Analytics account](http://www.google.com/analytics/). Using this call, you can either: - Specify an &#x60;analyticsAccountId&#x60; to provision a new Google Analytics property within the specified account and associate the new property with the &#x60;FirebaseProject&#x60;. - Specify an existing &#x60;analyticsPropertyId&#x60; to associate the property with the &#x60;FirebaseProject&#x60;. Note that when you call &#x60;AddGoogleAnalytics&#x60;: 1. The first check determines if any existing data streams in the Google Analytics property correspond to any existing Firebase Apps in the &#x60;FirebaseProject&#x60; (based on the &#x60;packageName&#x60; or &#x60;bundleId&#x60; associated with the data stream). Then, as applicable, the data streams and apps are linked. Note that this auto-linking only applies to &#x60;AndroidApps&#x60; and &#x60;IosApps&#x60;. 2. If no corresponding data streams are found for the Firebase Apps, new data streams are provisioned in the Google Analytics property for each of the Firebase Apps. Note that a new data stream is always provisioned for a Web App even if it was previously associated with a data stream in the Analytics property. Learn more about the hierarchy and structure of Google Analytics accounts in the [Analytics documentation](https://support.google.com/analytics/answer/9303323). The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations). Poll the &#x60;Operation&#x60; to track the provisioning process by calling GetOperation until [&#x60;done&#x60;](../../v1beta1/operations#Operation.FIELDS.done) is &#x60;true&#x60;. When &#x60;done&#x60; is &#x60;true&#x60;, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) is set to an AnalyticsDetails; if the &#x60;Operation&#x60; failed, its [&#x60;error&#x60;](../../v1beta1/operations#Operation.FIELDS.error) is set to a google.rpc.Status. To call &#x60;AddGoogleAnalytics&#x60;, a project member must be an Owner for the existing &#x60;FirebaseProject&#x60; and have the [&#x60;Edit&#x60; permission](https://support.google.com/analytics/answer/2884495) for the Google Analytics account. If the &#x60;FirebaseProject&#x60; already has Google Analytics enabled, and you call &#x60;AddGoogleAnalytics&#x60; using an &#x60;analyticsPropertyId&#x60; that&#39;s different from the currently associated property, then the call will fail. Analytics may have already been enabled in the Firebase console or by specifying &#x60;timeZone&#x60; and &#x60;regionCode&#x60; in the call to [&#x60;AddFirebase&#x60;](../../v1beta1/projects/addFirebase).

    :param parent: The resource name of the FirebaseProject to link to an existing Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = AddGoogleAnalyticsRequest.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_android_apps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_android_apps_create

    Requests the creation of a new AndroidApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

    :param parent: The resource name of the parent FirebaseProject in which to create an AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = AndroidApp.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_android_apps_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebase_projects_android_apps_list

    Lists each AndroidApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

    :param parent: The resource name of the parent FirebaseProject for which to list each associated AndroidApp, in the format: projects/PROJECT_IDENTIFIER /androidApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param page_size: The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;ListAndroidApps&#x60; indicating where in the set of Apps to resume listing.
    :type page_token: str
    :param show_deleted: Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebase_projects_android_apps_sha_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_android_apps_sha_create

    Adds a ShaCertificate to the specified AndroidApp.

    :param parent: The resource name of the parent AndroidApp to which to add a ShaCertificate, in the format: projects/PROJECT_IDENTIFIER/androidApps/ APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the &#x60;AndroidApp&#x60; [&#x60;name&#x60;](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ShaCertificate.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_android_apps_sha_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firebase_projects_android_apps_sha_delete

    Removes a ShaCertificate from the specified AndroidApp.

    :param name: The resource name of the ShaCertificate to remove from the parent AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps/APP_ID /sha/SHA_HASH Refer to the &#x60;ShaCertificate&#x60; [&#x60;name&#x60;](../projects.androidApps.sha#ShaCertificate.FIELDS.name) field for details about PROJECT_IDENTIFIER, APP_ID, and SHA_HASH values. You can obtain the full resource name of the &#x60;ShaCertificate&#x60; from the response of [&#x60;ListShaCertificates&#x60;](../projects.androidApps.sha/list) or the original [&#x60;CreateShaCertificate&#x60;](../projects.androidApps.sha/create).
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

    """
    return web.Response(status=200)


async def firebase_projects_android_apps_sha_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firebase_projects_android_apps_sha_list

    Lists the SHA-1 and SHA-256 certificates for the specified AndroidApp.

    :param parent: The resource name of the parent AndroidApp for which to list each associated ShaCertificate, in the format: projects/PROJECT_IDENTIFIER /androidApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the &#x60;AndroidApp&#x60; [&#x60;name&#x60;](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
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

    """
    return web.Response(status=200)


async def firebase_projects_available_locations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """firebase_projects_available_locations_list

    **DEPRECATED.** _Instead, use the applicable resource-specific REST API (or associated documentation, as needed) to determine valid locations for each resource used in your Project._ Lists the valid Google Cloud Platform (GCP) resource locations for the specified Project (including a FirebaseProject). One of these locations can be selected as the Project&#39;s [_default_ GCP resource location](https://firebase.google.com/docs/projects/locations), which is the geographical location where the Project&#39;s resources, such as Cloud Firestore, will be provisioned by default. However, if the default GCP resource location has already been set for the Project, then this setting cannot be changed. This call checks for any possible [location restrictions](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations) for the specified Project and, thus, might return a subset of all possible GCP resource locations. To list all GCP resource locations (regardless of any restrictions), call the endpoint without specifying a unique project identifier (that is, &#x60;/v1beta1/{parent&#x3D;projects/-}/listAvailableLocations&#x60;). To call &#x60;ListAvailableLocations&#x60; with a specified project, a member must be at minimum a Viewer of the Project. Calls without a specified project do not require any specific project permissions.

    :param parent: The FirebaseProject for which to list GCP resource locations, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. If no unique project identifier is specified (that is, &#x60;projects/-&#x60;), the returned list does not take into account org-specific or project-specific location restrictions.
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
    :param page_size: The maximum number of locations to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;ListAvailableLocations&#x60; indicating where in the list of locations to resume listing.
    :type page_token: str

    """
    return web.Response(status=200)


async def firebase_projects_default_location_finalize(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_default_location_finalize

    **DEPRECATED.** _Instead, use the applicable resource-specific REST API to set the location for each resource used in your Project._ Sets the default Google Cloud Platform (GCP) resource location for the specified FirebaseProject. This method creates an App Engine application with a [default Cloud Storage bucket](https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/setting-up-cloud-storage#activating_a_cloud_storage_bucket), located in the specified [&#x60;locationId&#x60;](#body.request_body.FIELDS.location_id). This location must be one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations). After the default GCP resource location is finalized, or if it was already set, it cannot be changed. The default GCP resource location for the specified &#x60;FirebaseProject&#x60; might already be set because either the underlying GCP &#x60;Project&#x60; already has an App Engine application or &#x60;FinalizeDefaultLocation&#x60; was previously called with a specified &#x60;locationId&#x60;. Any new calls to &#x60;FinalizeDefaultLocation&#x60; with a *different* specified &#x60;locationId&#x60; will return a 409 error. The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations), which can be used to track the provisioning process. The [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) type of the &#x60;Operation&#x60; is google.protobuf.Empty. The &#x60;Operation&#x60; can be polled by its &#x60;name&#x60; using GetOperation until &#x60;done&#x60; is true. When &#x60;done&#x60; is true, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; has succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) will be set to a google.protobuf.Empty; if the &#x60;Operation&#x60; has failed, its &#x60;error&#x60; will be set to a google.rpc.Status. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call DeleteOperation. All fields listed in the [request body](#request-body) are required. To call &#x60;FinalizeDefaultLocation&#x60;, a member must be an Owner of the Project.

    :param parent: The resource name of the FirebaseProject for which the default GCP resource location will be set, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = FinalizeDefaultLocationRequest.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_ios_apps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_ios_apps_create

    Requests the creation of a new IosApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

    :param parent: The resource name of the parent FirebaseProject in which to create an IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = IosApp.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_ios_apps_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebase_projects_ios_apps_list

    Lists each IosApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

    :param parent: The resource name of the parent FirebaseProject for which to list each associated IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param page_size: The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;ListIosApps&#x60; indicating where in the set of Apps to resume listing.
    :type page_token: str
    :param show_deleted: Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebase_projects_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebase_projects_list

    Lists each FirebaseProject accessible to the caller. The elements are returned in no particular order, but they will be a consistent view of the Projects when additional requests are made with a &#x60;pageToken&#x60;. This method is eventually consistent with Project mutations, which means newly provisioned Projects and recent modifications to existing Projects might not be reflected in the set of Projects. The list will include only ACTIVE Projects. Use GetFirebaseProject for consistent reads as well as for additional Project details.

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
    :param page_size: The maximum number of Projects to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. This value cannot be negative.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;ListFirebaseProjects&#x60; indicating where in the set of Projects to resume listing.
    :type page_token: str
    :param show_deleted: Optional. Controls whether Projects in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Projects will be returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebase_projects_remove_analytics(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_remove_analytics

    Unlinks the specified FirebaseProject from its Google Analytics account. This call removes the association of the specified &#x60;FirebaseProject&#x60; with its current Google Analytics property. However, this call does not delete the Google Analytics resources, such as the Google Analytics property or any data streams. These resources may be re-associated later to the &#x60;FirebaseProject&#x60; by calling [&#x60;AddGoogleAnalytics&#x60;](../../v1beta1/projects/addGoogleAnalytics) and specifying the same &#x60;analyticsPropertyId&#x60;. For Android Apps and iOS Apps, this call re-links data streams with their corresponding apps. However, for Web Apps, this call provisions a *new* data stream for each Web App. To call &#x60;RemoveAnalytics&#x60;, a project member must be an Owner for the &#x60;FirebaseProject&#x60;.

    :param parent: The resource name of the FirebaseProject to unlink from its Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveAnalyticsRequest.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_search_apps(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebase_projects_search_apps

    Lists all available Apps for the specified FirebaseProject. This is a convenience method. Typically, interaction with an App should be done using the platform-specific service, but some tool use-cases require a summary of all known Apps (such as for App selector interfaces).

    :param parent: The parent FirebaseProject for which to list Apps, in the format: projects/ PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param filter: A query string compatible with Google&#39;s [AIP-160 standard](https://google.aip.dev/160). Use any of the following fields in a query: * [&#x60;app_id&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.app_id) * [&#x60;namespace&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.namespace) * [&#x60;platform&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.platform) This query also supports the following \&quot;virtual\&quot; fields. These are fields which are not actually part of the returned resource object, but they can be queried as if they are pre-populated with specific values. * &#x60;sha1_hash&#x60; or &#x60;sha1_hashes&#x60;: This field is considered to be a _repeated_ &#x60;string&#x60; field, populated with the list of all SHA-1 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an &#x60;AndroidApp&#x60;. * &#x60;sha256_hash&#x60; or &#x60;sha256_hashes&#x60;: This field is considered to be a _repeated_ &#x60;string&#x60; field, populated with the list of all SHA-256 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an &#x60;AndroidApp&#x60;. * &#x60;app_store_id&#x60;: This field is considered to be a _singular_ &#x60;string&#x60; field, populated with the Apple App Store ID registered with the IosApp. This field is empty if the App is not an &#x60;IosApp&#x60;. * &#x60;team_id&#x60;: This field is considered to be a _singular_ &#x60;string&#x60; field, populated with the Apple team ID registered with the IosApp. This field is empty if the App is not an &#x60;IosApp&#x60;.
    :type filter: str
    :param page_size: The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;SearchFirebaseApps&#x60; indicating where in the set of Apps to resume listing.
    :type page_token: str
    :param show_deleted: Controls whether Apps in the DELETED state should be returned. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebase_projects_web_apps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_web_apps_create

    Requests the creation of a new WebApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

    :param parent: The resource name of the parent FirebaseProject in which to create a WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param body: 
    :type body: dict | bytes

    """
    body = WebApp.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_web_apps_get_config(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firebase_projects_web_apps_get_config

    Gets the configuration artifact associated with the specified WebApp.

    :param name: The resource name of the WebApp configuration to download, in the format: projects/PROJECT_IDENTIFIER/webApps/APP_ID/config Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the &#x60;WebApp&#x60; [&#x60;name&#x60;](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
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

    """
    return web.Response(status=200)


async def firebase_projects_web_apps_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """firebase_projects_web_apps_list

    Lists each WebApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

    :param parent: The resource name of the parent FirebaseProject for which to list each associated WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
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
    :param page_size: The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit.
    :type page_size: int
    :param page_token: Token returned from a previous call to &#x60;ListWebApps&#x60; indicating where in the set of Apps to resume listing.
    :type page_token: str
    :param show_deleted: Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def firebase_projects_web_apps_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """firebase_projects_web_apps_patch

    Updates the attributes of the specified WebApp.

    :param name: The resource name of the WebApp, in the format: projects/PROJECT_IDENTIFIER /webApps/APP_ID * PROJECT_IDENTIFIER: the parent Project&#39;s [&#x60;ProjectNumber&#x60;](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the &#x60;ProjectId&#x60;. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [&#x60;appId&#x60;](../projects.webApps#WebApp.FIELDS.app_id)).
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
    :param update_mask: Specifies which fields of the WebApp to update. Note that the following fields are immutable: &#x60;name&#x60;, &#x60;app_id&#x60;, and &#x60;project_id&#x60;. To update &#x60;state&#x60;, use any of the following endpoints: RemoveWebApp or UndeleteWebApp.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = WebApp.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_web_apps_remove(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_web_apps_remove

    Removes the specified WebApp from the FirebaseProject.

    :param name: Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
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
    body = RemoveWebAppRequest.from_dict(body)
    return web.Response(status=200)


async def firebase_projects_web_apps_undelete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebase_projects_web_apps_undelete

    Restores the specified WebApp to the FirebaseProject.

    :param name: Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
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
    body = UndeleteWebAppRequest.from_dict(body)
    return web.Response(status=200)
