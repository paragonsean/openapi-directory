# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.message_comment_reaction_entity import MessageCommentReactionEntity


pytestmark = pytest.mark.asyncio

async def test_delete_message_comment_reactions_id(client):
    """Test case for delete_message_comment_reactions_id

    Delete Message Comment Reaction
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/message_comment_reactions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_message_comment_reactions(client):
    """Test case for get_message_comment_reactions

    List Message Comment Reactions
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('message_comment_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/message_comment_reactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_message_comment_reactions_id(client):
    """Test case for get_message_comment_reactions_id

    Show Message Comment Reaction
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/message_comment_reactions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_message_comment_reactions(client):
    """Test case for post_message_comment_reactions

    Create Message Comment Reaction
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('emoji', 'emoji_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/message_comment_reactions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

