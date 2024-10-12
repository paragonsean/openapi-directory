# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.template import Template
from openapi_server.models.templates_list import TemplatesList


pytestmark = pytest.mark.asyncio

async def test_get_v3_gitignores(client):
    """Test case for get_v3_gitignores

    Get the list of the available template
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gitignores',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_gitignores_name(client):
    """Test case for get_v3_gitignores_name

    Get the text for a specific template present in local filesystem
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gitignores/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

