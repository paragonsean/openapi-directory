# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airtravel_multileg_request import AirtravelMultilegRequest


pytestmark = pytest.mark.asyncio

async def test_airtravel_multileg(client):
    """Test case for airtravel_multileg

    airtravelMultileg
    """
    body = {"apiKey_l1":"d95fead6-e8a6-4547-9fb9-7835101a3960","apiKey_l2":"c60f8db5-7204-4427-960d-27400c38b166","leg1":{"destination_airport_code":"DXB","origin_airport_code":"KHI","travel_class":"Economy"},"leg2":{"destination_airport_code":"LHR","origin_airport_code":"DXB","travel_class":"Business"},"leg3":{"destination_airport_code":"KHI","origin_airport_code":"FRA","travel_class":"Premium Economy"},"legs_count":"2","number_of_passengers":"2","travel_mode":"multileg"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/footprint/airtravelMultileg',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_carbon_offset3(client):
    """Test case for confirm_carbon_offset3

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
        path='/footprint/airtravelMultileg/confirmCarbonOffset',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment3(client):
    """Test case for confirm_payment3

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
        path='/footprint/airtravelMultileg/confirmPayment',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirm_payment_of_transaction3(client):
    """Test case for confirm_payment_of_transaction3

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
        path='/footprint/airtravelMultileg/confirmTransaction',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_confirms_planting3(client):
    """Test case for confirms_planting3

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
        path='/footprint/airtravelMultileg/confirmPlanting',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

