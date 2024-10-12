# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_portfolio_membership200_response import GetPortfolioMembership200Response
from openapi_server.models.get_portfolio_memberships200_response import GetPortfolioMemberships200Response


pytestmark = pytest.mark.asyncio

async def test_get_portfolio_membership(client):
    """Test case for get_portfolio_membership

    Get a portfolio membership
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/portfolio_memberships/{portfolio_membership_gid}'.format(portfolio_membership_gid='1331'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolio_memberships(client):
    """Test case for get_portfolio_memberships

    Get multiple portfolio memberships
    """
    params = [('portfolio', '12345'),
                    ('workspace', '12345'),
                    ('user', 'me'),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/portfolio_memberships',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolio_memberships_for_portfolio(client):
    """Test case for get_portfolio_memberships_for_portfolio

    Get memberships from a portfolio
    """
    params = [('user', 'me'),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/portfolios/{portfolio_gid}/portfolio_memberships'.format(portfolio_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

