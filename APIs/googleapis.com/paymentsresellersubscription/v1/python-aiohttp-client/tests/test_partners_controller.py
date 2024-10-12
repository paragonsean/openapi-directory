# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_payments_reseller_subscription_v1_cancel_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_cancel_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_entitle_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_entitle_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_extend_subscription_request import GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_extend_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_find_eligible_promotions_request import GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_find_eligible_promotions_response import GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_list_products_response import GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_list_promotions_response import GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_subscription import GoogleCloudPaymentsResellerSubscriptionV1Subscription
from openapi_server.models.google_cloud_payments_reseller_subscription_v1_undo_cancel_subscription_response import GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_products_list(client):
    """Test case for paymentsresellersubscription_partners_products_list

    
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
        path='/v1/{parent}/products'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_promotions_find_eligible(client):
    """Test case for paymentsresellersubscription_partners_promotions_find_eligible

    
    """
    body = {"filter":"filter","pageSize":0,"pageToken":"pageToken"}
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
        path='/v1/{parent}/promotions:findEligible'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_promotions_list(client):
    """Test case for paymentsresellersubscription_partners_promotions_list

    
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
        path='/v1/{parent}/promotions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_cancel(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_cancel

    
    """
    body = {"cancelImmediately":True,"cancellationReason":"CANCELLATION_REASON_UNSPECIFIED"}
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_create(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_create

    
    """
    body = {"redirectUri":"redirectUri","serviceLocation":{"regionCode":"regionCode","postalCode":"postalCode"},"upgradeDowngradeDetails":{"previousSubscriptionId":"previousSubscriptionId","billingCycleSpec":"BILLING_CYCLE_SPEC_UNSPECIFIED"},"partnerUserToken":"partnerUserToken","updateTime":"updateTime","products":["products","products"],"lineItems":[{"lineItemIndex":0,"amount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"product":"product","lineItemPromotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"bundleDetails":{"bundleElementDetails":[{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"},{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"}]},"description":"description","finiteBillingCycleDetails":{"billingCycleCountLimit":"billingCycleCountLimit"},"lineItemFreeTrialEndTime":"lineItemFreeTrialEndTime","oneTimeRecurrenceDetails":{"servicePeriod":{"startTime":"startTime","endTime":"endTime"}},"state":"LINE_ITEM_STATE_UNSPECIFIED","productPayload":{"googleOnePayload":{"campaigns":["campaigns","campaigns"],"offering":"OFFERING_UNSPECIFIED","salesChannel":"CHANNEL_UNSPECIFIED","storeId":"storeId"},"youtubePayload":{"accessEndTime":"accessEndTime","partnerEligibilityIds":["partnerEligibilityIds","partnerEligibilityIds"],"partnerPlanType":"PARTNER_PLAN_TYPE_UNSPECIFIED"}},"recurrenceType":"LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED"},{"lineItemIndex":0,"amount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"product":"product","lineItemPromotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"bundleDetails":{"bundleElementDetails":[{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"},{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"}]},"description":"description","finiteBillingCycleDetails":{"billingCycleCountLimit":"billingCycleCountLimit"},"lineItemFreeTrialEndTime":"lineItemFreeTrialEndTime","oneTimeRecurrenceDetails":{"servicePeriod":{"startTime":"startTime","endTime":"endTime"}},"state":"LINE_ITEM_STATE_UNSPECIFIED","productPayload":{"googleOnePayload":{"campaigns":["campaigns","campaigns"],"offering":"OFFERING_UNSPECIFIED","salesChannel":"CHANNEL_UNSPECIFIED","storeId":"storeId"},"youtubePayload":{"accessEndTime":"accessEndTime","partnerEligibilityIds":["partnerEligibilityIds","partnerEligibilityIds"],"partnerPlanType":"PARTNER_PLAN_TYPE_UNSPECIFIED"}},"recurrenceType":"LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED"}],"cycleEndTime":"cycleEndTime","processingState":"PROCESSING_STATE_UNSPECIFIED","renewalTime":"renewalTime","promotions":["promotions","promotions"],"createTime":"createTime","cancellationDetails":{"reason":"CANCELLATION_REASON_UNSPECIFIED"},"name":"name","promotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"state":"STATE_UNSPECIFIED","endUserEntitled":True,"freeTrialEndTime":"freeTrialEndTime"}
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
                    ('subscriptionId', 'subscription_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/subscriptions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_entitle(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_entitle

    
    """
    body = {"lineItemEntitlementDetails":[{"lineItemIndex":0,"products":["products","products"]},{"lineItemIndex":0,"products":["products","products"]}]}
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
        path='/v1/{nameentitl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_extend(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_extend

    
    """
    body = {"extension":{"duration":{"unit":"UNIT_UNSPECIFIED","count":6},"partnerUserToken":"partnerUserToken"},"requestId":"requestId"}
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
        path='/v1/{nameexten}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_get(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_provision(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_provision

    
    """
    body = {"redirectUri":"redirectUri","serviceLocation":{"regionCode":"regionCode","postalCode":"postalCode"},"upgradeDowngradeDetails":{"previousSubscriptionId":"previousSubscriptionId","billingCycleSpec":"BILLING_CYCLE_SPEC_UNSPECIFIED"},"partnerUserToken":"partnerUserToken","updateTime":"updateTime","products":["products","products"],"lineItems":[{"lineItemIndex":0,"amount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"product":"product","lineItemPromotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"bundleDetails":{"bundleElementDetails":[{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"},{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"}]},"description":"description","finiteBillingCycleDetails":{"billingCycleCountLimit":"billingCycleCountLimit"},"lineItemFreeTrialEndTime":"lineItemFreeTrialEndTime","oneTimeRecurrenceDetails":{"servicePeriod":{"startTime":"startTime","endTime":"endTime"}},"state":"LINE_ITEM_STATE_UNSPECIFIED","productPayload":{"googleOnePayload":{"campaigns":["campaigns","campaigns"],"offering":"OFFERING_UNSPECIFIED","salesChannel":"CHANNEL_UNSPECIFIED","storeId":"storeId"},"youtubePayload":{"accessEndTime":"accessEndTime","partnerEligibilityIds":["partnerEligibilityIds","partnerEligibilityIds"],"partnerPlanType":"PARTNER_PLAN_TYPE_UNSPECIFIED"}},"recurrenceType":"LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED"},{"lineItemIndex":0,"amount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"product":"product","lineItemPromotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"bundleDetails":{"bundleElementDetails":[{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"},{"product":"product","userAccountLinkedTime":"userAccountLinkedTime"}]},"description":"description","finiteBillingCycleDetails":{"billingCycleCountLimit":"billingCycleCountLimit"},"lineItemFreeTrialEndTime":"lineItemFreeTrialEndTime","oneTimeRecurrenceDetails":{"servicePeriod":{"startTime":"startTime","endTime":"endTime"}},"state":"LINE_ITEM_STATE_UNSPECIFIED","productPayload":{"googleOnePayload":{"campaigns":["campaigns","campaigns"],"offering":"OFFERING_UNSPECIFIED","salesChannel":"CHANNEL_UNSPECIFIED","storeId":"storeId"},"youtubePayload":{"accessEndTime":"accessEndTime","partnerEligibilityIds":["partnerEligibilityIds","partnerEligibilityIds"],"partnerPlanType":"PARTNER_PLAN_TYPE_UNSPECIFIED"}},"recurrenceType":"LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED"}],"cycleEndTime":"cycleEndTime","processingState":"PROCESSING_STATE_UNSPECIFIED","renewalTime":"renewalTime","promotions":["promotions","promotions"],"createTime":"createTime","cancellationDetails":{"reason":"CANCELLATION_REASON_UNSPECIFIED"},"name":"name","promotionSpecs":[{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"},{"freeTrialDuration":{"unit":"UNIT_UNSPECIFIED","count":6},"type":"PROMOTION_TYPE_UNSPECIFIED","introductoryPricingDetails":{"introductoryPricingSpecs":[{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1},{"discountRatioMicros":"discountRatioMicros","regionCode":"regionCode","discountAmount":{"amountMicros":"amountMicros","currencyCode":"currencyCode"},"recurrenceCount":1}]},"promotion":"promotion"}],"state":"STATE_UNSPECIFIED","endUserEntitled":True,"freeTrialEndTime":"freeTrialEndTime"}
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
                    ('subscriptionId', 'subscription_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/subscriptions:provision'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_paymentsresellersubscription_partners_subscriptions_undo_cancel(client):
    """Test case for paymentsresellersubscription_partners_subscriptions_undo_cancel

    
    """
    body = None
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
        path='/v1/{nameundo_cance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

