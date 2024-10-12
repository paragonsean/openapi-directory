from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_channel_v1_activate_entitlement_request import GoogleCloudChannelV1ActivateEntitlementRequest
from openapi_server.models.google_cloud_channel_v1_change_offer_request import GoogleCloudChannelV1ChangeOfferRequest
from openapi_server.models.google_cloud_channel_v1_change_parameters_request import GoogleCloudChannelV1ChangeParametersRequest
from openapi_server.models.google_cloud_channel_v1_change_renewal_settings_request import GoogleCloudChannelV1ChangeRenewalSettingsRequest
from openapi_server.models.google_cloud_channel_v1_channel_partner_link import GoogleCloudChannelV1ChannelPartnerLink
from openapi_server.models.google_cloud_channel_v1_channel_partner_repricing_config import GoogleCloudChannelV1ChannelPartnerRepricingConfig
from openapi_server.models.google_cloud_channel_v1_check_cloud_identity_accounts_exist_request import GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequest
from openapi_server.models.google_cloud_channel_v1_check_cloud_identity_accounts_exist_response import GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponse
from openapi_server.models.google_cloud_channel_v1_create_entitlement_request import GoogleCloudChannelV1CreateEntitlementRequest
from openapi_server.models.google_cloud_channel_v1_customer import GoogleCloudChannelV1Customer
from openapi_server.models.google_cloud_channel_v1_customer_repricing_config import GoogleCloudChannelV1CustomerRepricingConfig
from openapi_server.models.google_cloud_channel_v1_fetch_report_results_request import GoogleCloudChannelV1FetchReportResultsRequest
from openapi_server.models.google_cloud_channel_v1_fetch_report_results_response import GoogleCloudChannelV1FetchReportResultsResponse
from openapi_server.models.google_cloud_channel_v1_import_customer_request import GoogleCloudChannelV1ImportCustomerRequest
from openapi_server.models.google_cloud_channel_v1_list_channel_partner_links_response import GoogleCloudChannelV1ListChannelPartnerLinksResponse
from openapi_server.models.google_cloud_channel_v1_list_channel_partner_repricing_configs_response import GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponse
from openapi_server.models.google_cloud_channel_v1_list_customer_repricing_configs_response import GoogleCloudChannelV1ListCustomerRepricingConfigsResponse
from openapi_server.models.google_cloud_channel_v1_list_customers_response import GoogleCloudChannelV1ListCustomersResponse
from openapi_server.models.google_cloud_channel_v1_list_entitlement_changes_response import GoogleCloudChannelV1ListEntitlementChangesResponse
from openapi_server.models.google_cloud_channel_v1_list_entitlements_response import GoogleCloudChannelV1ListEntitlementsResponse
from openapi_server.models.google_cloud_channel_v1_list_offers_response import GoogleCloudChannelV1ListOffersResponse
from openapi_server.models.google_cloud_channel_v1_list_purchasable_offers_response import GoogleCloudChannelV1ListPurchasableOffersResponse
from openapi_server.models.google_cloud_channel_v1_list_purchasable_skus_response import GoogleCloudChannelV1ListPurchasableSkusResponse
from openapi_server.models.google_cloud_channel_v1_list_reports_response import GoogleCloudChannelV1ListReportsResponse
from openapi_server.models.google_cloud_channel_v1_list_sku_group_billable_skus_response import GoogleCloudChannelV1ListSkuGroupBillableSkusResponse
from openapi_server.models.google_cloud_channel_v1_list_sku_groups_response import GoogleCloudChannelV1ListSkuGroupsResponse
from openapi_server.models.google_cloud_channel_v1_list_subscribers_response import GoogleCloudChannelV1ListSubscribersResponse
from openapi_server.models.google_cloud_channel_v1_list_transferable_offers_request import GoogleCloudChannelV1ListTransferableOffersRequest
from openapi_server.models.google_cloud_channel_v1_list_transferable_offers_response import GoogleCloudChannelV1ListTransferableOffersResponse
from openapi_server.models.google_cloud_channel_v1_list_transferable_skus_request import GoogleCloudChannelV1ListTransferableSkusRequest
from openapi_server.models.google_cloud_channel_v1_list_transferable_skus_response import GoogleCloudChannelV1ListTransferableSkusResponse
from openapi_server.models.google_cloud_channel_v1_offer import GoogleCloudChannelV1Offer
from openapi_server.models.google_cloud_channel_v1_provision_cloud_identity_request import GoogleCloudChannelV1ProvisionCloudIdentityRequest
from openapi_server.models.google_cloud_channel_v1_query_eligible_billing_accounts_response import GoogleCloudChannelV1QueryEligibleBillingAccountsResponse
from openapi_server.models.google_cloud_channel_v1_register_subscriber_request import GoogleCloudChannelV1RegisterSubscriberRequest
from openapi_server.models.google_cloud_channel_v1_register_subscriber_response import GoogleCloudChannelV1RegisterSubscriberResponse
from openapi_server.models.google_cloud_channel_v1_run_report_job_request import GoogleCloudChannelV1RunReportJobRequest
from openapi_server.models.google_cloud_channel_v1_start_paid_service_request import GoogleCloudChannelV1StartPaidServiceRequest
from openapi_server.models.google_cloud_channel_v1_suspend_entitlement_request import GoogleCloudChannelV1SuspendEntitlementRequest
from openapi_server.models.google_cloud_channel_v1_transfer_entitlements_request import GoogleCloudChannelV1TransferEntitlementsRequest
from openapi_server.models.google_cloud_channel_v1_transfer_entitlements_to_google_request import GoogleCloudChannelV1TransferEntitlementsToGoogleRequest
from openapi_server.models.google_cloud_channel_v1_unregister_subscriber_request import GoogleCloudChannelV1UnregisterSubscriberRequest
from openapi_server.models.google_cloud_channel_v1_unregister_subscriber_response import GoogleCloudChannelV1UnregisterSubscriberResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_create

    Creates a ChannelPartnerRepricingConfig. Call this method to set modifications for a specific ChannelPartner&#39;s bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions. When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month. The following restrictions are for creating configs in the current month. * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. * There is a limit of ten configs for any ChannelPartner or RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. * The contained ChannelPartnerRepricingConfig.repricing_config value must be different from the value used in the current config for a ChannelPartner. Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different. * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated ChannelPartnerRepricingConfig resource, otherwise returns an error.

    :param parent: Required. The resource name of the ChannelPartner that will receive the repricing config. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}
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
    body = GoogleCloudChannelV1ChannelPartnerRepricingConfig.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_list

    Lists information about how a Reseller modifies their bill before sending it to a ChannelPartner. Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different. * NOT_FOUND: The ChannelPartnerRepricingConfig specified does not exist or is not associated with the given account. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the ChannelPartnerRepricingConfig resources. The data for each resource is displayed in the ascending order of: * Channel Partner ID * RepricingConfig.effective_invoice_month * ChannelPartnerRepricingConfig.update_time If unsuccessful, returns an error.

    :param parent: Required. The resource name of the account&#39;s ChannelPartnerLink. Parent uses the format: accounts/{account_id}/channelPartnerLinks/{channel_partner_id}. Supports accounts/{account_id}/channelPartnerLinks/- to retrieve configs for all channel partners.
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
    :param filter: Optional. A filter for [CloudChannelService.ListChannelPartnerRepricingConfigs] results (channel_partner_link only). You can use this filter when you support a BatchGet-like query. To use the filter, you must set &#x60;parent&#x3D;accounts/{account_id}/channelPartnerLinks/-&#x60;. Example: &#x60;channel_partner_link &#x3D; accounts/account_id/channelPartnerLinks/c1&#x60; OR &#x60;channel_partner_link &#x3D; accounts/account_id/channelPartnerLinks/c2&#x60;.
    :type filter: str
    :param page_size: Optional. The maximum number of repricing configs to return. The service may return fewer than this value. If unspecified, returns a maximum of 50 rules. The maximum value is 100; values above 100 will be coerced to 100.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results beyond the first page. Obtained through ListChannelPartnerRepricingConfigsResponse.next_page_token of the previous CloudChannelService.ListChannelPartnerRepricingConfigs call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_channel_partner_links_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_channel_partner_links_create

    Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. * NOT_FOUND: No Cloud Identity customer exists for provided domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The new ChannelPartnerLink resource.

    :param parent: Required. Create a channel partner link for the provided reseller account&#39;s resource name. Parent uses the format: accounts/{account_id}
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
    body = GoogleCloudChannelV1ChannelPartnerLink.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_channel_partner_links_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, view=None) -> web.Response:
    """cloudchannel_accounts_channel_partner_links_list

    List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: The list of the distributor account&#39;s ChannelPartnerLink resources.

    :param parent: Required. The resource name of the reseller account for listing channel partner links. Parent uses the format: accounts/{account_id}
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
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, server will pick a default size (25). The maximum value is 200; the server will coerce values above 200.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page. Obtained using ListChannelPartnerLinksResponse.next_page_token of the previous CloudChannelService.ListChannelPartnerLinks call.
    :type page_token: str
    :param view: Optional. The level of granularity the ChannelPartnerLink will display.
    :type view: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_check_cloud_identity_accounts_exist(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_check_cloud_identity_accounts_exist

    Confirms the existence of Cloud Identity accounts based on the domain and if the Cloud Identity accounts are owned by the reseller. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * INVALID_VALUE: Invalid domain value in the request. Return value: A list of CloudIdentityCustomerAccount resources for the domain (may be empty) Note: in the v1alpha1 version of the API, a NOT_FOUND error returns if no CloudIdentityCustomerAccount resources match the domain.

    :param parent: Required. The reseller account&#39;s resource name. Parent uses the format: accounts/{account_id}
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
    body = GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_create

    Creates a new Customer resource under the reseller or distributor account. Possible error codes: * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to create a customer. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Domain field value doesn&#39;t match the primary email domain. Return value: The newly created Customer resource.

    :param parent: Required. The resource name of reseller account in which to create the customer. Parent uses the format: accounts/{account_id}
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
    body = GoogleCloudChannelV1Customer.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_customer_repricing_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_customer_repricing_configs_create

    Creates a CustomerRepricingConfig. Call this method to set modifications for a specific customer&#39;s bill. You can only create configs if the RepricingConfig.effective_invoice_month is a future month. If needed, you can create a config for the current month, with some restrictions. When creating a config for a future month, make sure there are no existing configs for that RepricingConfig.effective_invoice_month. The following restrictions are for creating configs in the current month. * This functionality is reserved for recovering from an erroneous config, and should not be used for regular business cases. * The new config will not modify exports used with other configs. Changes to the config may be immediate, but may take up to 24 hours. * There is a limit of ten configs for any RepricingConfig.EntitlementGranularity.entitlement, for any RepricingConfig.effective_invoice_month. * The contained CustomerRepricingConfig.repricing_config value must be different from the value used in the current config for a RepricingConfig.EntitlementGranularity.entitlement. Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different. * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

    :param parent: Required. The resource name of the customer that will receive this repricing config. Parent uses the format: accounts/{account_id}/customers/{customer_id}
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
    body = GoogleCloudChannelV1CustomerRepricingConfig.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_customer_repricing_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_customer_repricing_configs_list

    Lists information about how a Reseller modifies their bill before sending it to a Customer. Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different. * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the CustomerRepricingConfig resources. The data for each resource is displayed in the ascending order of: * Customer ID * RepricingConfig.EntitlementGranularity.entitlement * RepricingConfig.effective_invoice_month * CustomerRepricingConfig.update_time If unsuccessful, returns an error.

    :param parent: Required. The resource name of the customer. Parent uses the format: accounts/{account_id}/customers/{customer_id}. Supports accounts/{account_id}/customers/- to retrieve configs for all customers.
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
    :param filter: Optional. A filter for [CloudChannelService.ListCustomerRepricingConfigs] results (customer only). You can use this filter when you support a BatchGet-like query. To use the filter, you must set &#x60;parent&#x3D;accounts/{account_id}/customers/-&#x60;. Example: customer &#x3D; accounts/account_id/customers/c1 OR customer &#x3D; accounts/account_id/customers/c2.
    :type filter: str
    :param page_size: Optional. The maximum number of repricing configs to return. The service may return fewer than this value. If unspecified, returns a maximum of 50 rules. The maximum value is 100; values above 100 will be coerced to 100.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results beyond the first page. Obtained through ListCustomerRepricingConfigsResponse.next_page_token of the previous CloudChannelService.ListCustomerRepricingConfigs call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_customer_repricing_configs_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_customer_repricing_configs_patch

    Updates a CustomerRepricingConfig. Call this method to set modifications for a specific customer&#39;s bill. This method overwrites the existing CustomerRepricingConfig. You can only update configs if the RepricingConfig.effective_invoice_month is a future month. To make changes to configs for the current month, use CreateCustomerRepricingConfig, taking note of its restrictions. You cannot update the RepricingConfig.effective_invoice_month. When updating a config in the future: * This config must already exist. Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different. * INVALID_ARGUMENT: Missing or invalid required parameters in the request. Also displays if the updated config is for the current month or past months. * NOT_FOUND: The CustomerRepricingConfig specified does not exist or is not associated with the given account. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the updated CustomerRepricingConfig resource, otherwise returns an error.

    :param name: Output only. Resource name of the CustomerRepricingConfig. Format: accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.
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
    :param update_mask: The update mask that applies to the resource. Optional.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudChannelV1CustomerRepricingConfig.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_activate(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_activate

    Activates a previously suspended entitlement. Entitlements suspended for pending ToS acceptance can&#39;t be activated using this method. An entitlement activation is a long-running operation and it updates the state of the customer entitlement. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Entitlement resource not found. * SUSPENSION_NOT_RESELLER_INITIATED: Can only activate reseller-initiated suspensions and entitlements that have accepted the TOS. * NOT_SUSPENDED: Can only activate suspended entitlements not in an ACTIVE state. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The resource name of the entitlement to activate. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1ActivateEntitlementRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_change_offer(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_change_offer

    Updates the Offer for an existing customer entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Offer or Entitlement resource not found. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The resource name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1ChangeOfferRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_change_parameters(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_change_parameters

    Change parameters of the entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. For example, the number of seats being changed is greater than the allowed number of max seats, or decreasing seats for a commitment based plan. * NOT_FOUND: Entitlement resource not found. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1ChangeParametersRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_change_renewal_settings(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_change_renewal_settings

    Updates the renewal settings for an existing customer entitlement. An entitlement update is a long-running operation and it updates the entitlement as a result of fulfillment. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Entitlement resource not found. * NOT_COMMITMENT_PLAN: Renewal Settings are only applicable for a commitment plan. Can&#39;t enable or disable renewals for non-commitment plans. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1ChangeRenewalSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_create

    Creates an entitlement for a customer. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller. * The reseller is not authorized to transact on this Product. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * There is already a customer entitlement for a SKU from the same product family. * INVALID_VALUE: Make sure the OfferId is valid. If it is, contact Google Channel support for further troubleshooting. * NOT_FOUND: The customer or offer resource was not found. * ALREADY_EXISTS: * The SKU was already purchased for the customer. * The customer&#39;s primary email already exists. Retry after changing the customer&#39;s primary contact email. * CONDITION_NOT_MET or FAILED_PRECONDITION: * The domain required for purchasing a SKU has not been verified. * A pre-requisite SKU required to purchase an Add-On SKU is missing. For example, Google Workspace Business Starter is required to purchase Vault or Drive. * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param parent: Required. The resource name of the reseller&#39;s customer account in which to create the entitlement. Parent uses the format: accounts/{account_id}/customers/{customer_id}
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
    body = GoogleCloudChannelV1CreateEntitlementRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_list

    Lists Entitlements belonging to a customer. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: A list of the customer&#39;s Entitlements.

    :param parent: Required. The resource name of the reseller&#39;s customer account to list entitlements for. Parent uses the format: accounts/{account_id}/customers/{customer_id}
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
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, return at most 50 entitlements. The maximum value is 100; the server will coerce values above 100.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page. Obtained using ListEntitlementsResponse.next_page_token of the previous CloudChannelService.ListEntitlements call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_list_entitlement_changes(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_list_entitlement_changes

    List entitlement history. Possible error codes: * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different. * INVALID_ARGUMENT: Missing or invalid required fields in the request. * NOT_FOUND: The parent resource doesn&#39;t exist. Usually the result of an invalid name parameter. * INTERNAL: Any non-user error related to a technical issue in the backend. In this case, contact CloudChannel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. In this case, contact Cloud Channel support. Return value: List of EntitlementChanges.

    :param parent: Required. The resource name of the entitlement for which to list entitlement changes. The &#x60;-&#x60; wildcard may be used to match entitlements across a customer. Formats: * accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} * accounts/{account_id}/customers/{customer_id}/entitlements/-
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
    :param filter: Optional. Filters applied to the list results.
    :type filter: str
    :param page_size: Optional. The maximum number of entitlement changes to return. The service may return fewer than this value. If unspecified, returns at most 10 entitlement changes. The maximum value is 50; the server will coerce values above 50.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous CloudChannelService.ListEntitlementChanges call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to CloudChannelService.ListEntitlementChanges must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_lookup_offer(request: web.Request, entitlement, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_lookup_offer

    Returns the requested Offer resource. Possible error codes: * PERMISSION_DENIED: The entitlement doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Entitlement or offer was not found. Return value: The Offer resource.

    :param entitlement: Required. The resource name of the entitlement to retrieve the Offer. Entitlement uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    :type entitlement: str
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


async def cloudchannel_accounts_customers_entitlements_start_paid_service(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_start_paid_service

    Starts paid service for a trial entitlement. Starts paid service for a trial entitlement immediately. This method is only applicable if a plan is set up for a trial entitlement but has some trial days remaining. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Entitlement resource not found. * FAILED_PRECONDITION/NOT_IN_TRIAL: This method only works for entitlement on trial plans. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The name of the entitlement to start a paid service for. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1StartPaidServiceRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_entitlements_suspend(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_entitlements_suspend

    Suspends a previously fulfilled entitlement. An entitlement suspension is a long-running operation. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: Entitlement resource not found. * NOT_ACTIVE: Entitlement is not active. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param name: Required. The resource name of the entitlement to suspend. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
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
    body = GoogleCloudChannelV1SuspendEntitlementRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_import(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_import

    Imports a Customer from the Cloud Identity associated with the provided Cloud Identity ID or domain before a TransferEntitlements call. If a linked Customer already exists and overwrite_if_exists is true, it will update that Customer&#39;s data. Possible error codes: * PERMISSION_DENIED: * The reseller account making the request is different from the reseller account in the API request. * You are not authorized to import the customer. See https://support.google.com/channelservices/answer/9759265 * NOT_FOUND: Cloud Identity doesn&#39;t exist or was deleted. * INVALID_ARGUMENT: Required parameters are missing, or the auth_token is expired or invalid. * ALREADY_EXISTS: A customer already exists and has conflicting critical fields. Requires an overwrite. Return value: The Customer.

    :param parent: Required. The resource name of the reseller&#39;s account. Parent takes the format: accounts/{account_id} or accounts/{account_id}/channelPartnerLinks/{channel_partner_id}
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
    body = GoogleCloudChannelV1ImportCustomerRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_list

    List Customers. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: List of Customers, or an empty list if there are no customers.

    :param parent: Required. The resource name of the reseller account to list customers from. Parent uses the format: accounts/{account_id}.
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
    :param filter: Optional. Filters applied to the [CloudChannelService.ListCustomers] results. See https://cloud.google.com/channel/docs/concepts/google-cloud/filter-customers for more information.
    :type filter: str
    :param page_size: Optional. The maximum number of customers to return. The service may return fewer than this value. If unspecified, returns at most 10 customers. The maximum value is 50.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results other than the first page. Obtained through ListCustomersResponse.next_page_token of the previous CloudChannelService.ListCustomers call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_list_purchasable_offers(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, change_offer_purchase_billing_account=None, change_offer_purchase_entitlement=None, change_offer_purchase_new_sku=None, create_entitlement_purchase_billing_account=None, create_entitlement_purchase_sku=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_list_purchasable_offers

    Lists the following: * Offers that you can purchase for a customer. * Offers that you can change for an entitlement. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller * The reseller is not authorized to transact on this Product. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: Required request parameters are missing or invalid.

    :param customer: Required. The resource name of the customer to list Offers for. Format: accounts/{account_id}/customers/{customer_id}.
    :type customer: str
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
    :param change_offer_purchase_billing_account: Optional. Resource name of the new target Billing Account. Provide this Billing Account when setting up billing for a trial subscription. Format: accounts/{account_id}/billingAccounts/{billing_account_id}. This field is only relevant for multi-currency accounts. It should be left empty for single currency accounts.
    :type change_offer_purchase_billing_account: str
    :param change_offer_purchase_entitlement: Required. Resource name of the entitlement. Format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    :type change_offer_purchase_entitlement: str
    :param change_offer_purchase_new_sku: Optional. Resource name of the new target SKU. Provide this SKU when upgrading or downgrading an entitlement. Format: products/{product_id}/skus/{sku_id}
    :type change_offer_purchase_new_sku: str
    :param create_entitlement_purchase_billing_account: Optional. Billing account that the result should be restricted to. Format: accounts/{account_id}/billingAccounts/{billing_account_id}.
    :type create_entitlement_purchase_billing_account: str
    :param create_entitlement_purchase_sku: Required. SKU that the result should be restricted to. Format: products/{product_id}/skus/{sku_id}.
    :type create_entitlement_purchase_sku: str
    :param language_code: Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Offers. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_list_purchasable_skus(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, change_offer_purchase_change_type=None, change_offer_purchase_entitlement=None, create_entitlement_purchase_product=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_customers_list_purchasable_skus

    Lists the following: * SKUs that you can purchase for a customer * SKUs that you can upgrade or downgrade for an entitlement. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid.

    :param customer: Required. The resource name of the customer to list SKUs for. Format: accounts/{account_id}/customers/{customer_id}.
    :type customer: str
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
    :param change_offer_purchase_change_type: Required. Change Type for the entitlement.
    :type change_offer_purchase_change_type: str
    :param change_offer_purchase_entitlement: Required. Resource name of the entitlement. Format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
    :type change_offer_purchase_entitlement: str
    :param create_entitlement_purchase_product: Required. List SKUs belonging to this Product. Format: products/{product_id}. Supports products/- to retrieve SKUs for all products.
    :type create_entitlement_purchase_product: str
    :param language_code: Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_provision_cloud_identity(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_provision_cloud_identity

    Creates a Cloud Identity for the given customer using the customer&#39;s information, or the information provided here. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller. * You are not authorized to provision cloud identity id. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The customer was not found. * ALREADY_EXISTS: The customer&#39;s primary email already exists. Retry after changing the customer&#39;s primary contact email. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

    :param customer: Required. Resource name of the customer. Format: accounts/{account_id}/customers/{customer_id}
    :type customer: str
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
    body = GoogleCloudChannelV1ProvisionCloudIdentityRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_query_eligible_billing_accounts(request: web.Request, customer, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, skus=None) -> web.Response:
    """cloudchannel_accounts_customers_query_eligible_billing_accounts

    Lists the billing accounts that are eligible to purchase particular SKUs for a given customer. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: Based on the provided list of SKUs, returns a list of SKU groups that must be purchased using the same billing account and the billing accounts eligible to purchase each SKU group.

    :param customer: Required. The resource name of the customer to list eligible billing accounts for. Format: accounts/{account_id}/customers/{customer_id}.
    :type customer: str
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
    :param skus: Required. List of SKUs to list eligible billing accounts for. At least one SKU is required. Format: products/{product_id}/skus/{sku_id}.
    :type skus: List[str]

    """
    return web.Response(status=200)


async def cloudchannel_accounts_customers_transfer_entitlements(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_transfer_entitlements

    Transfers customer entitlements to new reseller. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller. * The reseller is not authorized to transact on this Product. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The customer or offer resource was not found. * ALREADY_EXISTS: The SKU was already transferred for the customer. * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * Specify all transferring entitlements. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata will contain an instance of OperationMetadata.

    :param parent: Required. The resource name of the reseller&#39;s customer account that will receive transferred entitlements. Parent uses the format: accounts/{account_id}/customers/{customer_id}
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
    body = GoogleCloudChannelV1TransferEntitlementsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_customers_transfer_entitlements_to_google(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_customers_transfer_entitlements_to_google

    Transfers customer entitlements from their current reseller to Google. Possible error codes: * PERMISSION_DENIED: The customer doesn&#39;t belong to the reseller. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The customer or offer resource was not found. * ALREADY_EXISTS: The SKU was already transferred for the customer. * CONDITION_NOT_MET or FAILED_PRECONDITION: * The SKU requires domain verification to transfer, but the domain is not verified. * An Add-On SKU (example, Vault or Drive) is missing the pre-requisite SKU (example, G Suite Basic). * (Developer accounts only) Reseller and resold domain must meet the following naming requirements: * Domain names must start with goog-test. * Domain names must include the reseller domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The response will contain google.protobuf.Empty on success. The Operation metadata will contain an instance of OperationMetadata.

    :param parent: Required. The resource name of the reseller&#39;s customer account where the entitlements transfer from. Parent uses the format: accounts/{account_id}/customers/{customer_id}
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
    body = GoogleCloudChannelV1TransferEntitlementsToGoogleRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_list_subscribers(request: web.Request, account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_list_subscribers

    Lists service accounts with subscriber privileges on the Cloud Pub/Sub topic created for this Channel Services account. Possible error codes: * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The topic resource doesn&#39;t exist. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: A list of service email addresses.

    :param account: Required. Resource name of the account.
    :type account: str
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
    :param page_size: Optional. The maximum number of service accounts to return. The service may return fewer than this value. If unspecified, returns at most 100 service accounts. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListSubscribers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscribers&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_list_transferable_offers(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_list_transferable_offers

    List TransferableOffers of a customer based on Cloud Identity ID or Customer Name in the request. Use this method when a reseller gets the entitlement information of an unowned customer. The reseller should provide the customer&#39;s Cloud Identity ID or Customer Name. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller and has no auth token. * The customer provided incorrect reseller information when generating auth token. * The reseller account making the request is different from the reseller account in the query. * The reseller is not authorized to transact on this Product. See https://support.google.com/channelservices/answer/9759265 * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: List of TransferableOffer for the given customer and SKU.

    :param parent: Required. The resource name of the reseller&#39;s account.
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
    body = GoogleCloudChannelV1ListTransferableOffersRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_list_transferable_skus(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_list_transferable_skus

    List TransferableSkus of a customer based on the Cloud Identity ID or Customer Name in the request. Use this method to list the entitlements information of an unowned customer. You should provide the customer&#39;s Cloud Identity ID or Customer Name. Possible error codes: * PERMISSION_DENIED: * The customer doesn&#39;t belong to the reseller and has no auth token. * The supplied auth token is invalid. * The reseller account making the request is different from the reseller account in the query. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: A list of the customer&#39;s TransferableSku.

    :param parent: Required. The reseller account&#39;s resource name. Parent uses the format: accounts/{account_id}
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
    body = GoogleCloudChannelV1ListTransferableSkusRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_offers_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, language_code=None, page_size=None, page_token=None, show_future_offers=None) -> web.Response:
    """cloudchannel_accounts_offers_list

    Lists the Offers the reseller can sell. Possible error codes: * INVALID_ARGUMENT: Required request parameters are missing or invalid.

    :param parent: Required. The resource name of the reseller account from which to list Offers. Parent uses the format: accounts/{account_id}.
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
    :param filter: Optional. The expression to filter results by name (name of the Offer), sku.name (name of the SKU), or sku.product.name (name of the Product). Example 1: sku.product.name&#x3D;products/p1 AND sku.name!&#x3D;products/p1/skus/s1 Example 2: name&#x3D;accounts/a1/offers/o1
    :type filter: str
    :param language_code: Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 500 Offers. The maximum value is 1000; the server will coerce values above 1000.
    :type page_size: int
    :param page_token: Optional. A token for a page of results other than the first page.
    :type page_token: str
    :param show_future_offers: Optional. A boolean flag that determines if a response returns future offers 30 days from now. If the show_future_offers is true, the response will only contain offers that are scheduled to be available 30 days from now.
    :type show_future_offers: bool

    """
    return web.Response(status=200)


async def cloudchannel_accounts_register(request: web.Request, account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_register

    Registers a service account with subscriber privileges on the Cloud Pub/Sub topic for this Channel Services account. After you create a subscriber, you get the events through SubscriberEvent Possible error codes: * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The topic name with the registered service email address.

    :param account: Required. Resource name of the account.
    :type account: str
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
    body = GoogleCloudChannelV1RegisterSubscriberRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_report_jobs_fetch_report_results(request: web.Request, report_job, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_report_jobs_fetch_report_results

    Retrieves data generated by CloudChannelReportsService.RunReportJob. Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

    :param report_job: Required. The report job created by CloudChannelReportsService.RunReportJob. Report_job uses the format: accounts/{account_id}/reportJobs/{report_job_id}
    :type report_job: str
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
    body = GoogleCloudChannelV1FetchReportResultsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_reports_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_reports_list

    Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result. Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

    :param parent: Required. The resource name of the partner account to list available reports for. Parent uses the format: accounts/{account_id}
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
    :param language_code: Optional. The BCP-47 language code, such as \&quot;en-US\&quot;. If specified, the response is localized to the corresponding language code if the original data sources support it. Default is \&quot;en-US\&quot;.
    :type language_code: str
    :param page_size: Optional. Requested page size of the report. The server might return fewer results than requested. If unspecified, returns 20 reports. The maximum value is 100.
    :type page_size: int
    :param page_token: Optional. A token that specifies a page of results beyond the first page. Obtained through ListReportsResponse.next_page_token of the previous CloudChannelReportsService.ListReports call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_reports_run(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_reports_run

    Begins generation of data for a given report. The report identifier is a UID (for example, &#x60;613bf59q&#x60;). Possible error codes: * PERMISSION_DENIED: The user doesn&#39;t have access to this report. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The report identifier was not found. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The ID of a long-running operation. To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata. To get the results of report generation, call CloudChannelReportsService.FetchReportResults with the RunReportJobResponse.report_job. Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

    :param name: Required. The report&#39;s resource name. Specifies the account and report used to generate report data. The report_id identifier is a UID (for example, &#x60;613bf59q&#x60;). Name uses the format: accounts/{account_id}/reports/{report_id}
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
    body = GoogleCloudChannelV1RunReportJobRequest.from_dict(body)
    return web.Response(status=200)


async def cloudchannel_accounts_sku_groups_billable_skus_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_sku_groups_billable_skus_list

    Lists the Billable SKUs in a given SKU group. Possible error codes: PERMISSION_DENIED: If the account making the request and the account being queried for are different, or the account doesn&#39;t exist. INVALID_ARGUMENT: Missing or invalid required parameters in the request. INTERNAL: Any non-user error related to technical issue in the backend. In this case, contact cloud channel support. Return Value: If successful, the BillableSku resources. The data for each resource is displayed in the ascending order of: * BillableSku.service_display_name * BillableSku.sku_display_name If unsuccessful, returns an error.

    :param parent: Required. Resource name of the SKU group. Format: accounts/{account}/skuGroups/{sku_group}.
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
    :param page_size: Optional. The maximum number of SKUs to return. The service may return fewer than this value. If unspecified, returns a maximum of 100000 SKUs. The maximum value is 100000; values above 100000 will be coerced to 100000.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results beyond the first page. Obtained through ListSkuGroupBillableSkus.next_page_token of the previous CloudChannelService.ListSkuGroupBillableSkus call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_sku_groups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudchannel_accounts_sku_groups_list

    Lists the Rebilling supported SKU groups the account is authorized to sell. Reference: https://cloud.google.com/skus/sku-groups Possible Error Codes: * PERMISSION_DENIED: If the account making the request and the account being queried are different, or the account doesn&#39;t exist. * INTERNAL: Any non-user error related to technical issues in the backend. In this case, contact Cloud Channel support. Return Value: If successful, the SkuGroup resources. The data for each resource is displayed in the alphabetical order of SKU group display name. The data for each resource is displayed in the ascending order of SkuGroup.display_name If unsuccessful, returns an error.

    :param parent: Required. The resource name of the account from which to list SKU groups. Parent uses the format: accounts/{account}.
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
    :param page_size: Optional. The maximum number of SKU groups to return. The service may return fewer than this value. If unspecified, returns a maximum of 1000 SKU groups. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results beyond the first page. Obtained through ListSkuGroups.next_page_token of the previous CloudChannelService.ListSkuGroups call.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudchannel_accounts_unregister(request: web.Request, account, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudchannel_accounts_unregister

    Unregisters a service account with subscriber privileges on the Cloud Pub/Sub topic created for this Channel Services account. If there are no service accounts left with subscriber privileges, this deletes the topic. You can call ListSubscribers to check for these accounts. Possible error codes: * PERMISSION_DENIED: The reseller account making the request and the provided reseller account are different, or the impersonated user is not a super admin. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: The topic resource doesn&#39;t exist. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The topic name that unregistered the service email address. Returns a success response if the service email address wasn&#39;t registered with the topic.

    :param account: Required. Resource name of the account.
    :type account: str
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
    body = GoogleCloudChannelV1UnregisterSubscriberRequest.from_dict(body)
    return web.Response(status=200)
