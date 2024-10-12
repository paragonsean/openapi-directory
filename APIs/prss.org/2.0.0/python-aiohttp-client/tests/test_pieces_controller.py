# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.piece import Piece


pytestmark = pytest.mark.asyncio

async def test_api_v2_pieces_get(client):
    """Test case for api_v2_pieces_get

    Returns the pieces matching the query parameters.
    """
    params = [('episodeId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pieces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_pieces_id_delete(client):
    """Test case for api_v2_pieces_id_delete

    Deletes the piece with the given ID.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/pieces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_pieces_id_get(client):
    """Test case for api_v2_pieces_id_get

    Returns the piece matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pieces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_pieces_post(client):
    """Test case for api_v2_pieces_post

    Create a new piece.
    """
    body = {"lastModifiedDate":"2000-01-23T04:56:07.000+00:00","relativeEndTime":5,"description":"description","episodeId":0,"fullDescription":"fullDescription","title":"title","imageFileSize":1,"relativeStartTime":5,"segmentNumber":1,"imageCdDriveUri":"imageCdDriveUri","contributor":"contributor","createdDate":"2000-01-23T04:56:07.000+00:00","imageOriginalFileName":"imageOriginalFileName","imageFileName":"imageFileName","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/pieces',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

