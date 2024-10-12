# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.pay_pal_account import PayPalAccount


pytestmark = pytest.mark.asyncio

async def test_get_pay_pal_account(client):
    """Test case for get_pay_pal_account

    Retrieve a PayPal Account
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/paypal-accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_pal_account_collection(client):
    """Test case for get_pay_pal_account_collection

    Retrieve a list of PayPal accounts
    """
    params = [('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('limit', 56),
                    ('offset', 56),
                    ('q', 'q_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/paypal-accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pay_pal_account(client):
    """Test case for post_pay_pal_account

    Create a PayPal Account
    """
    body = {"updatedTime":"","method":"paypal","_embedded":[{"authTransaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}},{"authTransaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}}],"_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"riskMetadata":{"country":"US","accuracyRadius":0,"distance":1,"city":"New York","isp":"isp","latitude":5.962133916683182,"postalCode":"postalCode","hasMismatchedHolderName":True,"httpHeaders":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Content-Type":"application/json"},"score":7,"vpnServiceName":"vpnServiceName","hasMismatchedBillingAddressCountry":True,"isVpn":True,"fingerprint":"pIUt3xbgX3l9g3YDiLbx","isHosting":True,"longitude":5.637376656633329,"hasMismatchedTimeZone":True,"deviceVelocity":6,"ipAddress":"93.92.91.90","timeZone":"America/New_York","paymentInstrumentVelocity":2,"isProxy":True,"isTor":True,"browserData":{"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":300,"isJavaEnabled":True,"language":"en-US","colorDepth":24},"hasMismatchedBankCountry":True,"region":"NY"},"customerId":"","createdTime":"","billingAddress":"","id":"","status":"inactive","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/paypal-accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pay_pal_account_deactivation(client):
    """Test case for post_pay_pal_account_deactivation

    Deactivate a PayPal Account
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/paypal-accounts/{id}/deactivation'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_pay_pal_account(client):
    """Test case for put_pay_pal_account

    Create a PayPal account with predefined ID
    """
    body = {"updatedTime":"","method":"paypal","_embedded":[{"authTransaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}},{"authTransaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}}],"_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"riskMetadata":{"country":"US","accuracyRadius":0,"distance":1,"city":"New York","isp":"isp","latitude":5.962133916683182,"postalCode":"postalCode","hasMismatchedHolderName":True,"httpHeaders":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Content-Type":"application/json"},"score":7,"vpnServiceName":"vpnServiceName","hasMismatchedBillingAddressCountry":True,"isVpn":True,"fingerprint":"pIUt3xbgX3l9g3YDiLbx","isHosting":True,"longitude":5.637376656633329,"hasMismatchedTimeZone":True,"deviceVelocity":6,"ipAddress":"93.92.91.90","timeZone":"America/New_York","paymentInstrumentVelocity":2,"isProxy":True,"isTor":True,"browserData":{"screenWidth":1920,"screenHeight":1080,"timeZoneOffset":300,"isJavaEnabled":True,"language":"en-US","colorDepth":24},"hasMismatchedBankCountry":True,"region":"NY"},"customerId":"","createdTime":"","billingAddress":"","id":"","status":"inactive","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/paypal-accounts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

