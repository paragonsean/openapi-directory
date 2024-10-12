from typing import List, Dict
from aiohttp import web

from openapi_server.models.estimate_cost_scenario_for_billing_account_request import EstimateCostScenarioForBillingAccountRequest
from openapi_server.models.estimate_cost_scenario_for_billing_account_response import EstimateCostScenarioForBillingAccountResponse
from openapi_server.models.google_cloud_billing_billingaccountservices_v1beta_list_billing_account_services_response import GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse
from openapi_server.models.google_cloud_billing_billingaccountskugroups_v1beta_list_billing_account_sku_groups_response import GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse
from openapi_server import util


async def cloudbilling_billing_accounts_estimate_cost_scenario(request: web.Request, billing_account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudbilling_billing_accounts_estimate_cost_scenario

    Use custom pricing in the estimate, using a &#x60;CostScenario&#x60; with a defined &#x60;billingAccount&#x60;.

    :param billing_account: Resource name of the billing account for the cost estimate. The resource name has the form &#x60;billingAccounts/{billing_account_id}&#x60;. For example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60; is the resource name for billing account &#x60;012345-567890-ABCDEF&#x60;. Must be specified.
    :type billing_account: str
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
    body = EstimateCostScenarioForBillingAccountRequest.from_dict(body)
    return web.Response(status=200)


async def cloudbilling_billing_accounts_services_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_billing_accounts_services_list

    Lists services visible to a billing account.

    :param parent: Required. The billing account to list billing account service from. Format: billingAccounts/{billing_account}
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
    :param page_size: Maximum number of billing account service to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    :type page_size: int
    :param page_token: Page token received from a previous ListBillingAccountServices call to retrieve the next page of results. If this field is empty, the first page is returned.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudbilling_billing_accounts_sku_groups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudbilling_billing_accounts_sku_groups_list

    Lists SKU groups visible to a billing account.

    :param parent: Required. The billing account to list billing account SKU groups from. Format: billingAccounts/{billing_account}
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
    :param page_size: Maximum number of billing account SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    :type page_size: int
    :param page_token: Page token received from a previous ListBillingAccountSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned.
    :type page_token: str

    """
    return web.Response(status=200)
