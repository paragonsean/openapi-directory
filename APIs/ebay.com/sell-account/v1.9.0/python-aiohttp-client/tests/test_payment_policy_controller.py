# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_policy import PaymentPolicy
from openapi_server.models.payment_policy_request import PaymentPolicyRequest
from openapi_server.models.payment_policy_response import PaymentPolicyResponse
from openapi_server.models.set_payment_policy_response import SetPaymentPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_create_payment_policy(client):
    """Test case for create_payment_policy

    
    """
    body = {"marketplaceId":"marketplaceId","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"paymentMethods":[{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"},{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"}],"name":"name","paymentInstructions":"paymentInstructions","deposit":{"amount":{"currency":"currency","value":"value"},"paymentMethods":[{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"},{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"}],"dueIn":{"unit":"unit","value":0}},"description":"description","immediatePay":True,"fullPaymentDueIn":{"unit":"unit","value":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/payment_policy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payment_policy(client):
    """Test case for delete_payment_policy

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/account/v1/payment_policy/{payment_policy_id}'.format(payment_policy_id='payment_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_policies(client):
    """Test case for get_payment_policies

    
    """
    params = [('marketplace_id', 'marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/payment_policy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_policy(client):
    """Test case for get_payment_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/payment_policy/{payment_policy_id}'.format(payment_policy_id='payment_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_policy_by_name(client):
    """Test case for get_payment_policy_by_name

    
    """
    params = [('marketplace_id', 'marketplace_id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/payment_policy/get_by_policy_name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment_policy(client):
    """Test case for update_payment_policy

    
    """
    body = {"marketplaceId":"marketplaceId","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"paymentMethods":[{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"},{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"}],"name":"name","paymentInstructions":"paymentInstructions","deposit":{"amount":{"currency":"currency","value":"value"},"paymentMethods":[{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"},{"recipientAccountReference":{"referenceType":"referenceType","referenceId":"referenceId"},"brands":["brands","brands"],"paymentMethodType":"paymentMethodType"}],"dueIn":{"unit":"unit","value":0}},"description":"description","immediatePay":True,"fullPaymentDueIn":{"unit":"unit","value":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/account/v1/payment_policy/{payment_policy_id}'.format(payment_policy_id='payment_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

