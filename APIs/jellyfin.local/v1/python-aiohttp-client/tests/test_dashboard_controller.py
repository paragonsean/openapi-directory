# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration_page_info import ConfigurationPageInfo
from openapi_server.models.configuration_page_type import ConfigurationPageType
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_configuration_pages(client):
    """Test case for get_configuration_pages

    Gets the configuration pages.
    """
    params = [('enableInMainMenu', True),
                    ('pageType', openapi_server.ConfigurationPageType())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/web/ConfigurationPages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard_configuration_page(client):
    """Test case for get_dashboard_configuration_page

    Gets a dashboard configuration page.
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/web/ConfigurationPage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

