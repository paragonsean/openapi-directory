# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_carbon_offset(client):
    """Test case for confirm_carbon_offset

    confirmCarbonOffset
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'carbon_offset': 'carbon_offset_example',
        'contact_email': 'contact_email_example',
        'contact_first_name': 'contact_first_name_example',
        'contact_last_name': 'contact_last_name_example',
        'transaction_id': 'transaction_id_example'
        }
    response = await client.request(
        method='PATCH',
        path='/footprint/urbanDelivery/confirmCarbonOffset',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment(client):
    """Test case for confirm_payment

    confirmPayment
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'confirm_payment': 'confirm_payment_example',
        'payment_id': 56,
        'transaction_id': 'transaction_id_example'
        }
    response = await client.request(
        method='PATCH',
        path='/footprint/urbanDelivery/confirmPayment',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment_of_transaction(client):
    """Test case for confirm_payment_of_transaction

    confirmTransaction
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'confirm_transaction': 'confirm_transaction_example',
        'transaction_id': 'transaction_id_example'
        }
    response = await client.request(
        method='PATCH',
        path='/footprint/urbanDelivery/confirmTransaction',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirms_planting(client):
    """Test case for confirms_planting

    confirmPlanting
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'confirm_planting': 'confirm_planting_example',
        'transaction_id': 'transaction_id_example'
        }
    response = await client.request(
        method='PATCH',
        path='/footprint/urbanDelivery/confirmPlanting',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_urban_delivery(client):
    """Test case for urban_delivery

    urbanDelivery
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'destination_latitude': 3.4,
        'destination_longitude': 3.4,
        'item_count': 56,
        'origin_latitude': 3.4,
        'origin_longitude': 3.4,
        'vehicle_type': 'vehicle_type_example'
        }
    response = await client.request(
        method='POST',
        path='/footprint/urbanDelivery',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

