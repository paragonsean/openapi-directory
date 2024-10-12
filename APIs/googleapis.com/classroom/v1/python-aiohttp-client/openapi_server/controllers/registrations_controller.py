from typing import List, Dict
from aiohttp import web

from openapi_server.models.registration import Registration
from openapi_server import util


async def classroom_registrations_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_registrations_create

    Creates a &#x60;Registration&#x60;, causing Classroom to start sending notifications from the provided &#x60;feed&#x60; to the destination provided in &#x60;cloudPubSubTopic&#x60;. Returns the created &#x60;Registration&#x60;. Currently, this will be the same as the argument, but with server-assigned fields such as &#x60;expiry_time&#x60; and &#x60;id&#x60; filled in. Note that any value specified for the &#x60;expiry_time&#x60; or &#x60;id&#x60; fields will be ignored. While Classroom may validate the &#x60;cloudPubSubTopic&#x60; and return errors on a best effort basis, it is the caller&#39;s responsibility to ensure that it exists and that Classroom has permission to publish to it. This method may return the following error codes: * &#x60;PERMISSION_DENIED&#x60; if: * the authenticated user does not have permission to receive notifications from the requested field; or * the current user has not granted access to the current Cloud project with the appropriate scope for the requested feed. Note that domain-wide delegation of authority is not currently supported for this purpose. If the request has the appropriate scope, but no grant exists, a Request Errors is returned. * another access error is encountered. * &#x60;INVALID_ARGUMENT&#x60; if: * no &#x60;cloudPubsubTopic&#x60; is specified, or the specified &#x60;cloudPubsubTopic&#x60; is not valid; or * no &#x60;feed&#x60; is specified, or the specified &#x60;feed&#x60; is not valid. * &#x60;NOT_FOUND&#x60; if: * the specified &#x60;feed&#x60; cannot be located, or the requesting user does not have permission to determine whether or not it exists; or * the specified &#x60;cloudPubsubTopic&#x60; cannot be located, or Classroom has not been granted permission to publish to it.

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
    body = Registration.from_dict(body)
    return web.Response(status=200)


async def classroom_registrations_delete(request: web.Request, registration_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_registrations_delete

    Deletes a &#x60;Registration&#x60;, causing Classroom to stop sending notifications for that &#x60;Registration&#x60;.

    :param registration_id: The &#x60;registration_id&#x60; of the &#x60;Registration&#x60; to be deleted.
    :type registration_id: str
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
