# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_convert_region_prices(client):
    """Test case for androidpublisher_monetization_convert_region_prices

    
    """
    body = {"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}
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
        path='/androidpublisher/v3/applications/{package_name}/pricing:convertRegionPrices'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_archive(client):
    """Test case for androidpublisher_monetization_subscriptions_archive

    
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_idarchiv}'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_activate(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_activate

    
    """
    body = {"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_idactivat}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_batch_migrate_prices(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_batch_migrate_prices

    
    """
    body = {"requests":[{"regionalPriceMigrations":[{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"},{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"}],"productId":"productId","regionsVersion":{"version":"version"},"packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},{"regionalPriceMigrations":[{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"},{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"}],"productId":"productId","regionsVersion":{"version":"version"},"packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans:batchMigratePrices'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_batch_update_states(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_batch_update_states

    
    """
    body = {"requests":[{"deactivateBasePlanRequest":{"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},"activateBasePlanRequest":{"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}},{"deactivateBasePlanRequest":{"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},"activateBasePlanRequest":{"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans:batchUpdateStates'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_deactivate(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_deactivate

    
    """
    body = {"productId":"productId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_iddeactivat}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_delete(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_migrate_prices(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_migrate_prices

    
    """
    body = {"regionalPriceMigrations":[{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"},{"oldestAllowedPriceVersionTime":"oldestAllowedPriceVersionTime","regionCode":"regionCode","priceIncreaseType":"PRICE_INCREASE_TYPE_UNSPECIFIED"}],"productId":"productId","regionsVersion":{"version":"version"},"packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_idmigrate_price}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_activate(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_activate

    
    """
    body = {"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers/{offer_idactivat}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example', offer_id='offer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_batch_get(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_batch_get

    
    """
    body = {"requests":[{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId"},{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId"}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers:batchGet'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_batch_update(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_batch_update

    
    """
    body = {"requests":[{"subscriptionOffer":{"otherRegionsConfig":{"otherRegionsNewSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"targeting":{"upgradeRule":{"oncePerUser":True,"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"},"billingPeriodDuration":"billingPeriodDuration"},"acquisitionRule":{"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"}}},"productId":"productId","offerId":"offerId","regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True},{"regionCode":"regionCode","newSubscriberAvailability":True}],"packageName":"packageName","state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","phases":[{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]},{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]}]},"allowMissing":True,"regionsVersion":{"version":"version"},"updateMask":"updateMask","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},{"subscriptionOffer":{"otherRegionsConfig":{"otherRegionsNewSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"targeting":{"upgradeRule":{"oncePerUser":True,"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"},"billingPeriodDuration":"billingPeriodDuration"},"acquisitionRule":{"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"}}},"productId":"productId","offerId":"offerId","regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True},{"regionCode":"regionCode","newSubscriberAvailability":True}],"packageName":"packageName","state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","phases":[{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]},{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]}]},"allowMissing":True,"regionsVersion":{"version":"version"},"updateMask":"updateMask","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers:batchUpdate'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_batch_update_states(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_batch_update_states

    
    """
    body = {"requests":[{"activateSubscriptionOfferRequest":{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},"deactivateSubscriptionOfferRequest":{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}},{"activateSubscriptionOfferRequest":{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},"deactivateSubscriptionOfferRequest":{"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers:batchUpdateStates'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_create(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_create

    
    """
    body = {"otherRegionsConfig":{"otherRegionsNewSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"targeting":{"upgradeRule":{"oncePerUser":True,"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"},"billingPeriodDuration":"billingPeriodDuration"},"acquisitionRule":{"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"}}},"productId":"productId","offerId":"offerId","regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True},{"regionCode":"regionCode","newSubscriberAvailability":True}],"packageName":"packageName","state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","phases":[{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]},{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]}]}
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
                    ('offerId', 'offer_id_example'),
                    ('regionsVersion.version', 'regions_version_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_deactivate(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_deactivate

    
    """
    body = {"productId":"productId","offerId":"offerId","packageName":"packageName","basePlanId":"basePlanId","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers/{offer_iddeactivat}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example', offer_id='offer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_delete(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers/{offer_id}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example', offer_id='offer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_get(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_get

    
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers/{offer_id}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example', offer_id='offer_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_list(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_list

    
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_base_plans_offers_patch(client):
    """Test case for androidpublisher_monetization_subscriptions_base_plans_offers_patch

    
    """
    body = {"otherRegionsConfig":{"otherRegionsNewSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"targeting":{"upgradeRule":{"oncePerUser":True,"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"},"billingPeriodDuration":"billingPeriodDuration"},"acquisitionRule":{"scope":{"specificSubscriptionInApp":"specificSubscriptionInApp"}}},"productId":"productId","offerId":"offerId","regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True},{"regionCode":"regionCode","newSubscriberAvailability":True}],"packageName":"packageName","state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","phases":[{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]},{"duration":"duration","otherRegionsConfig":{"absoluteDiscounts":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"relativeDiscount":0.8008281904610115,"otherRegionsPrices":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"recurrenceCount":6,"regionalConfigs":[{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","price":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"relativeDiscount":1.4658129805029452,"absoluteDiscount":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}]}]}
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
                    ('allowMissing', True),
                    ('latencyTolerance', 'latency_tolerance_example'),
                    ('regionsVersion.version', 'regions_version_version_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}/basePlans/{base_plan_id}/offers/{offer_id}'.format(package_name='package_name_example', product_id='product_id_example', base_plan_id='base_plan_id_example', offer_id='offer_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_batch_get(client):
    """Test case for androidpublisher_monetization_subscriptions_batch_get

    
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
                    ('productIds', ['product_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions:batchGet'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_batch_update(client):
    """Test case for androidpublisher_monetization_subscriptions_batch_update

    
    """
    body = {"requests":[{"allowMissing":True,"regionsVersion":{"version":"version"},"subscription":{"archived":True,"listings":[{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"},{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"}],"productId":"productId","packageName":"packageName","basePlans":[{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}},{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}}],"taxAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"}},"updateMask":"updateMask","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"},{"allowMissing":True,"regionsVersion":{"version":"version"},"subscription":{"archived":True,"listings":[{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"},{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"}],"productId":"productId","packageName":"packageName","basePlans":[{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}},{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}}],"taxAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"}},"updateMask":"updateMask","latencyTolerance":"PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"}]}
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions:batchUpdate'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_create(client):
    """Test case for androidpublisher_monetization_subscriptions_create

    
    """
    body = {"archived":True,"listings":[{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"},{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"}],"productId":"productId","packageName":"packageName","basePlans":[{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}},{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}}],"taxAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"}}
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
                    ('productId', 'product_id_example'),
                    ('regionsVersion.version', 'regions_version_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions'.format(package_name='package_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_delete(client):
    """Test case for androidpublisher_monetization_subscriptions_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_get(client):
    """Test case for androidpublisher_monetization_subscriptions_get

    
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
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_list(client):
    """Test case for androidpublisher_monetization_subscriptions_list

    
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
                    ('showArchived', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_monetization_subscriptions_patch(client):
    """Test case for androidpublisher_monetization_subscriptions_patch

    
    """
    body = {"archived":True,"listings":[{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"},{"benefits":["benefits","benefits"],"description":"description","languageCode":"languageCode","title":"title"}],"productId":"productId","packageName":"packageName","basePlans":[{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}},{"otherRegionsConfig":{"eurPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"usdPrice":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"newSubscriberAvailability":True},"offerTags":[{"tag":"tag"},{"tag":"tag"}],"autoRenewingBasePlanType":{"accountHoldDuration":"accountHoldDuration","billingPeriodDuration":"billingPeriodDuration","gracePeriodDuration":"gracePeriodDuration","legacyCompatibleSubscriptionOfferId":"legacyCompatibleSubscriptionOfferId","resubscribeState":"RESUBSCRIBE_STATE_UNSPECIFIED","legacyCompatible":True,"prorationMode":"SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED"},"regionalConfigs":[{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},{"regionCode":"regionCode","newSubscriberAvailability":True,"price":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}],"state":"STATE_UNSPECIFIED","basePlanId":"basePlanId","prepaidBasePlanType":{"timeExtension":"TIME_EXTENSION_UNSPECIFIED","billingPeriodDuration":"billingPeriodDuration"}}],"taxAndComplianceSettings":{"taxRateInfoByRegionCode":{"key":{"eligibleForStreamingServiceTaxRate":True,"taxTier":"TAX_TIER_UNSPECIFIED","streamingTaxType":"STREAMING_TAX_TYPE_UNSPECIFIED"}},"isTokenizedDigitalAsset":True,"eeaWithdrawalRightType":"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"}}
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
                    ('allowMissing', True),
                    ('latencyTolerance', 'latency_tolerance_example'),
                    ('regionsVersion.version', 'regions_version_version_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/androidpublisher/v3/applications/{package_name}/subscriptions/{product_id}'.format(package_name='package_name_example', product_id='product_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

