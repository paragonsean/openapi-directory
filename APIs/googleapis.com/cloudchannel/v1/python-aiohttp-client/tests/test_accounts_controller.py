# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_create(client):
    """Test case for cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_create

    
    """
    body = {"repricingConfig":{"effectiveInvoiceMonth":{"month":6,"year":1,"day":0},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED","channelPartnerGranularity":"{}","conditionalOverrides":[{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"},{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"}],"entitlementGranularity":{"entitlement":"entitlement"}},"name":"name","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/channelPartnerRepricingConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_list(client):
    """Test case for cloudchannel_accounts_channel_partner_links_channel_partner_repricing_configs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/channelPartnerRepricingConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_channel_partner_links_create(client):
    """Test case for cloudchannel_accounts_channel_partner_links_create

    
    """
    body = {"linkState":"CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED","inviteLinkUri":"inviteLinkUri","createTime":"createTime","channelPartnerCloudIdentityInfo":{"alternateEmail":"alternateEmail","customerType":"CUSTOMER_TYPE_UNSPECIFIED","phoneNumber":"phoneNumber","primaryDomain":"primaryDomain","adminConsoleUri":"adminConsoleUri","eduData":{"website":"website","instituteSize":"INSTITUTE_SIZE_UNSPECIFIED","instituteType":"INSTITUTE_TYPE_UNSPECIFIED"},"isDomainVerified":True,"languageCode":"languageCode"},"name":"name","updateTime":"updateTime","publicId":"publicId","resellerCloudIdentityId":"resellerCloudIdentityId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/channelPartnerLinks'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_channel_partner_links_list(client):
    """Test case for cloudchannel_accounts_channel_partner_links_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/channelPartnerLinks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_check_cloud_identity_accounts_exist(client):
    """Test case for cloudchannel_accounts_check_cloud_identity_accounts_exist

    
    """
    body = {"domain":"domain"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentcheck_cloud_identity_accounts_exis}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_create(client):
    """Test case for cloudchannel_accounts_customers_create

    
    """
    body = {"alternateEmail":"alternateEmail","primaryContactInfo":{"firstName":"firstName","lastName":"lastName","phone":"phone","displayName":"displayName","title":"title","email":"email"},"updateTime":"updateTime","cloudIdentityId":"cloudIdentityId","languageCode":"languageCode","orgPostalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0},"createTime":"createTime","domain":"domain","channelPartnerId":"channelPartnerId","name":"name","correlationId":"correlationId","orgDisplayName":"orgDisplayName","cloudIdentityInfo":{"alternateEmail":"alternateEmail","customerType":"CUSTOMER_TYPE_UNSPECIFIED","phoneNumber":"phoneNumber","primaryDomain":"primaryDomain","adminConsoleUri":"adminConsoleUri","eduData":{"website":"website","instituteSize":"INSTITUTE_SIZE_UNSPECIFIED","instituteType":"INSTITUTE_TYPE_UNSPECIFIED"},"isDomainVerified":True,"languageCode":"languageCode"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_customer_repricing_configs_create(client):
    """Test case for cloudchannel_accounts_customers_customer_repricing_configs_create

    
    """
    body = {"repricingConfig":{"effectiveInvoiceMonth":{"month":6,"year":1,"day":0},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED","channelPartnerGranularity":"{}","conditionalOverrides":[{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"},{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"}],"entitlementGranularity":{"entitlement":"entitlement"}},"name":"name","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customerRepricingConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_customer_repricing_configs_list(client):
    """Test case for cloudchannel_accounts_customers_customer_repricing_configs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customerRepricingConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_customer_repricing_configs_patch(client):
    """Test case for cloudchannel_accounts_customers_customer_repricing_configs_patch

    
    """
    body = {"repricingConfig":{"effectiveInvoiceMonth":{"month":6,"year":1,"day":0},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED","channelPartnerGranularity":"{}","conditionalOverrides":[{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"},{"repricingCondition":{"skuGroupCondition":{"skuGroup":"skuGroup"}},"adjustment":{"percentageAdjustment":{"percentage":{"value":"value"}}},"rebillingBasis":"REBILLING_BASIS_UNSPECIFIED"}],"entitlementGranularity":{"entitlement":"entitlement"}},"name":"name","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_activate(client):
    """Test case for cloudchannel_accounts_customers_entitlements_activate

    
    """
    body = {"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameactivat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_change_offer(client):
    """Test case for cloudchannel_accounts_customers_entitlements_change_offer

    
    """
    body = {"offer":"offer","purchaseOrderId":"purchaseOrderId","requestId":"requestId","billingAccount":"billingAccount","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namechange_offe}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_change_parameters(client):
    """Test case for cloudchannel_accounts_customers_entitlements_change_parameters

    
    """
    body = {"purchaseOrderId":"purchaseOrderId","requestId":"requestId","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namechange_parameter}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_change_renewal_settings(client):
    """Test case for cloudchannel_accounts_customers_entitlements_change_renewal_settings

    
    """
    body = {"requestId":"requestId","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namechange_renewal_setting}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_create(client):
    """Test case for cloudchannel_accounts_customers_entitlements_create

    
    """
    body = {"requestId":"requestId","entitlement":{"commitmentSettings":{"startTime":"startTime","endTime":"endTime","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}},"updateTime":"updateTime","provisioningState":"PROVISIONING_STATE_UNSPECIFIED","billingAccount":"billingAccount","trialSettings":{"endTime":"endTime","trial":True},"offer":"offer","createTime":"createTime","provisionedService":{"productId":"productId","provisioningId":"provisioningId","skuId":"skuId"},"suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"purchaseOrderId":"purchaseOrderId","associationInfo":{"baseEntitlement":"baseEntitlement"},"name":"name","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/entitlements'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_list(client):
    """Test case for cloudchannel_accounts_customers_entitlements_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/entitlements'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_list_entitlement_changes(client):
    """Test case for cloudchannel_accounts_customers_entitlements_list_entitlement_changes

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parentlist_entitlement_change}'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_lookup_offer(client):
    """Test case for cloudchannel_accounts_customers_entitlements_lookup_offer

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{entitlementlookup_offe}'.format(entitlement='entitlement_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_start_paid_service(client):
    """Test case for cloudchannel_accounts_customers_entitlements_start_paid_service

    
    """
    body = {"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namestart_paid_servic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_entitlements_suspend(client):
    """Test case for cloudchannel_accounts_customers_entitlements_suspend

    
    """
    body = {"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namesuspen}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_import(client):
    """Test case for cloudchannel_accounts_customers_import

    
    """
    body = {"authToken":"authToken","domain":"domain","channelPartnerId":"channelPartnerId","overwriteIfExists":True,"cloudIdentityId":"cloudIdentityId","customer":"customer"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customers:import'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_list(client):
    """Test case for cloudchannel_accounts_customers_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_list_purchasable_offers(client):
    """Test case for cloudchannel_accounts_customers_list_purchasable_offers

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('changeOfferPurchase.billingAccount', 'change_offer_purchase_billing_account_example'),
                    ('changeOfferPurchase.entitlement', 'change_offer_purchase_entitlement_example'),
                    ('changeOfferPurchase.newSku', 'change_offer_purchase_new_sku_example'),
                    ('createEntitlementPurchase.billingAccount', 'create_entitlement_purchase_billing_account_example'),
                    ('createEntitlementPurchase.sku', 'create_entitlement_purchase_sku_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{customerlist_purchasable_offer}'.format(customer='customer_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_list_purchasable_skus(client):
    """Test case for cloudchannel_accounts_customers_list_purchasable_skus

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('changeOfferPurchase.changeType', 'change_offer_purchase_change_type_example'),
                    ('changeOfferPurchase.entitlement', 'change_offer_purchase_entitlement_example'),
                    ('createEntitlementPurchase.product', 'create_entitlement_purchase_product_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{customerlist_purchasable_sku}'.format(customer='customer_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_provision_cloud_identity(client):
    """Test case for cloudchannel_accounts_customers_provision_cloud_identity

    
    """
    body = {"validateOnly":True,"cloudIdentityInfo":{"alternateEmail":"alternateEmail","customerType":"CUSTOMER_TYPE_UNSPECIFIED","phoneNumber":"phoneNumber","primaryDomain":"primaryDomain","adminConsoleUri":"adminConsoleUri","eduData":{"website":"website","instituteSize":"INSTITUTE_SIZE_UNSPECIFIED","instituteType":"INSTITUTE_TYPE_UNSPECIFIED"},"isDomainVerified":True,"languageCode":"languageCode"},"user":{"familyName":"familyName","givenName":"givenName","email":"email"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{customerprovision_cloud_identit}'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_query_eligible_billing_accounts(client):
    """Test case for cloudchannel_accounts_customers_query_eligible_billing_accounts

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('skus', ['skus_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{customerquery_eligible_billing_account}'.format(customer='customer_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_transfer_entitlements(client):
    """Test case for cloudchannel_accounts_customers_transfer_entitlements

    
    """
    body = {"entitlements":[{"commitmentSettings":{"startTime":"startTime","endTime":"endTime","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}},"updateTime":"updateTime","provisioningState":"PROVISIONING_STATE_UNSPECIFIED","billingAccount":"billingAccount","trialSettings":{"endTime":"endTime","trial":True},"offer":"offer","createTime":"createTime","provisionedService":{"productId":"productId","provisioningId":"provisioningId","skuId":"skuId"},"suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"purchaseOrderId":"purchaseOrderId","associationInfo":{"baseEntitlement":"baseEntitlement"},"name":"name","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]},{"commitmentSettings":{"startTime":"startTime","endTime":"endTime","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}},"updateTime":"updateTime","provisioningState":"PROVISIONING_STATE_UNSPECIFIED","billingAccount":"billingAccount","trialSettings":{"endTime":"endTime","trial":True},"offer":"offer","createTime":"createTime","provisionedService":{"productId":"productId","provisioningId":"provisioningId","skuId":"skuId"},"suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"purchaseOrderId":"purchaseOrderId","associationInfo":{"baseEntitlement":"baseEntitlement"},"name":"name","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]}],"requestId":"requestId","authToken":"authToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parenttransfer_entitlement}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_customers_transfer_entitlements_to_google(client):
    """Test case for cloudchannel_accounts_customers_transfer_entitlements_to_google

    
    """
    body = {"entitlements":[{"commitmentSettings":{"startTime":"startTime","endTime":"endTime","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}},"updateTime":"updateTime","provisioningState":"PROVISIONING_STATE_UNSPECIFIED","billingAccount":"billingAccount","trialSettings":{"endTime":"endTime","trial":True},"offer":"offer","createTime":"createTime","provisionedService":{"productId":"productId","provisioningId":"provisioningId","skuId":"skuId"},"suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"purchaseOrderId":"purchaseOrderId","associationInfo":{"baseEntitlement":"baseEntitlement"},"name":"name","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]},{"commitmentSettings":{"startTime":"startTime","endTime":"endTime","renewalSettings":{"enableRenewal":True,"paymentPlan":"PAYMENT_PLAN_UNSPECIFIED","resizeUnitCount":True,"paymentCycle":{"duration":6,"periodType":"PERIOD_TYPE_UNSPECIFIED"}}},"updateTime":"updateTime","provisioningState":"PROVISIONING_STATE_UNSPECIFIED","billingAccount":"billingAccount","trialSettings":{"endTime":"endTime","trial":True},"offer":"offer","createTime":"createTime","provisionedService":{"productId":"productId","provisioningId":"provisioningId","skuId":"skuId"},"suspensionReasons":["SUSPENSION_REASON_UNSPECIFIED","SUSPENSION_REASON_UNSPECIFIED"],"purchaseOrderId":"purchaseOrderId","associationInfo":{"baseEntitlement":"baseEntitlement"},"name":"name","parameters":[{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}},{"editable":True,"name":"name","value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"protoValue":{"key":""},"doubleValue":0.8008281904610115}}]}],"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parenttransfer_entitlements_to_googl}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_list_subscribers(client):
    """Test case for cloudchannel_accounts_list_subscribers

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{accountlist_subscriber}'.format(account='account_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_list_transferable_offers(client):
    """Test case for cloudchannel_accounts_list_transferable_offers

    
    """
    body = {"pageSize":0,"pageToken":"pageToken","billingAccount":"billingAccount","cloudIdentityId":"cloudIdentityId","languageCode":"languageCode","sku":"sku","customerName":"customerName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentlist_transferable_offer}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_list_transferable_skus(client):
    """Test case for cloudchannel_accounts_list_transferable_skus

    
    """
    body = {"authToken":"authToken","pageSize":0,"pageToken":"pageToken","cloudIdentityId":"cloudIdentityId","languageCode":"languageCode","customerName":"customerName"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentlist_transferable_sku}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_offers_list(client):
    """Test case for cloudchannel_accounts_offers_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('showFutureOffers', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/offers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_register(client):
    """Test case for cloudchannel_accounts_register

    
    """
    body = {"serviceAccount":"serviceAccount"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{accountregiste}'.format(account='account_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_report_jobs_fetch_report_results(client):
    """Test case for cloudchannel_accounts_report_jobs_fetch_report_results

    
    """
    body = {"pageSize":0,"pageToken":"pageToken","partitionKeys":["partitionKeys","partitionKeys"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{report_jobfetch_report_result}'.format(report_job='report_job_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_reports_list(client):
    """Test case for cloudchannel_accounts_reports_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/reports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_reports_run(client):
    """Test case for cloudchannel_accounts_reports_run

    
    """
    body = {"filter":"filter","dateRange":{"usageEndDateTime":{"hours":5,"seconds":3,"utcOffset":"utcOffset","month":7,"nanos":9,"year":2,"minutes":2,"timeZone":{"id":"id","version":"version"},"day":5},"usageStartDateTime":{"hours":5,"seconds":3,"utcOffset":"utcOffset","month":7,"nanos":9,"year":2,"minutes":2,"timeZone":{"id":"id","version":"version"},"day":5},"invoiceEndDate":{"month":6,"year":1,"day":0},"invoiceStartDate":{"month":6,"year":1,"day":0}},"languageCode":"languageCode"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_sku_groups_billable_skus_list(client):
    """Test case for cloudchannel_accounts_sku_groups_billable_skus_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/billableSkus'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_sku_groups_list(client):
    """Test case for cloudchannel_accounts_sku_groups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/skuGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudchannel_accounts_unregister(client):
    """Test case for cloudchannel_accounts_unregister

    
    """
    body = {"serviceAccount":"serviceAccount"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{accountunregiste}'.format(account='account_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

