# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_transaction(client):
    """Test case for create_transaction

    Create Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'date_closed': '2013-10-20T19:20:30+01:00',
        'date_created': '2013-10-20T19:20:30+01:00',
        'licensee_number': 'licensee_number_example',
        'number': 'number_example',
        'payment_method': 'payment_method_example',
        'source': 'source_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/transaction',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transaction(client):
    """Test case for get_transaction

    Get Transaction 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/transaction/{transaction_number}'.format(transaction_number='transaction_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_transactions(client):
    """Test case for list_transactions

    List Transactions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/transaction',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_transaction(client):
    """Test case for update_transaction

    Update Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'date_closed': '2013-10-20T19:20:30+01:00',
        'date_created': '2013-10-20T19:20:30+01:00',
        'number': 'number_example',
        'payment_method': 'payment_method_example',
        'source': 'source_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/transaction/{transaction_number}'.format(transaction_number='transaction_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

