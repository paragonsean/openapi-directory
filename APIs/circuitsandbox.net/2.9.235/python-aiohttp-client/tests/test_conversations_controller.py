# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation import Conversation
from openapi_server.models.conversation_details import ConversationDetails
from openapi_server.models.conversation_item import ConversationItem
from openapi_server.models.conversation_participants_list import ConversationParticipantsList
from openapi_server.models.conversation_search_result import ConversationSearchResult
from openapi_server.models.conversations_page import ConversationsPage
from openapi_server.models.label import Label
from openapi_server.models.pinned_topic import PinnedTopic
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_add_favorite(client):
    """Test case for add_favorite

    Adds a conversation to the favorites
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/favorite'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_label(client):
    """Test case for add_label

    Add a user label
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'label': 'label_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/users/labels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_moderators(client):
    """Test case for add_moderators

    Add moderators
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'moderators': ['moderators_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/moderators'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_participant_community(client):
    """Test case for add_participant_community

    Adds participants to a community
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'participants': ['participants_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/community/{conv_id}/participants'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_participant_group(client):
    """Test case for add_participant_group

    Adds participants to a group conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'participants': ['participants_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/group/{conv_id}/participants'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_text_item(client):
    """Test case for add_text_item

    Adds a message to a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'content': 'content_example',
        'form_meta_data': 'form_meta_data_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/messages'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_text_item_with_parent(client):
    """Test case for add_text_item_with_parent

    Adds a message to an item
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'content': 'content_example',
        'form_meta_data': 'form_meta_data_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_conversation(client):
    """Test case for archive_conversation

    Archives conversation
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/archive'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_assign_label(client):
    """Test case for assign_label

    Adds a label to a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'label': 'label_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/label'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_community_conversation(client):
    """Test case for create_community_conversation

    Creates a community conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'participants': ['participants_example'],
        'topic': 'topic_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/community',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_direct_conversation(client):
    """Test case for create_direct_conversation

    Creates a 1-to-1 conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'participant': 'participant_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/direct',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_group_conversation(client):
    """Test case for create_group_conversation

    Creates a group conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'participants': ['participants_example'],
        'topic': 'topic_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/group',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_favorite(client):
    """Test case for delete_favorite

    Removes a conversation from favorites
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/favorite'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_text_item(client):
    """Test case for delete_text_item

    Deletes a message from a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_flag_item(client):
    """Test case for flag_item

    Adds a flag to a message in a conversation
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'item_creation_time': 'item_creation_time_example',
        'parent_id': 'parent_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}/flag'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_community_conversations(client):
    """Test case for get_community_conversations

    Gets a list of communities
    """
    params = [('sort', ALPHABETICALLY),
                    ('order', ASCENDING),
                    ('includeOwn', False),
                    ('startIndex', 0),
                    ('results', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/community',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversation_items(client):
    """Test case for get_conversation_items

    Gets a list of conversation items
    """
    params = [('modTime', '2013-10-20T19:20:30+01:00'),
                    ('direction', BEFORE),
                    ('results', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}/items'.format(conv_id='conv_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversationby_id(client):
    """Test case for get_conversationby_id

    Gets a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversations(client):
    """Test case for get_conversations

    Gets a list of conversations
    """
    params = [('modTime', '2013-10-20T19:20:30+01:00'),
                    ('direction', BEFORE),
                    ('results', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversations_by_id(client):
    """Test case for get_conversations_by_id

    Gets conversations
    """
    params = [('convIds', ['conv_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/byIds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conversations_by_label(client):
    """Test case for get_conversations_by_label

    Returns conversations with a certain label
    """
    params = [('nextPagePointer', 'next_page_pointer_example'),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/label/{label_id}'.format(label_id='label_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_direct_conversation(client):
    """Test case for get_direct_conversation

    Checks for a 1-to-1 conversation
    """
    params = [('participant', 'participant_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/direct',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_favorite_conversations(client):
    """Test case for get_favorite_conversations

    Gets favorite conversations
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/favorite',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flag_item(client):
    """Test case for get_flag_item

    Gets a list of the flagged messages of a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}/messages/flag'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flag_item_conv(client):
    """Test case for get_flag_item_conv

    Gets a list of the flagged messages
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/messages/flag',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_join_details(client):
    """Test case for get_join_details

    Gets the conference details of a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}/conversationdetails'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_join_details_multiple(client):
    """Test case for get_join_details_multiple

    Gets the conference details for multiple conversations
    """
    params = [('convIds', ['conv_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/conversationdetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_participants_by_conv_id(client):
    """Test case for get_participants_by_conv_id

    Performs a list of participants
    """
    params = [('pageSize', 3.4),
                    ('name', 'name_example'),
                    ('type', REGULAR),
                    ('searchPointer', 'search_pointer_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}/participants'.format(conv_id='conv_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pinned_conversations(client):
    """Test case for get_pinned_conversations

    Returns pinned topics of a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/{conv_id}/pins'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_conversationtem(client):
    """Test case for get_single_conversationtem

    Returns a text item
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/messages/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_join_community_conversation(client):
    """Test case for join_community_conversation

    Adds the authenticated user to a community
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/community/{conv_id}/join'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_like_item(client):
    """Test case for like_item

    Adds a \"like\" to a message
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}/like'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_moderate_conversation(client):
    """Test case for moderate_conversation

    Set conversation moderated
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/moderate/{conv_id}'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pin_a_conversation(client):
    """Test case for pin_a_conversation

    Pins a topic of a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/{conv_id}/pins/{item_id}'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_label(client):
    """Test case for remove_label

    Remove a user label
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/users/labels/{label_id}'.format(label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_remove_moderators(client):
    """Test case for remove_moderators

    Remove moderators
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'moderators': ['moderators_example']
        }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/moderators'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_participant_community(client):
    """Test case for remove_participant_community

    Removes participants from a community
    """
    params = [('participants', ['participants_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/community/{conv_id}/participants'.format(conv_id='conv_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_participant_group(client):
    """Test case for remove_participant_group

    Removes participants from a group conversation
    """
    params = [('participants', ['participants_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/group/{conv_id}/participants'.format(conv_id='conv_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resolve_invitation_token(client):
    """Test case for resolve_invitation_token

    Resolves an invite token to a conversation
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/resolveinvitetoken',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_conversations(client):
    """Test case for search_conversations

    Performs a conversation search
    """
    params = [('term', 'term_example'),
                    ('includeItemIds', False),
                    ('scope', ALL)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/conversations/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_un_flag_item(client):
    """Test case for un_flag_item

    Removes the flag from a message
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}/flag'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_un_pin_a_conversation(client):
    """Test case for un_pin_a_conversation

    Unpins a topic of a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/pins/{item_id}'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unassign_label(client):
    """Test case for unassign_label

    Removes a label from a conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/label/{label_id}'.format(conv_id='conv_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_undo_archive_conversation(client):
    """Test case for undo_archive_conversation

    Unmute conversation
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/archive'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlike_item(client):
    """Test case for unlike_item

    Removes a \"like\" from a message
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}/like'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmoderate_conversation(client):
    """Test case for unmoderate_conversation

    Set conversation unmoderated
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/conversations/unmoderate/{conv_id}'.format(conv_id='conv_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation_community(client):
    """Test case for update_conversation_community

    Updates the information of a community
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'topic': 'topic_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/conversations/community/{conv_id}'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conversation_group(client):
    """Test case for update_conversation_group

    Updates the information of a group conversation
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'topic': 'topic_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/conversations/group/{conv_id}'.format(conv_id='conv_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_profile(client):
    """Test case for update_profile

    Updates the user profile
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'firstname': 'firstname_example',
        'job_title': 'job_title_example',
        'lastname': 'lastname_example',
        'locale': 'locale_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/users/profile',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_text_item(client):
    """Test case for update_text_item

    Updates a message
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'content': 'content_example',
        'form_meta_data': 'form_meta_data_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/conversations/{conv_id}/messages/{item_id}'.format(conv_id='conv_id_example', item_id='item_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

