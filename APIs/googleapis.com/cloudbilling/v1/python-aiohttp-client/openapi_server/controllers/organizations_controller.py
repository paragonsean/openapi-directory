from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_account import BillingAccount
from openapi_server.models.list_billing_accounts_response import ListBillingAccountsResponse
from openapi_server import util


async def cloudbilling_organizations_billing_accounts_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudbilling_organizations_billing_accounts_create

    This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts). Google Cloud resellers should use the Channel Services APIs, [accounts.customers.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create) and [accounts.customers.entitlements.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create). When creating a subaccount, the current authenticated user must have the &#x60;billing.accounts.update&#x60; IAM permission on the parent account, which is typically given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access). This method will return an error if the parent account has not been provisioned for subaccounts.

    :param parent: Optional. The parent to create a billing account from. Format: - &#x60;billingAccounts/{billing_account_id}&#x60;, for example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60;
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
    body = BillingAccount.from_dict(body)
    return web.Response(status=200)


async def cloudbilling_organizations_billing_accounts_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_organizations_billing_accounts_list

    Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).

    :param parent: Optional. The parent resource to list billing accounts from. Format: - &#x60;organizations/{organization_id}&#x60;, for example, &#x60;organizations/12345678&#x60; - &#x60;billingAccounts/{billing_account_id}&#x60;, for example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60;
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
    :param filter: Options for how to filter the returned billing accounts. This only supports filtering for [subaccounts](https://cloud.google.com/billing/docs/concepts) under a single provided parent billing account. (for example, &#x60;master_billing_account&#x3D;billingAccounts/012345-678901-ABCDEF&#x60;). Boolean algebra and other fields are not currently supported.
    :type filter: str
    :param page_size: Requested page size. The maximum page size is 100; this is also the default.
    :type page_size: int
    :param page_token: A token identifying a page of results to return. This should be a &#x60;next_page_token&#x60; value returned from a previous &#x60;ListBillingAccounts&#x60; call. If unspecified, the first page of results is returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudbilling_organizations_billing_accounts_move(request: web.Request, destination_parent, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """cloudbilling_organizations_billing_accounts_move

    Changes which parent organization a billing account belongs to.

    :param destination_parent: Required. The resource name of the Organization to move the billing account under. Must be of the form &#x60;organizations/{organization_id}&#x60;.
    :type destination_parent: str
    :param name: Required. The resource name of the billing account to move. Must be of the form &#x60;billingAccounts/{billing_account_id}&#x60;. The specified billing account cannot be a subaccount, since a subaccount always belongs to the same organization as its parent account.
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
