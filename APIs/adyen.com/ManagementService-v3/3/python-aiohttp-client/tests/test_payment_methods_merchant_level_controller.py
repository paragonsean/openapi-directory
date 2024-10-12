# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apple_pay_info import ApplePayInfo
from openapi_server.models.payment_method import PaymentMethod
from openapi_server.models.payment_method_response import PaymentMethodResponse
from openapi_server.models.payment_method_setup_info import PaymentMethodSetupInfo
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_payment_method_info import UpdatePaymentMethodInfo


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_payment_method_settings(client):
    """Test case for get_merchants_merchant_id_payment_method_settings

    Get all payment methods
    """
    params = [('storeId', 'store_id_example'),
                    ('businessLineId', 'business_line_id_example'),
                    ('pageSize', 56),
                    ('pageNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_payment_method_settings_payment_method_id(client):
    """Test case for get_merchants_merchant_id_payment_method_settings_payment_method_id

    Get payment method details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings/{payment_method_id}'.format(merchant_id='merchant_id_example', payment_method_id='payment_method_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains(client):
    """Test case for get_merchants_merchant_id_payment_method_settings_payment_method_id_get_apple_pay_domains

    Get Apple Pay domains
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings/{payment_method_id}/getApplePayDomains'.format(merchant_id='merchant_id_example', payment_method_id='payment_method_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_payment_method_settings_payment_method_id(client):
    """Test case for patch_merchants_merchant_id_payment_method_settings_payment_method_id

    Update a payment method
    """
    body = {"discover":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"customRoutingFlags":["customRoutingFlags","customRoutingFlags"],"diners":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"ideal":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"jcb":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"countries":["countries","countries"],"enabled":True,"storeIds":["storeIds","storeIds"],"girocard":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"interac_card":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"mc":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"visa":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"bcmc":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"},"enableBcmcMobile":True},"cartesBancaires":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"},"siret":"siret"},"eftpos_australia":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"maestro":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"cup":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"currencies":["currencies","currencies"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings/{payment_method_id}'.format(merchant_id='merchant_id_example', payment_method_id='payment_method_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_payment_method_settings(client):
    """Test case for post_merchants_merchant_id_payment_method_settings

    Request a payment method
    """
    body = {"giroPay":{"supportEmail":"supportEmail"},"customRoutingFlags":["customRoutingFlags","customRoutingFlags"],"jcb":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"googlePay":{"merchantId":"merchantId","reuseMerchantId":True},"type":"afterpaytouch","storeIds":["storeIds","storeIds"],"reference":"reference","vipps":{"subscriptionCancelUrl":"subscriptionCancelUrl","logo":"logo"},"mealVoucher_FR":{"conecsId":"conecsId","subTypes":["subTypes","subTypes"],"siret":"siret"},"mc":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"swish":{"swishNumber":"swishNumber"},"twint":{"logo":"logo"},"cartesBancaires":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"},"siret":"siret"},"shopperInteraction":"eCommerce","afterpayTouch":{"supportUrl":"supportUrl"},"paypal":{"subject":"subject","payerId":"payerId","directCapture":True},"clearpay":{"supportUrl":"supportUrl"},"discover":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"diners":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"ideal":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"applePay":{"domains":["domains","domains"]},"countries":["countries","countries"],"sofort":{"logo":"logo","currencyCode":"currencyCode"},"klarna":{"autoCapture":True,"supportEmail":"supportEmail","region":"NA","disputeEmail":"disputeEmail"},"girocard":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"interac_card":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"visa":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"bcmc":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"},"enableBcmcMobile":True},"eftpos_australia":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"maestro":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"businessLineId":"businessLineId","cup":{"transactionDescription":{"doingBusinessAsName":"doingBusinessAsName","type":"dynamic"}},"currencies":["currencies","currencies"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains(client):
    """Test case for post_merchants_merchant_id_payment_method_settings_payment_method_id_add_apple_pay_domains

    Add an Apple Pay domain
    """
    body = {"domains":["domains","domains"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/paymentMethodSettings/{payment_method_id}/addApplePayDomains'.format(merchant_id='merchant_id_example', payment_method_id='payment_method_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

