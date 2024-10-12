# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_issue import InvoiceIssue
from openapi_server.models.order_timeline import OrderTimeline
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_cancellation import SubscriptionCancellation
from openapi_server.models.subscription_change import SubscriptionChange
from openapi_server.models.subscription_invoice import SubscriptionInvoice
from openapi_server.models.subscription_reactivation import SubscriptionReactivation


pytestmark = pytest.mark.asyncio

async def test_delete_subscription_cancellation(client):
    """Test case for delete_subscription_cancellation

    Delete a cancellation
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscription-cancellations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscription_timeline(client):
    """Test case for delete_subscription_timeline

    Delete an Order Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    Retrieve an order
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
        path='/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_cancellation(client):
    """Test case for get_subscription_cancellation

    Retrieve an order сancellation
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscription-cancellations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_cancellation_collection(client):
    """Test case for get_subscription_cancellation_collection

    Retrieve a list of cancellations
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscription-cancellations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_collection(client):
    """Test case for get_subscription_collection

    Retrieve a list of orders
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
        path='/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_reactivation(client):
    """Test case for get_subscription_reactivation

    Retrieve an order reactivation
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscription-reactivations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_reactivation_collection(client):
    """Test case for get_subscription_reactivation_collection

    Retrieve a list of reactivations
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscription-reactivations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_timeline(client):
    """Test case for get_subscription_timeline

    Retrieve an Order Timeline message
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{id}/timeline/{message_id}'.format(id='id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_timeline_collection(client):
    """Test case for get_subscription_timeline_collection

    Retrieve a list of order timeline messages
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
        path='/subscriptions/{id}/timeline'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_upcoming_invoice_collection(client):
    """Test case for get_subscription_upcoming_invoice_collection

    Retrieve subscription order's upcoming invoice
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
        path='/subscriptions/{id}/upcoming-invoices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription(client):
    """Test case for post_subscription

    Create an order
    """
    body = {"orderType":"subscription-order"}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription_cancellation(client):
    """Test case for post_subscription_cancellation

    Cancel an order
    """
    body = {"reason":"other","_links":[{"rel":"self"},{"rel":"self"}],"canceledBy":"customer","description":"description","lineItems":"","churnTime":"2000-01-23T04:56:07.000+00:00","proratedInvoiceId":"","lineItemSubtotal":49.95,"appliedInvoiceId":"","createdTime":"","id":"","canceledTime":"2000-01-23T04:56:07.000+00:00","subscriptionId":"","prorated":False,"status":"confirmed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscription-cancellations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription_interim_invoice(client):
    """Test case for post_subscription_interim_invoice

    Issue an interim invoice for a subscription order
    """
    body = {"transactionId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{id}/interim-invoice'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription_items_change(client):
    """Test case for post_subscription_items_change

    Change an order's items
    """
    body = {"preview":False,"effectiveTime":"2000-01-23T04:56:07.000+00:00","renewalPolicy":"reset","keepTrial":False,"items":[{"quantity":0,"plan":{"id":""}},{"quantity":0,"plan":{"id":""}}],"prorated":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{id}/change-items'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription_reactivation(client):
    """Test case for post_subscription_reactivation

    Reactivate an order
    """
    body = {"renewalTime":"2000-01-23T04:56:07.000+00:00","_links":[{"rel":"self"},{"rel":"self"}],"effectiveTime":"2000-01-23T04:56:07.000+00:00","createdTime":"2000-01-23T04:56:07.000+00:00","description":"description","id":"","cancellationId":"","subscriptionId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscription-reactivations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_subscription_timeline(client):
    """Test case for post_subscription_timeline

    Create an order Timeline comment
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
        path='/subscriptions/{id}/timeline'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_upcoming_invoice_issuance(client):
    """Test case for post_upcoming_invoice_issuance

    Issue an upcoming invoice for early pay
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
        path='/subscriptions/{id}/upcoming-invoices/{invoice_id}/issue'.format(id='id_example', invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_subscription(client):
    """Test case for put_subscription

    Upsert an order with predefined ID
    """
    body = {"orderType":"subscription-order"}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_subscription_cancellation(client):
    """Test case for put_subscription_cancellation

    Cancel an order
    """
    body = {"reason":"other","_links":[{"rel":"self"},{"rel":"self"}],"canceledBy":"customer","description":"description","lineItems":"","churnTime":"2000-01-23T04:56:07.000+00:00","proratedInvoiceId":"","lineItemSubtotal":49.95,"appliedInvoiceId":"","createdTime":"","id":"","canceledTime":"2000-01-23T04:56:07.000+00:00","subscriptionId":"","prorated":False,"status":"confirmed"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscription-cancellations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

