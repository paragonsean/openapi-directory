# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_comment_reaction_entity import FileCommentReactionEntity


pytestmark = pytest.mark.asyncio

async def test_delete_file_comment_reactions_id(client):
    """Test case for delete_file_comment_reactions_id

    Delete File Comment Reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/file_comment_reactions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_file_comment_reactions(client):
    """Test case for post_file_comment_reactions

    Create File Comment Reaction
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('emoji', 'emoji_example')
    data.add_field('file_comment_id', 56)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/file_comment_reactions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

