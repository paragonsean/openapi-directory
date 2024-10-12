# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_client_preferences_request import AddClientPreferencesRequest
from openapi_server.models.add_client_profile_request import AddClientProfileRequest
from openapi_server.models.add_marketing_data_request import AddMarketingDataRequest
from openapi_server.models.add_merchant_context_data200_response import AddMerchantContextData200Response
from openapi_server.models.add_merchant_context_data_request import AddMerchantContextDataRequest
from openapi_server.models.add_payment_data_request import AddPaymentDataRequest
from openapi_server.models.add_shipping_address_request import AddShippingAddressRequest
from openapi_server.models.get_client_profile_by_email200_response import GetClientProfileByEmail200Response


pytestmark = pytest.mark.asyncio

async def test_add_client_preferences(client):
    """Test case for add_client_preferences

    Add client preferences
    """
    body = openapi_server.AddClientPreferencesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/clientPreferencesData'.format(order_form_id='order_form_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_client_profile(client):
    """Test case for add_client_profile

    Add client profile
    """
    body = openapi_server.AddClientProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/clientProfileData'.format(order_form_id='order_form_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_marketing_data(client):
    """Test case for add_marketing_data

    Add marketing data
    """
    body = openapi_server.AddMarketingDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/marketingData'.format(order_form_id='order_form_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_merchant_context_data(client):
    """Test case for add_merchant_context_data

    Add merchant context data
    """
    body = openapi_server.AddMerchantContextDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/merchantContextData'.format(order_form_id='29154e27383145cc8ce1f7a1df0d99c4'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_payment_data(client):
    """Test case for add_payment_data

    Add payment data
    """
    body = openapi_server.AddPaymentDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/paymentData'.format(order_form_id='order_form_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_shipping_address(client):
    """Test case for add_shipping_address

    Add shipping address and select delivery option
    """
    body = openapi_server.AddShippingAddressRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/attachments/shippingData'.format(order_form_id='order_form_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_profile_by_email(client):
    """Test case for get_client_profile_by_email

    Get client profile by email
    """
    params = [('email', 'clark.kent@examplemail.com')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

