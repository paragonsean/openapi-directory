# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.extension import Extension


pytestmark = pytest.mark.asyncio

async def test_get_extensions(client):
    """Test case for get_extensions

    Get a list Extensions
    """
    params = [('ext_name', 'ext_name_example'),
                    ('siteids', 'siteids_example'),
                    ('ext_prefix', 'ext_prefix_example'),
                    ('version', 'version_example'),
                    ('vUpdate', 56),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/extensions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields_extensions(client):
    """Test case for get_fields_extensions

    Get the list of fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/extensions/metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ignore_extension_update(client):
    """Test case for ignore_extension_update

    Set 'ignore updates' for a given extension / site_id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/extensions/{id}/ignore'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unignore_extension_update(client):
    """Test case for unignore_extension_update

    Remove 'ignore updates' for a given extension
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/extensions/{id}/unignore'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_extension(client):
    """Test case for update_extension

    Update the extension on the remote site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/extensions/{id}/update'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

