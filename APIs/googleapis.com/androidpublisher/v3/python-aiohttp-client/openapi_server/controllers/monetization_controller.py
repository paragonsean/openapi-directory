from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_base_plan_request import ActivateBasePlanRequest
from openapi_server.models.activate_subscription_offer_request import ActivateSubscriptionOfferRequest
from openapi_server.models.batch_get_subscription_offers_request import BatchGetSubscriptionOffersRequest
from openapi_server.models.batch_get_subscription_offers_response import BatchGetSubscriptionOffersResponse
from openapi_server.models.batch_get_subscriptions_response import BatchGetSubscriptionsResponse
from openapi_server.models.batch_migrate_base_plan_prices_request import BatchMigrateBasePlanPricesRequest
from openapi_server.models.batch_migrate_base_plan_prices_response import BatchMigrateBasePlanPricesResponse
from openapi_server.models.batch_update_base_plan_states_request import BatchUpdateBasePlanStatesRequest
from openapi_server.models.batch_update_base_plan_states_response import BatchUpdateBasePlanStatesResponse
from openapi_server.models.batch_update_subscription_offer_states_request import BatchUpdateSubscriptionOfferStatesRequest
from openapi_server.models.batch_update_subscription_offer_states_response import BatchUpdateSubscriptionOfferStatesResponse
from openapi_server.models.batch_update_subscription_offers_request import BatchUpdateSubscriptionOffersRequest
from openapi_server.models.batch_update_subscription_offers_response import BatchUpdateSubscriptionOffersResponse
from openapi_server.models.batch_update_subscriptions_request import BatchUpdateSubscriptionsRequest
from openapi_server.models.batch_update_subscriptions_response import BatchUpdateSubscriptionsResponse
from openapi_server.models.convert_region_prices_request import ConvertRegionPricesRequest
from openapi_server.models.convert_region_prices_response import ConvertRegionPricesResponse
from openapi_server.models.deactivate_base_plan_request import DeactivateBasePlanRequest
from openapi_server.models.deactivate_subscription_offer_request import DeactivateSubscriptionOfferRequest
from openapi_server.models.list_subscription_offers_response import ListSubscriptionOffersResponse
from openapi_server.models.list_subscriptions_response import ListSubscriptionsResponse
from openapi_server.models.migrate_base_plan_prices_request import MigrateBasePlanPricesRequest
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_offer import SubscriptionOffer
from openapi_server import util


