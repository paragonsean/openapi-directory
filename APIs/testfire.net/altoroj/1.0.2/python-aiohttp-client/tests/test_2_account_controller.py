# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dates import Dates


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/api/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_balance(client):
    """Test case for get_account_balance

    
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/api/account/{account_no}'.format(account_no='account_no_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions(client):
    """Test case for get_transactions

    
    """
    body = openapi_server.Dates()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/api/account/{account_no}/transactions'.format(account_no='account_no_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_last_ten_transactions(client):
    """Test case for show_last_ten_transactions

    
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/api/account/{account_no}/transactions'.format(account_no='account_no_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

