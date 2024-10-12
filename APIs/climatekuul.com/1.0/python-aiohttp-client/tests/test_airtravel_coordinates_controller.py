# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_airtravel_coordinates(client):
    """Test case for airtravel_coordinates

    airtravelCoordinates
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'content_type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'destination_airport_latitude': 3.4,
        'destination_airport_longitude': 3.4,
        'number_of_passengers': 56,
        'origin_airport_latitude': 3.4,
        'origin_airport_longitude': 3.4,
        'travel_class': 'travel_class_example',
        'travel_mode': 'travel_mode_example'
        }
    response = await client.request(
        method='POST',
        path='/footprint/airtravelCoordinates',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_carbon_offset4(client):
    """Test case for confirm_carbon_offset4

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
        path='/footprint/airtravelCoordinates/confirmCarbonOffset',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment4(client):
    """Test case for confirm_payment4

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
        path='/footprint/airtravelCoordinates/confirmPayment',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment_of_transaction4(client):
    """Test case for confirm_payment_of_transaction4

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
        path='/footprint/airtravelCoordinates/confirmTransaction',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirms_planting4(client):
    """Test case for confirms_planting4

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
        path='/footprint/airtravelCoordinates/confirmPlanting',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

