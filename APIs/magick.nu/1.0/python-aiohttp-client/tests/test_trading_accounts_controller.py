# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.password_dto import PasswordDTO
from openapi_server.models.trading_account import TradingAccount


pytestmark = pytest.mark.asyncio

async def test_post_trading_accounts(client):
    """Test case for post_trading_accounts

    Add a Trading Account
    """
    body = {"password":"password","brokerServer":"brokerServer","magickUsername":"magickUsername","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/tradingAccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_trading_accounts_password_username_brokerserver_mt4username(client):
    """Test case for put_trading_accounts_password_username_brokerserver_mt4username

    Update MT4 Account Password
    """
    body = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/tradingAccounts/password/{username}/{brokerserver}/{mt4username}'.format(username='username_example', brokerserver='brokerserver_example', mt4username='mt4username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

