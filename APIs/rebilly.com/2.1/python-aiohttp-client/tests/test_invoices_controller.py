# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_issue import InvoiceIssue
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.invoice_reissue import InvoiceReissue
from openapi_server.models.invoice_timeline import InvoiceTimeline
from openapi_server.models.invoice_transaction import InvoiceTransaction
from openapi_server.models.invoice_transaction_allocation import InvoiceTransactionAllocation


pytestmark = pytest.mark.asyncio

async def test_delete_invoice_timeline(client):
    """Test case for delete_invoice_timeline

    Delete an Invoice Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/invoices/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_upcoming_invoice_collection(client):
    """Test case for get_customer_upcoming_invoice_collection

    Retrieve customer's upcoming invoices
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers/{id}/upcoming-invoices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice(client):
    """Test case for get_invoice

    Retrieve an invoice
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'accept': application/json,
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/invoices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_collection(client):
    """Test case for get_invoice_collection

    Retrieve a list of invoices
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
        path='/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_item_collection(client):
    """Test case for get_invoice_item_collection

    Retrieve invoice items
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/invoices/{id}/items'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_timeline(client):
    """Test case for get_invoice_timeline

    Retrieve an Invoice Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/invoices/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_timeline_collection(client):
    """Test case for get_invoice_timeline_collection

    Retrieve a list of invoice timeline messages
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/invoices/{id}/timeline'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_transaction_allocation_collection(client):
    """Test case for get_invoice_transaction_allocation_collection

    Get transaction amounts allocated to an invoice
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/invoices/{id}/transaction-allocations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice(client):
    """Test case for post_invoice

    Create an invoice
    """
    body = {"notes":"notes","_links":[{"rel":"self"},{"rel":"self"}],"dueReminderTime":"","dueReminderNumber":1,"discountAmount":2.3021358869347655,"type":"initial","autopayScheduledTime":"2000-01-23T04:56:07.000+00:00","websiteId":"","delinquentCollectionPeriod":5,"discounts":["",""],"shipping":{"calculator":"manual"},"deliveryAddress":"","_embedded":[{"customer":{"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}},{"customer":{"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}}],"invoiceNumber":7,"customerId":"","createdTime":"","currency":"","id":"","updatedTime":"","amount":0.8008281904610115,"collectionPeriod":5,"paymentFormUrl":"http://example.com/aeiou","autopayRetryNumber":0,"issuedTime":"","tax":{"calculator":"manual","amount":1},"abandonedTime":"","dueTime":"","paidTime":"","transactions":[{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}},{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}],"subtotalAmount":1.2315135367772556,"revision":6,"amountDue":6.027456183070403,"retryInstruction":{"afterAttemptPolicies":["change-subscription-renewal-time","change-subscription-renewal-time"],"afterRetryEndPolicies":["abandon-invoice","abandon-invoice"],"attempts":[{"scheduleInstruction":{"method":"intelligent"}},{"scheduleInstruction":{"method":"intelligent"}}]},"voidedTime":"","billingAddress":"","subscriptionId":"","items":[{"unitPrice":7.386281948385884,"updatedTime":"","periodNumber":3,"quantity":4,"productId":"","_links":[{"rel":"self"},{"rel":"self"}],"description":"description","discountAmount":9.301444243932576,"periodEndTime":"2000-01-23T04:56:07.000+00:00","type":"debit","_embedded":[{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}},{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}}],"price":2.027123023002322,"periodStartTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":""},{"unitPrice":7.386281948385884,"updatedTime":"","periodNumber":3,"quantity":4,"productId":"","_links":[{"rel":"self"},{"rel":"self"}],"description":"description","discountAmount":9.301444243932576,"periodEndTime":"2000-01-23T04:56:07.000+00:00","type":"debit","_embedded":[{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}},{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}}],"price":2.027123023002322,"periodStartTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":""}],"poNumber":"PO123456","status":"draft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_abandonment(client):
    """Test case for post_invoice_abandonment

    Abandon an invoice
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/abandon'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_issuance(client):
    """Test case for post_invoice_issuance

    Issue an invoice
    """
    body = {"issuedTime":"2000-01-23T04:56:07.000+00:00","dueTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/issue'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_item(client):
    """Test case for post_invoice_item

    Create an invoice item
    """
    body = {"unitPrice":7.386281948385884,"updatedTime":"","periodNumber":3,"quantity":4,"productId":"","_links":[{"rel":"self"},{"rel":"self"}],"description":"description","discountAmount":9.301444243932576,"periodEndTime":"2000-01-23T04:56:07.000+00:00","type":"debit","_embedded":[{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}},{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}}],"price":2.027123023002322,"periodStartTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/items'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_recalculation(client):
    """Test case for post_invoice_recalculation

    Recalculate an invoice
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/recalculate'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_reissuance(client):
    """Test case for post_invoice_reissuance

    Reissue an invoice
    """
    body = {"dueTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/reissue'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_timeline(client):
    """Test case for post_invoice_timeline

    Create an invoice Timeline comment
    """
    body = {"_links":[{"rel":"self"},{"rel":"self"}],"extraData":{"tables":[{"footer":"footer","title":"title","type":"list"},{"footer":"footer","title":"title","type":"list"}],"author":{"userFullName":"userFullName","userId":"userId"},"mentions":{"key":"{\"@test@mail.com\":\"userId-1\"}"},"links":[{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"},{"resourceId":"4f6cf35x-2c4y-483z-a0a9-158621f77a21","placeholder":"KYC Document","resourceType":"kyc-document"}],"actions":[{"action":"resend-email"},{"action":"resend-email"}]},"occurredTime":"","id":"","message":"message","type":"timeline-comment-created","triggeredBy":"rebilly"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/timeline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_transaction(client):
    """Test case for post_invoice_transaction

    Apply a transaction to an invoice
    """
    body = {"amount":0.8008281904610115,"transactionId":"transactionId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/transaction'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_invoice_void(client):
    """Test case for post_invoice_void

    Void an invoice
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invoices/{id}/void'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_invoice(client):
    """Test case for put_invoice

    Create or update an invoice with predefined ID
    """
    body = {"notes":"notes","_links":[{"rel":"self"},{"rel":"self"}],"dueReminderTime":"","dueReminderNumber":1,"discountAmount":2.3021358869347655,"type":"initial","autopayScheduledTime":"2000-01-23T04:56:07.000+00:00","websiteId":"","delinquentCollectionPeriod":5,"discounts":["",""],"shipping":{"calculator":"manual"},"deliveryAddress":"","_embedded":[{"customer":{"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}},{"customer":{"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}}],"invoiceNumber":7,"customerId":"","createdTime":"","currency":"","id":"","updatedTime":"","amount":0.8008281904610115,"collectionPeriod":5,"paymentFormUrl":"http://example.com/aeiou","autopayRetryNumber":0,"issuedTime":"","tax":{"calculator":"manual","amount":1},"abandonedTime":"","dueTime":"","paidTime":"","transactions":[{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}},{"billingDescriptor":"billingDescriptor","3ds":"","redirectUrl":"https://openapi-generator.tech","_links":[{"rel":"self"},{"rel":"self"}],"orderId":"orderId","bin":"bin","type":"3ds-authentication","bumpOffer":{"selectedOffer":"","language":"","version":"","outcome":"presented","order":"","presentedOffers":""},"websiteId":"","disputeStatus":"response-needed","isProcessedOutside":True,"riskMetadata":"","createdTime":"","id":"","riskScore":8,"acquirerName":"","updatedTime":"","scheduledTime":"2000-01-23T04:56:07.000+00:00","method":"","disputeTime":"2000-01-23T04:56:07.000+00:00","has3ds":True,"parentTransactionId":"","processedTime":"","revision":6,"subscriptionIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"retryNumber":9,"invoiceIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"status":"completed","isRetry":True,"planIds":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"isReconciled":True,"rebillNumber":4,"hasBumpOffer":True,"isMerchantInitiated":True,"dcc":{"usdMarkup":"","quote":"","outcome":"rejected","base":""},"discrepancyTime":"2000-01-23T04:56:07.000+00:00","retriedTransactionId":"","customFields":{"foo":"bar"},"gatewayAccountId":"","description":"description","purchaseCurrency":"","requestAmount":5.025004791520295,"hadDiscrepancy":True,"hasDcc":True,"retriesResult":"approved","result":"abandoned","isDisputed":True,"reportCurrency":"","gatewayTransactionId":"","_embedded":[{},{}],"requestId":"requestId","customerId":"","currency":"","arn":"74836950144358910018150","requestCurrency":"","amount":7.457744773683766,"gatewayName":"","childTransactions":["4f6cf35x-2c4y-483z-a0a9-158621f77a21","4f6cf35x-2c4y-483z-a0a9-158621f77a21"],"velocity":9,"paymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"purchaseAmount":1.1730742509559433,"referenceData":{"gatewayTransactionId":"GAT123"},"hasAmountAdjustment":True,"retryInstruction":{"afterRetryEndPolicy":"none","afterAttemptPolicy":"none","attempts":[{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}},{"scheduleInstruction":{"method":"auto"},"paymentInstruction":{"method":"none"}}]},"settlementTime":"2000-01-23T04:56:07.000+00:00","isRebill":True,"reportAmount":9.369310271410669,"billingAddress":"","gateway":{"cvvResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"},"response":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage","type":"type"},"avsResponse":{"code":"code","originalCode":"originalCode","message":"message","originalMessage":"originalMessage"}}}],"subtotalAmount":1.2315135367772556,"revision":6,"amountDue":6.027456183070403,"retryInstruction":{"afterAttemptPolicies":["change-subscription-renewal-time","change-subscription-renewal-time"],"afterRetryEndPolicies":["abandon-invoice","abandon-invoice"],"attempts":[{"scheduleInstruction":{"method":"intelligent"}},{"scheduleInstruction":{"method":"intelligent"}}]},"voidedTime":"","billingAddress":"","subscriptionId":"","items":[{"unitPrice":7.386281948385884,"updatedTime":"","periodNumber":3,"quantity":4,"productId":"","_links":[{"rel":"self"},{"rel":"self"}],"description":"description","discountAmount":9.301444243932576,"periodEndTime":"2000-01-23T04:56:07.000+00:00","type":"debit","_embedded":[{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}},{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}}],"price":2.027123023002322,"periodStartTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":""},{"unitPrice":7.386281948385884,"updatedTime":"","periodNumber":3,"quantity":4,"productId":"","_links":[{"rel":"self"},{"rel":"self"}],"description":"description","discountAmount":9.301444243932576,"periodEndTime":"2000-01-23T04:56:07.000+00:00","type":"debit","_embedded":[{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}},{"product":{"updatedTime":"","requiresShipping":False,"accountingCode":"4010","unitLabel":"seat","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"name":"Premium membership","options":["options","options"],"createdTime":"","description":"description","id":"membership","taxCategoryId":"00000"}}],"price":2.027123023002322,"periodStartTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":""}],"poNumber":"PO123456","status":"draft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/invoices/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

