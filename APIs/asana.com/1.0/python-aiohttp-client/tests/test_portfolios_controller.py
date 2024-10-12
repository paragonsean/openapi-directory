# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_custom_field_setting_for_portfolio200_response import AddCustomFieldSettingForPortfolio200Response
from openapi_server.models.add_custom_field_setting_for_portfolio_request import AddCustomFieldSettingForPortfolioRequest
from openapi_server.models.add_item_for_portfolio_request import AddItemForPortfolioRequest
from openapi_server.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest
from openapi_server.models.create_portfolio201_response import CreatePortfolio201Response
from openapi_server.models.create_portfolio_request import CreatePortfolioRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
from openapi_server.models.get_portfolios200_response import GetPortfolios200Response
from openapi_server.models.remove_custom_field_setting_for_portfolio_request import RemoveCustomFieldSettingForPortfolioRequest
from openapi_server.models.remove_item_for_portfolio_request import RemoveItemForPortfolioRequest
from openapi_server.models.remove_members_for_portfolio_request import RemoveMembersForPortfolioRequest


pytestmark = pytest.mark.asyncio

async def test_add_custom_field_setting_for_portfolio(client):
    """Test case for add_custom_field_setting_for_portfolio

    Add a custom field to a portfolio
    """
    body = openapi_server.AddCustomFieldSettingForPortfolioRequest()
    params = [('opt_pretty', true)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/addCustomFieldSetting'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_item_for_portfolio(client):
    """Test case for add_item_for_portfolio

    Add a portfolio item
    """
    body = openapi_server.AddItemForPortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/addItem'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_for_portfolio(client):
    """Test case for add_members_for_portfolio

    Add users to a portfolio
    """
    body = openapi_server.AddMembersForPortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/addMembers'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_portfolio(client):
    """Test case for create_portfolio

    Create a portfolio
    """
    body = openapi_server.CreatePortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_portfolio(client):
    """Test case for delete_portfolio

    Delete a portfolio
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/1.0/portfolios/{portfolio_gid}'.format(portfolio_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_for_portfolio(client):
    """Test case for get_items_for_portfolio

    Get portfolio items
    """
    params = [('opt_pretty', true),
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
        path='/api/1.0/portfolios/{portfolio_gid}/items'.format(portfolio_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolio(client):
    """Test case for get_portfolio

    Get a portfolio
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
        path='/api/1.0/portfolios/{portfolio_gid}'.format(portfolio_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_portfolios(client):
    """Test case for get_portfolios

    Get multiple portfolios
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'),
                    ('workspace', '1331'),
                    ('owner', '14916')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/portfolios',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_custom_field_setting_for_portfolio(client):
    """Test case for remove_custom_field_setting_for_portfolio

    Remove a custom field from a portfolio
    """
    body = openapi_server.RemoveCustomFieldSettingForPortfolioRequest()
    params = [('opt_pretty', true)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/removeCustomFieldSetting'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_item_for_portfolio(client):
    """Test case for remove_item_for_portfolio

    Remove a portfolio item
    """
    body = openapi_server.RemoveItemForPortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/removeItem'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_members_for_portfolio(client):
    """Test case for remove_members_for_portfolio

    Remove users from a portfolio
    """
    body = openapi_server.RemoveMembersForPortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/portfolios/{portfolio_gid}/removeMembers'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_portfolio(client):
    """Test case for update_portfolio

    Update a portfolio
    """
    body = openapi_server.CreatePortfolioRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/1.0/portfolios/{portfolio_gid}'.format(portfolio_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

