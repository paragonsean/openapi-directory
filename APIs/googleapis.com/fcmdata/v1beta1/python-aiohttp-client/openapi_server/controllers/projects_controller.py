from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_firebase_fcm_data_v1beta1_list_android_delivery_data_response import GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse
from openapi_server import util


async def fcmdata_projects_android_apps_delivery_data_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """fcmdata_projects_android_apps_delivery_data_list

    List aggregate delivery data for the given Android application.

    :param parent: Required. The application for which to list delivery data. Format: &#x60;projects/{project_id}/androidApps/{app_id}&#x60;
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
    :param page_size: The maximum number of entries to return. The service may return fewer than this value. If unspecified, at most 1,000 entries will be returned. The maximum value is 10,000; values above 10,000 will be capped to 10,000. This default may change over time.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListAndroidDeliveryDataRequest&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListAndroidDeliveryDataRequest&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)
