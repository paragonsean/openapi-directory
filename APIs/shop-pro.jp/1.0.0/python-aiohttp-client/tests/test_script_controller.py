# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_shop_script_tag200_response import CreateShopScriptTag200Response
from openapi_server.models.create_shop_script_tag_request import CreateShopScriptTagRequest
from openapi_server.models.get_shop_script_tags200_response import GetShopScriptTags200Response


pytestmark = pytest.mark.asyncio

async def test_create_shop_script_tag(client):
    """Test case for create_shop_script_tag

    スクリプトタグの作成
    """
    body = openapi_server.CreateShopScriptTagRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/appstore/v1/script_tags.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_script_tag(client):
    """Test case for delete_script_tag

    スクリプトタグの削除
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/appstore/v1/script_tags/{script_tag_id_jso}'.format(script_tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shop_script_tag(client):
    """Test case for get_shop_script_tag

    スクリプトタグの取得
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/appstore/v1/script_tags/{script_tag_id_jso}'.format(script_tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shop_script_tags(client):
    """Test case for get_shop_script_tags

    スクリプトタグの取得
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/appstore/v1/script_tags.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_shop_script_tag(client):
    """Test case for update_shop_script_tag

    スクリプトタグの更新
    """
    body = openapi_server.CreateShopScriptTagRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/appstore/v1/script_tags/{script_tag_id_jso}'.format(script_tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

