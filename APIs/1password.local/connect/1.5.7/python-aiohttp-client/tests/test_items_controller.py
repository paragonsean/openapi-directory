# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.full_item import FullItem
from openapi_server.models.item import Item
from openapi_server.models.patch_inner import PatchInner


pytestmark = pytest.mark.asyncio

async def test_create_vault_item(client):
    """Test case for create_vault_item

    Create a new Item
    """
    body = {"title":"title","version":0,"lastEditedBy":"lastEditedBy","sections":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"tags":["tags","tags"],"createdAt":"2000-01-23T04:56:07.000+00:00","urls":[{"href":"https://example.com","primary":True},{"href":"https://example.org"}],"files":[{"content":"VGhlIGZ1dHVyZSBiZWxvbmdzIHRvIHRoZSBjdXJpb3VzLgo=","content_path":"v1/vaults/ionaiwtdvgclrixbt6ztpqcxnq/items/p7eflcy7f5mk7vg6zrzf5rjjyu/files/6r65pjq33banznomn7q22sj44e/content","id":"6r65pjq33banznomn7q22sj44e","name":"foo.txt","size":35},{"content":"VGhlIGZ1dHVyZSBiZWxvbmdzIHRvIHRoZSBjdXJpb3VzLgo=","content_path":"v1/vaults/ionaiwtdvgclrixbt6ztpqcxnq/items/p7eflcy7f5mk7vg6zrzf5rjjyu/files/6r65pjq33banznomn7q22sj44e/content","id":"6r65pjq33banznomn7q22sj44e","name":"foo.txt","size":35}],"id":"id","state":"ARCHIVED","category":"LOGIN","fields":[{"entropy":6.027456183070403,"purpose":"","recipe":{"characterSets":["LETTERS","LETTERS"],"length":10,"excludeCharacters":"abc1"},"section":{"id":"id"},"id":"id","label":"label","type":"STRING","generate":False,"value":"value"},{"entropy":6.027456183070403,"purpose":"","recipe":{"characterSets":["LETTERS","LETTERS"],"length":10,"excludeCharacters":"abc1"},"section":{"id":"id"},"id":"id","label":"label","type":"STRING","generate":False,"value":"value"}],"favorite":False,"vault":{"id":"id"},"updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/vaults/{vault_uuid}/items'.format(vault_uuid='vault_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vault_item(client):
    """Test case for delete_vault_item

    Delete an Item
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/vaults/{vault_uuid}/items/{item_uuid}'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vault_item_by_id(client):
    """Test case for get_vault_item_by_id

    Get the details of an Item
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}/items/{item_uuid}'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vault_items(client):
    """Test case for get_vault_items

    Get all items for inside a Vault
    """
    params = [('filter', 'title eq \"Some Item Name\"')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/vaults/{vault_uuid}/items'.format(vault_uuid='vault_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_vault_item(client):
    """Test case for patch_vault_item

    Update a subset of Item attributes
    """
    body = [{"op":"replace","path":"/favorite","value":true},{"op":"remove","path":"/tags/1"}]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/vaults/{vault_uuid}/items/{item_uuid}'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vault_item(client):
    """Test case for update_vault_item

    Update an Item
    """
    body = {"title":"title","version":0,"lastEditedBy":"lastEditedBy","sections":[{"id":"id","label":"label"},{"id":"id","label":"label"}],"tags":["tags","tags"],"createdAt":"2000-01-23T04:56:07.000+00:00","urls":[{"href":"https://example.com","primary":True},{"href":"https://example.org"}],"files":[{"content":"VGhlIGZ1dHVyZSBiZWxvbmdzIHRvIHRoZSBjdXJpb3VzLgo=","content_path":"v1/vaults/ionaiwtdvgclrixbt6ztpqcxnq/items/p7eflcy7f5mk7vg6zrzf5rjjyu/files/6r65pjq33banznomn7q22sj44e/content","id":"6r65pjq33banznomn7q22sj44e","name":"foo.txt","size":35},{"content":"VGhlIGZ1dHVyZSBiZWxvbmdzIHRvIHRoZSBjdXJpb3VzLgo=","content_path":"v1/vaults/ionaiwtdvgclrixbt6ztpqcxnq/items/p7eflcy7f5mk7vg6zrzf5rjjyu/files/6r65pjq33banznomn7q22sj44e/content","id":"6r65pjq33banznomn7q22sj44e","name":"foo.txt","size":35}],"id":"id","state":"ARCHIVED","category":"LOGIN","fields":[{"entropy":6.027456183070403,"purpose":"","recipe":{"characterSets":["LETTERS","LETTERS"],"length":10,"excludeCharacters":"abc1"},"section":{"id":"id"},"id":"id","label":"label","type":"STRING","generate":False,"value":"value"},{"entropy":6.027456183070403,"purpose":"","recipe":{"characterSets":["LETTERS","LETTERS"],"length":10,"excludeCharacters":"abc1"},"section":{"id":"id"},"id":"id","label":"label","type":"STRING","generate":False,"value":"value"}],"favorite":False,"vault":{"id":"id"},"updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/vaults/{vault_uuid}/items/{item_uuid}'.format(vault_uuid='vault_uuid_example', item_uuid='item_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

