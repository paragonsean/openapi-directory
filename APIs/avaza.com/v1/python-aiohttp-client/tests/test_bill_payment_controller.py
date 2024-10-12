# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_payment import BillPayment
from openapi_server.models.bill_payment_list import BillPaymentList
from openapi_server.models.new_bill_payment import NewBillPayment


pytestmark = pytest.mark.asyncio

async def test_bill_payment_get(client):
    """Test case for bill_payment_get

    Gets list of Bill Payments
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/BillPayment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_payment_get_by_id(client):
    """Test case for bill_payment_get_by_id

    Gets a Bill Payment by Payment Transaction ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/BillPayment/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bill_payment_post(client):
    """Test case for bill_payment_post

    Create new Bill Payment and optionally assign payment allocations to Bills
    """
    model = {"CurrencyCode":"CurrencyCode","TransactionPrefix":"TransactionPrefix","ExchangeRate":1.4658129805029452,"PaymentAllocations":[{"AllocationAmount":5.962133916683182,"AllocationDate":"2000-01-23T04:56:07.000+00:00","BillTransactionIDFK":5},{"AllocationAmount":5.962133916683182,"AllocationDate":"2000-01-23T04:56:07.000+00:00","BillTransactionIDFK":5}],"DateIssued":"2000-01-23T04:56:07.000+00:00","TransactionReference":"TransactionReference","PaymentProviderCode":"PaymentProviderCode","Amount":0.8008281904610115,"CompanyIDFK":6,"Notes":"Notes","PaymentNumber":"PaymentNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/BillPayment',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

