# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_coupons200_response import AddCoupons200Response
from openapi_server.models.add_coupons_request import AddCouponsRequest
from openapi_server.models.cart_simulation200_response import CartSimulation200Response
from openapi_server.models.cart_simulation_request import CartSimulationRequest
from openapi_server.models.ignore_profile_data_request import IgnoreProfileDataRequest
from openapi_server.models.items200_response import Items200Response
from openapi_server.models.items_request import ItemsRequest
from openapi_server.models.items_update200_response import ItemsUpdate200Response
from openapi_server.models.items_update_request import ItemsUpdateRequest
from openapi_server.models.price_change_request import PriceChangeRequest


pytestmark = pytest.mark.asyncio

async def test_add_coupons(client):
    """Test case for add_coupons

    Add coupons to the cart
    """
    body = openapi_server.AddCouponsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/coupons'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cart_simulation(client):
    """Test case for cart_simulation

    Cart simulation
    """
    body = openapi_server.CartSimulationRequest()
    params = [('RnbBehavior', 0),
                    ('sc', 1)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForms/simulation',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_a_new_cart(client):
    """Test case for create_a_new_cart

    Get current or create a new cart
    """
    params = [('forceNewCart', True)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/orderForm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cart_information_by_id(client):
    """Test case for get_cart_information_by_id

    Get cart information by ID
    """
    params = [('refreshOutdatedData', True)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/orderForm/{order_form_id}'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cart_installments(client):
    """Test case for get_cart_installments

    Cart installments
    """
    params = [('paymentSystem', 56)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/orderForm/{order_form_id}/installments'.format(order_form_id='order_form_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ignore_profile_data(client):
    """Test case for ignore_profile_data

    Ignore profile data
    """
    body = {"price":10000}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/checkout/pub/orderForm/{order_form_id}/profile'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items(client):
    """Test case for items

    Add cart items
    """
    body = openapi_server.ItemsRequest()
    params = [('allowedOutdatedData', ["paymentData"])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/items'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_items_update(client):
    """Test case for items_update

    Update cart items
    """
    body = openapi_server.ItemsUpdateRequest()
    params = [('allowedOutdatedData', ["paymentData"])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/items/update'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_change(client):
    """Test case for price_change

    Change price
    """
    body = {"price":10000}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/checkout/pub/orderForm/{order_form_id}/items/{item_index}/price'.format(order_form_id='ede846222cd44046ba6c638442c3505a', item_index='item_index_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_all_items(client):
    """Test case for remove_all_items

    Remove all items
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/items/removeAll'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_removeallpersonaldata(client):
    """Test case for removeallpersonaldata

    Remove all personal data
    """
    headers = { 
        'Accept': 'text/plain',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/checkout/changeToAnonymousUser/{order_form_id}'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

