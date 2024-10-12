# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blacklist_item_response_version import BlacklistItemResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_blacklist(client):
    """Test case for add_blacklist

    Add items to blacklist
    """
    blacklisted_items = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/blacklist.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=blacklisted_items,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_blacklist_items(client):
    """Test case for delete_blacklist_items

    Remove items from blacklist
    """
    blacklisted_item_ids = ['blacklisted_item_ids_example']
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/blacklist.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=blacklisted_item_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_blacklist(client):
    """Test case for get_blacklist

    Retrieve blacklisted items
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/blacklist.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_blacklist(client):
    """Test case for update_blacklist

    Update items in blacklist
    """
    blacklisted_items = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/blacklist.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=blacklisted_items,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

