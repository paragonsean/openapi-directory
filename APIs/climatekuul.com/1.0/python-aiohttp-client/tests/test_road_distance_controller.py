# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_carbon_offset5(client):
    """Test case for confirm_carbon_offset5

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
        path='/footprint/roadDistance/confirmCarbonOffset',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment5(client):
    """Test case for confirm_payment5

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
        path='/footprint/roadDistance/confirmPayment',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment_of_transaction5(client):
    """Test case for confirm_payment_of_transaction5

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
        path='/footprint/roadDistance/confirmTransaction',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirms_planting5(client):
    """Test case for confirms_planting5

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
        path='/footprint/roadDistance/confirmPlanting',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_road_distance(client):
    """Test case for road_distance

    RoadDistance
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'travel_distance': 56,
        'trip_end': 56,
        'trip_start': 56,
        'vehicle_make': 'vehicle_make_example',
        'vehicle_type': 'vehicle_type_example',
        'vehicle_year': 56
        }
    response = await client.request(
        method='POST',
        path='/footprint/roadDistance',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

