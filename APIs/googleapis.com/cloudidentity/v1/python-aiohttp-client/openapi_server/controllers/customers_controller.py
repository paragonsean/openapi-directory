from typing import List, Dict
from aiohttp import web

from openapi_server.models.is_invitable_user_response import IsInvitableUserResponse
from openapi_server.models.list_user_invitations_response import ListUserInvitationsResponse
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudidentity_customers_userinvitations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_customers_userinvitations_cancel

    Cancels a UserInvitation that was already sent.

    :param name: Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60;
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
    :type body: 

    """
    return web.Response(status=200)


async def cloudidentity_customers_userinvitations_is_invitable_user(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """cloudidentity_customers_userinvitations_is_invitable_user

    Verifies whether a user account is eligible to receive a UserInvitation (is an unmanaged account). Eligibility is based on the following criteria: * the email address is a consumer account and it&#39;s the primary email address of the account, and * the domain of the email address matches an existing verified Google Workspace or Cloud Identity domain If both conditions are met, the user is eligible. **Note:** This method is not supported for Workspace Essentials customers.

    :param name: Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60;
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


async def cloudidentity_customers_userinvitations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_customers_userinvitations_list

    Retrieves a list of UserInvitation resources. **Note:** New consumer accounts with the customer&#39;s verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains.

    :param parent: Required. The customer ID of the Google Workspace or Cloud Identity account the UserInvitation resources are associated with.
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
    :param filter: Optional. A query string for filtering &#x60;UserInvitation&#x60; results by their current state, in the format: &#x60;\&quot;state&#x3D;&#x3D;&#39;invited&#39;\&quot;&#x60;.
    :type filter: str
    :param order_by: Optional. The sort order of the list results. You can sort the results in descending order based on either email or last update timestamp but not both, using &#x60;order_by&#x3D;\&quot;email desc\&quot;&#x60;. Currently, sorting is supported for &#x60;update_time asc&#x60;, &#x60;update_time desc&#x60;, &#x60;email asc&#x60;, and &#x60;email desc&#x60;. If not specified, results will be returned based on &#x60;email asc&#x60; order.
    :type order_by: str
    :param page_size: Optional. The maximum number of UserInvitation resources to return. If unspecified, at most 100 resources will be returned. The maximum value is 200; values above 200 will be set to 200.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListUserInvitations&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBooks&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_customers_userinvitations_send(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_customers_userinvitations_send

    Sends a UserInvitation to email. If the &#x60;UserInvitation&#x60; does not exist for this request and it is a valid request, the request creates a &#x60;UserInvitation&#x60;. **Note:** The &#x60;get&#x60; and &#x60;list&#x60; methods have a 48-hour delay where newly-created consumer accounts will not appear in the results. You can still send a &#x60;UserInvitation&#x60; to those accounts if you know the unmanaged email address and IsInvitableUser&#x3D;&#x3D;True.

    :param name: Required. &#x60;UserInvitation&#x60; name in the format &#x60;customers/{customer}/userinvitations/{user_email_address}&#x60;
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
    :type body: 

    """
    return web.Response(status=200)