async def androidpublisher_monetization_convert_region_prices(request: web.Request, package_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_convert_region_prices

    Calculates the region prices, using today&#39;s exchange rate and country-specific pricing patterns, based on the price in the request for a set of regions.

    :param package_name: Required. The app package name.
    :type package_name: str
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
    body = ConvertRegionPricesRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_archive(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_archive

    Deprecated: subscription archiving is not supported.

    :param package_name: Required. The parent app (package name) of the app of the subscription to delete.
    :type package_name: str
    :param product_id: Required. The unique product ID of the subscription to delete.
    :type product_id: str
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


async def androidpublisher_monetization_subscriptions_base_plans_activate(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_activate

    Activates a base plan. Once activated, base plans will be available to new subscribers.

    :param package_name: Required. The parent app (package name) of the base plan to activate.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the base plan to activate.
    :type product_id: str
    :param base_plan_id: Required. The unique base plan ID of the base plan to activate.
    :type base_plan_id: str
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
    body = ActivateBasePlanRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_batch_migrate_prices(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_batch_migrate_prices

    Batch variant of the MigrateBasePlanPrices endpoint. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources.
    :type package_name: str
    :param product_id: Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set.
    :type product_id: str
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
    body = BatchMigrateBasePlanPricesRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_batch_update_states(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_batch_update_states

    Activates or deactivates base plans across one or multiple subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

    :param package_name: Required. The parent app (package name) of the updated base plans.
    :type package_name: str
    :param product_id: Required. The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set.
    :type product_id: str
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
    body = BatchUpdateBasePlanStatesRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_deactivate(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_deactivate

    Deactivates a base plan. Once deactivated, the base plan will become unavailable to new subscribers, but existing subscribers will maintain their subscription

    :param package_name: Required. The parent app (package name) of the base plan to deactivate.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the base plan to deactivate.
    :type product_id: str
    :param base_plan_id: Required. The unique base plan ID of the base plan to deactivate.
    :type base_plan_id: str
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
    body = DeactivateBasePlanRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_delete(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_delete

    Deletes a base plan. Can only be done for draft base plans. This action is irreversible.

    :param package_name: Required. The parent app (package name) of the base plan to delete.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the base plan to delete.
    :type product_id: str
    :param base_plan_id: Required. The unique offer ID of the base plan to delete.
    :type base_plan_id: str
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


async def androidpublisher_monetization_subscriptions_base_plans_migrate_prices(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_migrate_prices

    Migrates subscribers who are receiving an historical subscription price to the currently-offered price for the specified region. Requests will cause price change notifications to be sent to users who are currently receiving an historical price older than the supplied timestamp. Subscribers who do not agree to the new price will have their subscription ended at the next renewal.

    :param package_name: Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource.
    :type package_name: str
    :param product_id: Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource.
    :type product_id: str
    :param base_plan_id: Required. The unique base plan ID of the base plan to update prices on.
    :type base_plan_id: str
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
    body = MigrateBasePlanPricesRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_activate(request: web.Request, package_name, product_id, base_plan_id, offer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_activate

    Activates a subscription offer. Once activated, subscription offers will be available to new subscribers.

    :param package_name: Required. The parent app (package name) of the offer to activate.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the offer to activate.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) of the offer to activate.
    :type base_plan_id: str
    :param offer_id: Required. The unique offer ID of the offer to activate.
    :type offer_id: str
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
    body = ActivateSubscriptionOfferRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_batch_get(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_batch_get

    Reads one or more subscription offers.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests.
    :type package_name: str
    :param product_id: Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read offers from multiple base plans.
    :type base_plan_id: str
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
    body = BatchGetSubscriptionOffersRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_batch_update(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_batch_update

    Updates a batch of subscription offers. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

    :param package_name: Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
    :type package_name: str
    :param product_id: Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans.
    :type base_plan_id: str
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
    body = BatchUpdateSubscriptionOffersRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_batch_update_states(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_batch_update_states

    Updates a batch of subscription offer states. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

    :param package_name: Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
    :type package_name: str
    :param product_id: Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans.
    :type base_plan_id: str
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
    body = BatchUpdateSubscriptionOfferStatesRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_create(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, offer_id=None, regions_version_version=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_create

    Creates a new subscription offer. Only auto-renewing base plans can have subscription offers. The offer state will be DRAFT until it is activated.

    :param package_name: Required. The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource.
    :type base_plan_id: str
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
    :param offer_id: Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource.
    :type offer_id: str
    :param regions_version_version: Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    :type regions_version_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionOffer.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_deactivate(request: web.Request, package_name, product_id, base_plan_id, offer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_deactivate

    Deactivates a subscription offer. Once deactivated, existing subscribers will maintain their subscription, but the offer will become unavailable to new subscribers.

    :param package_name: Required. The parent app (package name) of the offer to deactivate.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the offer to deactivate.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) of the offer to deactivate.
    :type base_plan_id: str
    :param offer_id: Required. The unique offer ID of the offer to deactivate.
    :type offer_id: str
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
    body = DeactivateSubscriptionOfferRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_delete(request: web.Request, package_name, product_id, base_plan_id, offer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_delete

    Deletes a subscription offer. Can only be done for draft offers. This action is irreversible.

    :param package_name: Required. The parent app (package name) of the offer to delete.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the offer to delete.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) of the offer to delete.
    :type base_plan_id: str
    :param offer_id: Required. The unique offer ID of the offer to delete.
    :type offer_id: str
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


async def androidpublisher_monetization_subscriptions_base_plans_offers_get(request: web.Request, package_name, product_id, base_plan_id, offer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_get

    Reads a single offer

    :param package_name: Required. The parent app (package name) of the offer to get.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) of the offer to get.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) of the offer to get.
    :type base_plan_id: str
    :param offer_id: Required. The unique offer ID of the offer to get.
    :type offer_id: str
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


async def androidpublisher_monetization_subscriptions_base_plans_offers_list(request: web.Request, package_name, product_id, base_plan_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_list

    Lists all offers under a given subscription.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be read.
    :type package_name: str
    :param product_id: Required. The parent subscription (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under an app.
    :type product_id: str
    :param base_plan_id: Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under a subscription or an app. Must be specified as &#39;-&#39; if product_id is specified as &#39;-&#39;.
    :type base_plan_id: str
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
    :param page_size: The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSubscriptionsOffers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptionOffers&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_base_plans_offers_patch(request: web.Request, package_name, product_id, base_plan_id, offer_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_missing=None, latency_tolerance=None, regions_version_version=None, update_mask=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_base_plans_offers_patch

    Updates an existing subscription offer.

    :param package_name: Required. Immutable. The package name of the app the parent subscription belongs to.
    :type package_name: str
    :param product_id: Required. Immutable. The ID of the parent subscription this offer belongs to.
    :type product_id: str
    :param base_plan_id: Required. Immutable. The ID of the base plan to which this offer is an extension.
    :type base_plan_id: str
    :param offer_id: Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan.
    :type offer_id: str
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
    :param allow_missing: Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn&#39;t exist, an offer will be created. If a new offer is created, update_mask is ignored.
    :type allow_missing: bool
    :param latency_tolerance: Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
    :type latency_tolerance: str
    :param regions_version_version: Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    :type regions_version_version: str
    :param update_mask: Required. The list of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionOffer.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_batch_get(request: web.Request, package_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, product_ids=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_batch_get

    Reads one or more subscriptions.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests.
    :type package_name: str
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
    :param product_ids: Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different.
    :type product_ids: List[str]

    """
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_batch_update(request: web.Request, package_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_batch_update

    Updates a batch of subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources.
    :type package_name: str
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
    body = BatchUpdateSubscriptionsRequest.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_create(request: web.Request, package_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, product_id=None, regions_version_version=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_create

    Creates a new subscription. Newly added base plans will remain in draft state until activated.

    :param package_name: Required. The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource.
    :type package_name: str
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
    :param product_id: Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource.
    :type product_id: str
    :param regions_version_version: Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    :type regions_version_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_delete(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_delete

    Deletes a subscription. A subscription can only be deleted if it has never had a base plan published.

    :param package_name: Required. The parent app (package name) of the app of the subscription to delete.
    :type package_name: str
    :param product_id: Required. The unique product ID of the subscription to delete.
    :type product_id: str
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


async def androidpublisher_monetization_subscriptions_get(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_get

    Reads a single subscription.

    :param package_name: Required. The parent app (package name) of the subscription to get.
    :type package_name: str
    :param product_id: Required. The unique product ID of the subscription to get.
    :type product_id: str
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


async def androidpublisher_monetization_subscriptions_list(request: web.Request, package_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, show_archived=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_list

    Lists all subscriptions under a given app.

    :param package_name: Required. The parent app (package name) for which the subscriptions should be read.
    :type package_name: str
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
    :param page_size: The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListSubscriptions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptions&#x60; must match the call that provided the page token.
    :type page_token: str
    :param show_archived: Deprecated: subscription archiving is not supported.
    :type show_archived: bool

    """
    return web.Response(status=200)


async def androidpublisher_monetization_subscriptions_patch(request: web.Request, package_name, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_missing=None, latency_tolerance=None, regions_version_version=None, update_mask=None, body=None) -> web.Response:
    """androidpublisher_monetization_subscriptions_patch

    Updates an existing subscription.

    :param package_name: Immutable. Package name of the parent app.
    :type package_name: str
    :param product_id: Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length.
    :type product_id: str
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
    :param allow_missing: Optional. If set to true, and the subscription with the given package_name and product_id doesn&#39;t exist, the subscription will be created. If a new subscription is created, update_mask is ignored.
    :type allow_missing: bool
    :param latency_tolerance: Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
    :type latency_tolerance: str
    :param regions_version_version: Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    :type regions_version_version: str
    :param update_mask: Required. The list of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Subscription.from_dict(body)
    return web.Response(status=200)
