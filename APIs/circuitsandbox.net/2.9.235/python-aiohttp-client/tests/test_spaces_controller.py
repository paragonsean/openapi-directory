# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_participants_search_result import AddParticipantsSearchResult
from openapi_server.models.basic_search_result import BasicSearchResult
from openapi_server.models.directory_result import DirectoryResult
from openapi_server.models.flagged_items_result import FlaggedItemsResult
from openapi_server.models.label_ids import LabelIds
from openapi_server.models.participants_import_data_result import ParticipantsImportDataResult
from openapi_server.models.participants_like_result import ParticipantsLikeResult
from openapi_server.models.participants_search_result import ParticipantsSearchResult
from openapi_server.models.participants_search_result_large import ParticipantsSearchResultLarge
from openapi_server.models.space_pinned_topic import SpacePinnedTopic
from openapi_server.models.space_reply import SpaceReply
from openapi_server.models.space_search_result_detailed_back import SpaceSearchResultDetailedBack
from openapi_server.models.space_topic import SpaceTopic
from openapi_server.models.space_topic_with_replies import SpaceTopicWithReplies
from openapi_server.models.spaces_search_term_result import SpacesSearchTermResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_participants_to_space(client):
    """Test case for add_participants_to_space

    Add Participant to Space
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'role': DEFAULT,
        'user_id': ['user_id_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{id}/participant'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_recent_space_search(client):
    """Test case for add_recent_space_search

    Add recent search 
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'end_time': '2013-10-20T19:20:30+01:00',
        'scope': 'scope_example',
        'search_term': 'search_term_example',
        'start_time': '2013-10-20T19:20:30+01:00'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/search/add/recent',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_assign_labels(client):
    """Test case for assign_labels

    Assign labels
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'labels': ['labels_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{id}/labels/assign'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_space_search(client):
    """Test case for cancel_space_search

    Cancels a space search of a client.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/search/cancel/{search_id}'.format(search_id='search_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_reply(client):
    """Test case for create_reply

    creates a reply to a topic
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'complex': True,
        'content': 'content_example',
        'form_meta_data': 'form_meta_data_example',
        'mentioned_user': 'mentioned_user_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{space_id}/topic/{topic_id}/reply'.format(space_id='space_id_example', topic_id='topic_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_space(client):
    """Test case for create_space

    Create a space
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'access_mode_type': INTERNAL_ONLY,
        'description': 'description_example',
        'large_picture_base64': 'large_picture_base64_example',
        'name': 'name_example',
        'role': AUTHOR,
        'small_picture_base64': 'small_picture_base64_example',
        'status': ENABLED,
        'tags': ['tags_example'],
        'type': SECRET
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_space_topic(client):
    """Test case for create_space_topic

    creates a new space topic
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'complex': True,
        'content': 'content_example',
        'content_tags': ['content_tags_example'],
        'form_meta_data': 'form_meta_data_example',
        'mentioned_user': 'mentioned_user_example',
        'subject': 'subject_example',
        'tags': ['tags_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{space_id}/topic'.format(space_id='space_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_space(client):
    """Test case for delete_space

    Delete a space
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/spaces/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_space_item(client):
    """Test case for delete_space_item

    deletes a space item
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/spaces/item/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_deny_space_acces(client):
    """Test case for deny_space_acces

    Deny access for a space
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'reason': 'reason_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{space_id}/participant/{participant_id}/deny'.format(space_id='space_id_example', participant_id='participant_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exists_space_name(client):
    """Test case for exists_space_name

    Space name exists
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/exists/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flag_space_item(client):
    """Test case for flag_space_item

    flag a space item
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/flag/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_directory(client):
    """Test case for get_directory

    Get the directory
    """
    params = [('sortBy', LAST_CONTENT),
                    ('sortOrder', ASCENDING),
                    ('filter', NONE),
                    ('query', 'query_example'),
                    ('pagePointer', 'page_pointer_example'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/directory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flagged_items(client):
    """Test case for get_flagged_items

    Get flagged items
    """
    params = [('searchDirection', BEFORE),
                    ('timestamp', '2013-10-20T19:20:30+01:00'),
                    ('searchPointer', 'search_pointer_example'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/flagged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_likes(client):
    """Test case for get_likes

    Get the likes of an item
    """
    params = [('searchPointer', 'search_pointer_example'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/likes/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_participants_import_data(client):
    """Test case for get_participants_import_data

    missing documentation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{space_id}/participant/import'.format(space_id='space_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pending_participants(client):
    """Test case for get_pending_participants

    Get the pending participants of a space
    """
    params = [('searchPointer', 'search_pointer_example'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{id}/participants/pending'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pinned_topics(client):
    """Test case for get_pinned_topics

    Retrieve pinned topics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{id}/pinnedTopics'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_searches(client):
    """Test case for get_recent_searches

    Retrieve recent space searches
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/search/recent',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_space_participants(client):
    """Test case for get_space_participants

    Get the participants of a space
    """
    params = [('sortBy', NAME),
                    ('sortOrder', ASCENDING),
                    ('filterType', 'filter_type_example'),
                    ('filterValue', 'filter_value_example'),
                    ('query', 'query_example'),
                    ('searchPointer', 'search_pointer_example'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{id}/participants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_space_replies(client):
    """Test case for get_space_replies

    Gets space replies
    """
    params = [('searchDirection', BEFORE),
                    ('timestamp', '2013-10-20T19:20:30+01:00'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{space_id}/topic/{topic_id}/reply'.format(space_id='space_id_example', topic_id='topic_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_space_topics(client):
    """Test case for get_space_topics

    Gets space topics
    """
    params = [('searchDirection', BEFORE),
                    ('timestamp', '2013-10-20T19:20:30+01:00'),
                    ('numberOfResults', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{space_id}/topics'.format(space_id='space_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spaces(client):
    """Test case for get_spaces

    Get the spaces
    """
    params = [('timestamp', '2013-10-20T19:20:30+01:00'),
                    ('numberOfResults', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spaces_by_ids(client):
    """Test case for get_spaces_by_ids

    Get the spaces by their ids
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grant_space_acces(client):
    """Test case for grant_space_acces

    grant access for a space
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{space_id}/participant/{participant_id}/grant'.format(space_id='space_id_example', participant_id='participant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_join_space(client):
    """Test case for join_space

    Join a space
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{id}/join'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leave_space(client):
    """Test case for leave_space

    Leave a space
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{id}/leave'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_like_space_item(client):
    """Test case for like_space_item

    Like a space item
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/like/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_pin_topic(client):
    """Test case for pin_topic

    Pin a topic
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'position': 3.4
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{topic_id}/pin'.format(topic_id='topic_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_request_space_acces(client):
    """Test case for request_space_acces

    request access for a space
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'reason': 'reason_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{space_id}/participant/request'.format(space_id='space_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_participants_to_add(client):
    """Test case for search_participants_to_add

    Finds participants to add to add to a space 
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{id}/searchParticipantsToAdd'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_space_participants(client):
    """Test case for search_space_participants

    Get the participants of a space
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{id}/searchSpaceParticipants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_basic_spaces_search(client):
    """Test case for start_basic_spaces_search

    starts a basic search in spaces
    """
    params = [('scope', 'scope_example'),
                    ('searchTerm', 'search_term_example'),
                    ('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('prioritySpaces', ['priority_spaces_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/search/startBasic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_detailed_space_search(client):
    """Test case for start_detailed_space_search

    starts a detailed search in a space
    """
    params = [('scope', 'scope_example'),
                    ('searchTerm', 'search_term_example'),
                    ('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('spaceId', 'space_id_example'),
                    ('searchId', 'search_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/search/startDetailed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_unassign_labels(client):
    """Test case for unassign_labels

    Unassign labels
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'label_ids': ['label_ids_example']
        }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/spaces/{id}/labels/unassign'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unflag_space_item(client):
    """Test case for unflag_space_item

    Unflag a space item
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/unflag/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlike_space_item(client):
    """Test case for unlike_space_item

    Unlike a space item
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/unlike/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unpin_topic(client):
    """Test case for unpin_topic

    Unpin a topic
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{topic_id}/unpin'.format(topic_id='topic_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_participant_in_space(client):
    """Test case for update_participant_in_space

    Update participant
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'role': 'role_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{space_id}/participant'.format(space_id='space_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_read_timestamp(client):
    """Test case for update_read_timestamp

    Update read timestamp
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'timestamp': '2013-10-20T19:20:30+01:00'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{id}/updateTimestamp'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_space(client):
    """Test case for update_space

    Update a space
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'access_mode_type': NO_CHANGE,
        'description': 'description_example',
        'large_picture_base64': 'large_picture_base64_example',
        'name': 'name_example',
        'owner_id': 'owner_id_example',
        'role': NO_CHANGE,
        'small_picture_base64': 'small_picture_base64_example',
        'status': ENABLED,
        'tags': ['tags_example'],
        'type': NO_CHANGE
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{id}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_space_reply(client):
    """Test case for update_space_reply

    Updates a space reply
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'complex': True,
        'content': 'content_example',
        'form_meta_data': 'form_meta_data_example',
        'mentioned_users': ['mentioned_users_example']
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{space_id}/topic/{topic_id}/reply/{reply_id}'.format(space_id='space_id_example', topic_id='topic_id_example', reply_id='reply_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_space_topic(client):
    """Test case for update_space_topic

    Updates a topic
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'attachments': ['attachments_example'],
        'complex': True,
        'content': 'content_example',
        'content_tags': ['content_tags_example'],
        'form_meta_data': 'form_meta_data_example',
        'mentioned_users': ['mentioned_users_example'],
        'subject': 'subject_example',
        'tags': ['tags_example']
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{space_id}/topic/{topic_id}'.format(space_id='space_id_example', topic_id='topic_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_topic_tags(client):
    """Test case for update_topic_tags

    Update tags
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'tags': ['tags_example']
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/topic/{topic_id}/updateTags'.format(topic_id='topic_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_get_topic_with_replies(client):
    """Test case for v2_get_topic_with_replies

    Gets space replies and a topic
    """
    params = [('numberOfReplies', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/spaces/{space_id}/topic/{topic_id}'.format(space_id='space_id_example', topic_id='topic_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_remove_participants_from_space(client):
    """Test case for v2_remove_participants_from_space

    Removes participants from a space
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'user_ids': ['user_ids_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/spaces/{id}/participant/remove'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_update_welcome_box_content(client):
    """Test case for v2_update_welcome_box_content

    Update content of welcome box
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'display_welcome_box': False
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/spaces/{space_id}/welcomebox/{content}'.format(space_id='space_id_example', content='content_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

