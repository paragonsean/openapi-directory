# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gitignore_template import GitignoreTemplate


pytestmark = pytest.mark.asyncio

async def test_gitignore_get_all_templates(client):
    """Test case for gitignore_get_all_templates

    Get all gitignore templates
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gitignore/templates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gitignore_get_template(client):
    """Test case for gitignore_get_template

    Get a gitignore template
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gitignore/templates/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

