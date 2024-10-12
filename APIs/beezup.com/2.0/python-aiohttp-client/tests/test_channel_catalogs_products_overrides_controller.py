# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_product_value_override_copy(client):
    """Test case for configure_channel_catalog_product_value_override_copy

    Copy channel catalog product value override
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/overrides/copy'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_catalog_product_value_override(client):
    """Test case for delete_channel_catalog_product_value_override

    Delete a specific channel catalog product value override
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/overrides/{channel_column_id}'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67', channel_column_id='8a76f06a-fefc-4c0d-bcfe-b210f1482977'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_product_value_override_copy(client):
    """Test case for get_channel_catalog_product_value_override_copy

    Get channel catalog product value override compatibilities status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/overrides/copy'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_override_channel_catalog_product_values(client):
    """Test case for override_channel_catalog_product_values

    Override channel catalog product values
    """
    body = {'key': 'body_example'}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/overrides'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

