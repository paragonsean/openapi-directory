from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_browser_dlp_rule import GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_browser_dlp_rules_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_partner_tenants_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_proxy_configs_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_partner_tenant import GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_proxy_config import GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig
from openapi_server.models.google_cloud_beyondcorp_saasplatform_subscriptions_v1alpha_list_subscriptions_response import GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse
from openapi_server.models.google_cloud_beyondcorp_saasplatform_subscriptions_v1alpha_subscription import GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, body=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_create

    Creates a new BrowserDlpRule in a given organization and PartnerTenant.

    :param parent: Required. The resource name of the BrowserDlpRule parent using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60;
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
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_list

    Lists BrowserDlpRules for PartnerTenant in a given organization.

    :param parent: Required. The parent partnerTenant to which the BrowserDlpRules belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60;
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


async def beyondcorp_organizations_locations_global_partner_tenants_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, body=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_create

    Creates a new BeyondCorp Enterprise partnerTenant in a given organization and can only be called by onboarded BeyondCorp Enterprise partner.

    :param parent: Required. The resource name of the parent organization using the form: &#x60;organizations/{organization_id}/locations/global&#x60;
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
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_organizations_locations_global_partner_tenants_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_list

    Lists PartnerTenants in a given organization.

    :param parent: Required. The parent organization to which the PartnerTenants belong. Format: &#x60;organizations/{organization_id}/locations/global&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation. All fields in the PartnerTenant message are supported. For example, the following query will return the PartnerTenants with displayName \&quot;test-tenant\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;displayName&#x3D;\&quot;test-tenant\&quot; Nested fields are also supported. The follow query will return PartnerTenants with internal_tenant_id \&quot;1234\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;partnerMetadata.internalTenantId&#x3D;\&quot;1234\&quot; For more information, please refer to https://google.aip.dev/160.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListPartnerTenantsResponse, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, body=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_create

    Creates a new BeyondCorp Enterprise ProxyConfig in a given organization and PartnerTenant. Can only be called by on onboarded Beyondcorp Enterprise partner.

    :param parent: Required. The resource name of the parent PartnerTenant using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60;
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
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_list

    Lists ProxyConfigs for PartnerTenant in a given organization.

    :param parent: Required. The parent organization to which the ProxyConfigs belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation. All fields in the ProxyConfig message are supported. For example, the following query will return the ProxyConfigs with displayName \&quot;test-config\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;displayName&#x3D;\&quot;test-config\&quot; Nested fields are also supported. The follow query will return ProxyConfigs with pacUri \&quot;example.com/pac.pac\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;routingInfo.pacUri&#x3D;\&quot;example.com/pac.pac\&quot; For more information, please refer to https://google.aip.dev/160.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListProxyConfigsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_organizations_locations_subscriptions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_organizations_locations_subscriptions_create

    Creates a new BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization.

    :param parent: Required. The resource name of the subscription location using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60;
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
    body = GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_organizations_locations_subscriptions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_organizations_locations_subscriptions_list

    Lists Subscriptions in a given organization and location.

    :param parent: Required. The resource name of Subscription using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60;
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
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListSubscriptionsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)
