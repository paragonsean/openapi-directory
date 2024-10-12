# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.item_list import ItemList
from openapi_server.models.itv_billing_history import ItvBillingHistory
from openapi_server.models.itv_billing_history_request import ItvBillingHistoryRequest
from openapi_server.models.itv_cancel_subscription_request import ItvCancelSubscriptionRequest
from openapi_server.models.itv_card_details import ItvCardDetails
from openapi_server.models.itv_change_card_details_request import ItvChangeCardDetailsRequest
from openapi_server.models.itv_change_email_request import ItvChangeEmailRequest
from openapi_server.models.itv_change_marketing_request import ItvChangeMarketingRequest
from openapi_server.models.itv_current_subscription import ItvCurrentSubscription
from openapi_server.models.itv_delete_account_request import ItvDeleteAccountRequest
from openapi_server.models.itv_entitlement_current import ItvEntitlementCurrent
from openapi_server.models.itv_entitlements_history import ItvEntitlementsHistory
from openapi_server.models.itv_feature_flag import ItvFeatureFlag
from openapi_server.models.itv_get_card_details_request import ItvGetCardDetailsRequest
from openapi_server.models.itv_get_discount_response import ItvGetDiscountResponse
from openapi_server.models.itv_google_pay_subscription_request import ItvGooglePaySubscriptionRequest
from openapi_server.models.itv_had_entitlement import ItvHadEntitlement
from openapi_server.models.itv_pin_auth_request import ItvPinAuthRequest
from openapi_server.models.itv_plans import ItvPlans
from openapi_server.models.itv_profile_token import ItvProfileToken
from openapi_server.models.itv_profile_token_request import ItvProfileTokenRequest
from openapi_server.models.itv_purchase import ItvPurchase
from openapi_server.models.itv_purchase_request import ItvPurchaseRequest
from openapi_server.models.itv_purchase_strong_request import ItvPurchaseStrongRequest
from openapi_server.models.itv_purchase_strong_response import ItvPurchaseStrongResponse
from openapi_server.models.itv_purchase_with_offer_request import ItvPurchaseWithOfferRequest
from openapi_server.models.itv_purchase_with_offer_response import ItvPurchaseWithOfferResponse
from openapi_server.models.itv_roku_transaction_request import ItvRokuTransactionRequest
from openapi_server.models.itv_subscription_full_price_renewal import ItvSubscriptionFullPriceRenewal
from openapi_server.models.itv_subscription_state import ItvSubscriptionState
from openapi_server.models.itv_subscription_status_response import ItvSubscriptionStatusResponse
from openapi_server.models.itv_update_intent_strong_request import ItvUpdateIntentStrongRequest
from openapi_server.models.itv_update_intent_strong_response import ItvUpdateIntentStrongResponse
from openapi_server.models.itv_update_payment_strong_request import ItvUpdatePaymentStrongRequest
from openapi_server.models.itv_update_profile_request import ItvUpdateProfileRequest
from openapi_server.models.itv_upgrade_plan_request import ItvUpgradePlanRequest
from openapi_server.models.itv_voucher import ItvVoucher
from openapi_server.models.itv_voucher_request import ItvVoucherRequest
from openapi_server.models.roku_plans import RokuPlans
from openapi_server.models.samsung_preview import SamsungPreview
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_activate_save_offer(client):
    """Test case for activate_save_offer

    
    """
    body = 'body_example'
    params = [('lang', 'lang_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/save-offer',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_card_details(client):
    """Test case for change_card_details

    
    """
    body = {"profileToken":"profileToken","cardToken":"cardToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/itv/cards/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_email(client):
    """Test case for change_email

    
    """
    body = {"profileToken":"profileToken","email":"email"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/changeemail',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_marketing(client):
    """Test case for change_marketing

    
    """
    body = {"profileToken":"profileToken","emailOptIn":True}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/changemarketing',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_previous_entitlements(client):
    """Test case for check_previous_entitlements

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/had/entitlements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_voucher(client):
    """Test case for check_voucher

    
    """
    body = {"voucher":"voucher"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/voucher/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_purchase(client):
    """Test case for confirm_purchase

    
    """
    body = {"profileToken":"profileToken","voucher":"voucher","planId":"planId","cardToken":"cardToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/purchase/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_purchase_strong(client):
    """Test case for confirm_purchase_strong

    
    """
    body = {"paymentMethodFromToken":"paymentMethodFromToken","profileToken":"profileToken","paymentMethodId":"paymentMethodId","voucher":"voucher","planId":"planId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/purchase/{platform}/strong'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_purchase_with_offer(client):
    """Test case for confirm_purchase_with_offer

    
    """
    body = {"paymentMethodFromToken":"paymentMethodFromToken","profileToken":"profileToken","paymentMethodId":"paymentMethodId","planId":"planId","couponId":"couponId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/purchase/{platform}/withoffer'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    
    """
    body = {"profileToken":"profileToken"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/deleteaccount',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_transaction(client):
    """Test case for execute_transaction

    
    """
    body = {"profileToken":"profileToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/roku/transaction/{transactionid}'.format(transactionid='transactionid_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_token_with_pin(client):
    """Test case for get_account_token_with_pin

    
    """
    body = {"pin":"pin","cookieType":"Session","scopes":["Catalog","Catalog"]}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/pinauthorization',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_billing_history(client):
    """Test case for get_billing_history

    
    """
    body = {"profileToken":"profileToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/billinghistory/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_card_details(client):
    """Test case for get_card_details

    
    """
    body = {"profileToken":"profileToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/cards/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_entitlement(client):
    """Test case for get_current_entitlement

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/entitlements/current',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_subscription(client):
    """Test case for get_current_subscription

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/purchase/{platform}'.format(platform='platform_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entitlements_history(client):
    """Test case for get_entitlements_history

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/entitlements/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feature_flag(client):
    """Test case for get_feature_flag

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/featureFlag/{feature}'.format(feature='feature_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_full_price_renewal(client):
    """Test case for get_full_price_renewal

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/subscription/fullpricerenewal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_itv_profile_token(client):
    """Test case for get_itv_profile_token

    
    """
    body = {"password":"password"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/profiletoken',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_preview(client):
    """Test case for get_public_preview

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/samsung-preview',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recommended_list(client):
    """Test case for get_recommended_list

    
    """
    params = [('item_types', ['{\"item_types\":\"show,movie\"}']),
                    ('page', 1),
                    ('page_size', 12),
                    ('device', 'web_browser'),
                    ('sub', 'sub_example'),
                    ('segments', ['segments_example']),
                    ('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/profile/recommendation/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_save_offer(client):
    """Test case for get_save_offer

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/save-offer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_state(client):
    """Test case for get_subscription_state

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/subscriptionstate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_status(client):
    """Test case for get_subscription_status

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/subscription/status/{platform}'.format(platform='platform_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upcoming_invoice(client):
    """Test case for get_upcoming_invoice

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/upcominginvoice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_voucher_by_id(client):
    """Test case for get_voucher_by_id

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/voucher/{plan_id}/{voucher_id}'.format(voucher_id='voucher_id_example', plan_id='plan_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_google_pay_subscription(client):
    """Test case for google_pay_subscription

    
    """
    body = {"purchaseToken":"purchaseToken","subscriptionItem":"subscriptionItem"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/googlepay/subscription',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_itv_itemsummary_external_id_get(client):
    """Test case for itv_itemsummary_external_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/itemsummary/{external_id}'.format(external_id='external_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_itv_plans_platform_get(client):
    """Test case for itv_plans_platform_get

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/plans/{platform}'.format(platform='platform_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_itv_profile_get(client):
    """Test case for itv_profile_get

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_itv_purchase_platform_delete(client):
    """Test case for itv_purchase_platform_delete

    
    """
    body = {"profileToken":"profileToken"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/itv/purchase/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_itv_roku_plans_get(client):
    """Test case for itv_roku_plans_get

    
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/itv/roku/plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resubscribe(client):
    """Test case for resubscribe

    
    """
    params = [('planId', 'plan_id_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/resubscribe/{platform}'.format(platform='platform_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_intent_strong(client):
    """Test case for update_payment_intent_strong

    
    """
    body = {"paymentMethodFromToken":"paymentMethodFromToken","profileToken":"profileToken","paymentMethodId":"paymentMethodId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/itv/updateIntent/strong/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_method_strong(client):
    """Test case for update_payment_method_strong

    
    """
    body = {"paymentMethodFromToken":"paymentMethodFromToken","profileToken":"profileToken","paymentMethodId":"paymentMethodId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/itv/updatePayment/strong/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_profile(client):
    """Test case for update_profile

    
    """
    body = {"firstName":"firstName","lastName":"lastName","profileToken":"profileToken","postcode":"postcode","dateOfBirth":"dateOfBirth","title":"title","email":"email"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/itv/profile',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upgrade_plan(client):
    """Test case for upgrade_plan

    
    """
    body = {"planId":"planId"}
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/itv/plan/{platform}'.format(platform='platform_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

