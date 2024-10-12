from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_resourcesettings_v1_list_settings_response import GoogleCloudResourcesettingsV1ListSettingsResponse
from openapi_server.models.google_cloud_resourcesettings_v1_setting import GoogleCloudResourcesettingsV1Setting
from openapi_server import util


async def resourcesettings_projects_settings_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, view=None) -> web.Response:
    """resourcesettings_projects_settings_get

    Returns a specified setting. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the setting does not exist.

    :param name: Required. The name of the setting to get. See Setting for naming requirements.
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
    :param view: The SettingView for this request.
    :type view: str

    """
    return web.Response(status=200)


async def resourcesettings_projects_settings_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, view=None) -> web.Response:
    """resourcesettings_projects_settings_list

    Lists all the settings that are available on the Cloud resource &#x60;parent&#x60;.

    :param parent: Required. The project, folder, or organization that is the parent resource for this setting. Must be in one of the following forms: * &#x60;projects/{project_number}&#x60; * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60;
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
    :param page_size: Unused. The size of the page to be returned.
    :type page_size: int
    :param page_token: Unused. A page token used to retrieve the next page.
    :type page_token: str
    :param view: The SettingView for this request.
    :type view: str

    """
    return web.Response(status=200)


async def resourcesettings_projects_settings_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """resourcesettings_projects_settings_patch

    Updates a specified setting. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.NOT_FOUND&#x60; if the setting does not exist. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.FAILED_PRECONDITION&#x60; if the setting is flagged as read only. Returns a &#x60;google.rpc.Status&#x60; with &#x60;google.rpc.Code.ABORTED&#x60; if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only &#x60;name&#x60;, &#x60;local_value&#x60; and &#x60;etag&#x60;. The &#x60;metadata&#x60; and &#x60;effective_value&#x60; cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the &#x60;local_value&#x60; field.

    :param name: The resource name of the setting. Must be in one of the following forms: * &#x60;projects/{project_number}/settings/{setting_name}&#x60; * &#x60;folders/{folder_id}/settings/{setting_name}&#x60; * &#x60;organizations/{organization_id}/settings/{setting_name}&#x60; For example, \&quot;/projects/123/settings/gcp-enableMyFeature\&quot;
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
    body = GoogleCloudResourcesettingsV1Setting.from_dict(body)
    return web.Response(status=200)
