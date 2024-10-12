# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dispute import Dispute
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_get_dispute(client):
    """Test case for get_dispute

    Retrieve a dispute
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/disputes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dispute_collection(client):
    """Test case for get_dispute_collection

    Retrieve a list of disputes
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
        path='/disputes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_dispute(client):
    """Test case for post_dispute

    Create a dispute
    """
    body = {"updatedTime":"","amount":0.8008281904610115,"deadlineTime":"2000-01-23T04:56:07.000+00:00","_links":[{"rel":"self"},{"rel":"self"}],"rawResponse":"rawResponse","resolvedTime":"","postedTime":"2000-01-23T04:56:07.000+00:00","type":"information-request","transactionId":"transactionId","_embedded":[{"transaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}},{"transaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}}],"caseId":"caseId","customerId":"customerId","createdTime":"","currency":"","acquirerReferenceNumber":"acquirerReferenceNumber","id":"","reasonCode":"1000","category":"fraud","status":"response-needed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/disputes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_dispute(client):
    """Test case for put_dispute

    Create or update a Dispute with predefined ID
    """
    body = {"updatedTime":"","amount":0.8008281904610115,"deadlineTime":"2000-01-23T04:56:07.000+00:00","_links":[{"rel":"self"},{"rel":"self"}],"rawResponse":"rawResponse","resolvedTime":"","postedTime":"2000-01-23T04:56:07.000+00:00","type":"information-request","transactionId":"transactionId","_embedded":[{"transaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}},{"transaction":{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}}],"caseId":"caseId","customerId":"customerId","createdTime":"","currency":"","acquirerReferenceNumber":"acquirerReferenceNumber","id":"","reasonCode":"1000","category":"fraud","status":"response-needed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/disputes/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

