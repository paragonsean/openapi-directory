# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.portfolio_account_model import PortfolioAccountModel
from openapi_server.models.portfolio_accounts_model import PortfolioAccountsModel


pytestmark = pytest.mark.asyncio

async def test_portfolio_accounts_get_by_id_planid(client):
    """Test case for portfolio_accounts_get_by_id_planid

    Retrieve a portfolio account
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/PortfolioAccounts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_portfolio_accounts_get_by_planid(client):
    """Test case for portfolio_accounts_get_by_planid

    Retrieve portfolio accounts
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/PortfolioAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

