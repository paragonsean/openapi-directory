# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_board_assets_result import AddBoardAssetsResult
from openapi_server.models.board_asset import BoardAsset
from openapi_server.models.board_created import BoardCreated
from openapi_server.models.board_detail import BoardDetail
from openapi_server.models.board_info import BoardInfo
from openapi_server.models.board_list import BoardList
from openapi_server.models.board_relationship import BoardRelationship
from openapi_server.models.board_sort_order import BoardSortOrder
from openapi_server.models.comment_created import CommentCreated
from openapi_server.models.comment_request import CommentRequest
from openapi_server.models.comments_list import CommentsList


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_assets_asset_id_delete(client):
    """Test case for v3_boards_board_id_assets_asset_id_delete

    Remove an asset from a board
    """
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/boards/{board_id}/assets/{asset_id}'.format(board_id='board_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_assets_asset_id_put(client):
    """Test case for v3_boards_board_id_assets_asset_id_put

    Add an asset to a board
    """
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/boards/{board_id}/assets/{asset_id}'.format(board_id='board_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_assets_delete(client):
    """Test case for v3_boards_board_id_assets_delete

    Remove assets from a board
    """
    params = [('asset_ids', ['asset_ids_example'])]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/boards/{board_id}/assets'.format(board_id='board_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_assets_put(client):
    """Test case for v3_boards_board_id_assets_put

    Add assets to a board
    """
    body = {"asset_id":"asset_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/boards/{board_id}/assets'.format(board_id='board_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_comments_comment_id_delete(client):
    """Test case for v3_boards_board_id_comments_comment_id_delete

    Delete a comment from a board
    """
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/boards/{board_id}/comments/{comment_id}'.format(board_id='board_id_example', comment_id='comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_comments_get(client):
    """Test case for v3_boards_board_id_comments_get

    Get comments from a board
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/boards/{board_id}/comments'.format(board_id='board_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_comments_post(client):
    """Test case for v3_boards_board_id_comments_post

    Add a comment to a board
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/boards/{board_id}/comments'.format(board_id='board_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_delete(client):
    """Test case for v3_boards_board_id_delete

    Delete a board
    """
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/boards/{board_id}'.format(board_id='board_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_get(client):
    """Test case for v3_boards_board_id_get

    Get assets and metadata for a specific board
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/boards/{board_id}'.format(board_id='board_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_board_id_put(client):
    """Test case for v3_boards_board_id_put

    Update a board
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/boards/{board_id}'.format(board_id='board_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_get(client):
    """Test case for v3_boards_get

    Get all boards that the user participates in
    """
    params = [('page', 1),
                    ('board_relationship', openapi_server.BoardRelationship()),
                    ('sort_order', openapi_server.BoardSortOrder()),
                    ('pageSize', 30)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/boards',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_boards_post(client):
    """Test case for v3_boards_post

    Create a new board
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/boards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

