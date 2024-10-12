# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_payment import NewPayment
from openapi_server.models.payment import Payment
from openapi_server.models.payment_list import PaymentList


pytestmark = pytest.mark.asyncio

async def test_payment_get(client):
    """Test case for payment_get

    Gets list of Payments
    """
    params = [('InvoiceTransactionID', 56),
                    ('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Payment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_get_by_id(client):
    """Test case for payment_get_by_id

    Gets Payment by Payment Transaction ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Payment/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_payment_post(client):
    """Test case for payment_post

    Create new Payment and optionally assign payment allocations to Invoices
    """
    model = {"TransactionPrefix":"TransactionPrefix","CustomerIDFK":6,"ExchangeRate":1.4658129805029452,"PaymentAllocations":[{"AllocationAmount":5.962133916683182,"AllocationDate":"2000-01-23T04:56:07.000+00:00","InvoiceTransactionIDFK":5},{"AllocationAmount":5.962133916683182,"AllocationDate":"2000-01-23T04:56:07.000+00:00","InvoiceTransactionIDFK":5}],"DateIssued":"2000-01-23T04:56:07.000+00:00","TransactionReference":"TransactionReference","PaymentProviderCode":"PaymentProviderCode","Amount":0.8008281904610115,"Notes":"Notes","PaymentNumber":"PaymentNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Payment',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

