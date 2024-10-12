# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_inline_script_tag201_response import CreateInlineScriptTag201Response
from openapi_server.models.create_inline_script_tag_request import CreateInlineScriptTagRequest
from openapi_server.models.get_inline_script_tags200_response import GetInlineScriptTags200Response


pytestmark = pytest.mark.asyncio

async def test_create_inline_script_tag(client):
    """Test case for create_inline_script_tag

    インラインスクリプトタグの登録
    """
    body = openapi_server.CreateInlineScriptTagRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/inline_script_tags.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_inline_script_tag(client):
    """Test case for delete_inline_script_tag

    インラインスクリプトタグの削除
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/inline_script_tags/{inline_script_tag_id_jso}'.format(inline_script_tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inline_script_tag(client):
    """Test case for get_inline_script_tag

    インラインスクリプトタグの取得
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/inline_script_tags/{inline_script_tag_id_jso}'.format(inline_script_tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inline_script_tags(client):
    """Test case for get_inline_script_tags

    インラインスクリプトタグの取得
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/inline_script_tags.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_inline_script_tag(client):
    """Test case for update_inline_script_tag

    インラインスクリプトタグの更新
    """
    body = openapi_server.CreateInlineScriptTagRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/inline_script_tags/{inline_script_tag_id_jso}'.format(inline_script_tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

