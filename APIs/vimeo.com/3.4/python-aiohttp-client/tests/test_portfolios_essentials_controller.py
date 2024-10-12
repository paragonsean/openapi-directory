# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.portfolio import Portfolio


pytestmark = pytest.mark.asyncio

async def test_get_portfolio(client):
    """Test case for get_portfolio

    Get a specific portfolio
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.portfolio+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/portfolios/{portfolio_id}'.format(portfolio_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolio_alt1(client):
    """Test case for get_portfolio_alt1

    Get a specific portfolio
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.portfolio+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/portfolios/{portfolio_id}'.format(portfolio_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolios(client):
    """Test case for get_portfolios

    Get all the portfolios that belong to a user
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.portfolio+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/portfolios'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolios_alt1(client):
    """Test case for get_portfolios_alt1

    Get all the portfolios that belong to a user
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.portfolio+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/portfolios',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

