# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_custom_field_settings_for_portfolio200_response import GetCustomFieldSettingsForPortfolio200Response


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_settings_for_portfolio(client):
    """Test case for get_custom_field_settings_for_portfolio

    Get a portfolio's custom fields
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
        path='/api/1.0/portfolios/{portfolio_gid}/custom_field_settings'.format(portfolio_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_settings_for_project(client):
    """Test case for get_custom_field_settings_for_project

    Get a project's custom fields
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
        path='/api/1.0/projects/{project_gid}/custom_field_settings'.format(project_gid='1331'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

