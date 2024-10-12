# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_hidden_items_request import AddHiddenItemsRequest
from openapi_server.models.add_items_to_personal_list_request import AddItemsToPersonalListRequest
from openapi_server.models.create_personal_list_request import CreatePersonalListRequest
from openapi_server.models.remove_items_from_personal_list_request import RemoveItemsFromPersonalListRequest
from openapi_server.models.reorder_a_user_s_lists_request import ReorderAUserSListsRequest
from openapi_server.models.reorder_personally_recommended_items_request import ReorderPersonallyRecommendedItemsRequest
from openapi_server.models.update_personal_list_request import UpdatePersonalListRequest


pytestmark = pytest.mark.asyncio

async def test_add_hidden_items(client):
    """Test case for add_hidden_items

    Add hidden items
    """
    body = openapi_server.AddHiddenItemsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/hidden/{section}'.format(section='calendar'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_items_to_personal_list(client):
    """Test case for add_items_to_personal_list

    Add items to personal list
    """
    body = openapi_server.AddItemsToPersonalListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists/{list_id}/items'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_follow_request(client):
    """Test case for approve_follow_request

    Approve follow request
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/requests/{id}'.format(id='123'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_personal_list(client):
    """Test case for create_personal_list

    Create personal list
    """
    body = openapi_server.CreatePersonalListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_a_users_personal_list(client):
    """Test case for delete_a_users_personal_list

    Delete a user's personal list
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}/lists/{list_id}'.format(id='id_example', list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_follow_request(client):
    """Test case for deny_follow_request

    Deny follow request
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/requests/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_follow_this_user(client):
    """Test case for follow_this_user

    Follow this user
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/follow'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_users_personal_lists(client):
    """Test case for get_a_users_personal_lists

    Get a user's personal lists
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_lists_a_user_can_collaborate_on(client):
    """Test case for get_all_lists_a_user_can_collaborate_on

    Get all lists a user can collaborate on
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists/collaborations'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments(client):
    """Test case for get_comments

    Get comments
    """
    params = [('include_replies', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/comments/{comment_type}/{type}'.format(id='sean', comment_type='all', type='all'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_follow_requests(client):
    """Test case for get_follow_requests

    Get follow requests
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/requests',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_followers(client):
    """Test case for get_followers

    Get followers
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/followers'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_following(client):
    """Test case for get_following

    Get following
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/following'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_friends(client):
    """Test case for get_friends

    Get friends
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/friends'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hidden_items(client):
    """Test case for get_hidden_items

    Get hidden items
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/hidden/{section}'.format(section='calendar'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_on_a_personal_list(client):
    """Test case for get_items_on_a_personal_list

    Get items on a personal list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists/{list_id}/items/{type}'.format(id='sean', list_id='star-wars-in-machete-order', type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_likes(client):
    """Test case for get_likes

    Get likes
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/likes/{type}'.format(id='sean', type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pending_following_requests(client):
    """Test case for get_pending_following_requests

    Get pending following requests
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/requests/following',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personal_list(client):
    """Test case for get_personal_list

    Get personal list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists/{list_id}'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_filters(client):
    """Test case for get_saved_filters

    Get saved filters
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/saved_filters/{section}'.format(section='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stats(client):
    """Test case for get_stats

    Get stats
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/stats'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_profile(client):
    """Test case for get_user_profile

    Get user profile
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watching(client):
    """Test case for get_watching

    Get watching
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/watching'.format(id='sean'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_like_a_list(client):
    """Test case for like_a_list

    Like a list
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists/{list_id}/like'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_hidden_items(client):
    """Test case for remove_hidden_items

    Remove hidden items
    """
    body = openapi_server.AddHiddenItemsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/hidden/{section}/remove'.format(section='calendar'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_items_from_personal_list(client):
    """Test case for remove_items_from_personal_list

    Remove items from personal list
    """
    body = openapi_server.RemoveItemsFromPersonalListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists/{list_id}/items/remove'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_like_on_a_list(client):
    """Test case for remove_like_on_a_list

    Remove like on a list
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}/lists/{list_id}/like'.format(id='id_example', list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_a_users_lists(client):
    """Test case for reorder_a_users_lists

    Reorder a user's lists
    """
    body = openapi_server.ReorderAUserSListsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists/reorder'.format(id='sean'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_items_on_a_list(client):
    """Test case for reorder_items_on_a_list

    Reorder items on a list
    """
    body = openapi_server.ReorderPersonallyRecommendedItemsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/lists/{list_id}/items/reorder'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_settings(client):
    """Test case for retrieve_settings

    Retrieve settings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_this_user(client):
    """Test case for unfollow_this_user

    Unfollow this user
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}/follow'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_personal_list(client):
    """Test case for update_personal_list

    Update personal list
    """
    body = openapi_server.UpdatePersonalListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{id}/lists/{list_id}'.format(id='id_example', list_id='list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_collection_type_get(client):
    """Test case for users_id_collection_type_get

    Get collection
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/collection/{type}'.format(id='sean', type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_history_type_item_id_get(client):
    """Test case for users_id_history_type_item_id_get

    Get watched history
    """
    params = [('start_at', '2016-06-01T00:00:00.000Z'),
                    ('end_at', '2016-07-01T23:59:59.000Z')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/history/{type}/{item_id}'.format(id='sean', type='movies', item_id=123),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_lists_list_id_comments_sort_get(client):
    """Test case for users_id_lists_list_id_comments_sort_get

    Get all list comments
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists/{list_id}/comments/{sort}'.format(id='sean', list_id='star-wars-in-machete-order', sort='newest'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_lists_list_id_likes_get(client):
    """Test case for users_id_lists_list_id_likes_get

    Get all users who liked a list
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/lists/{list_id}/likes'.format(id='sean', list_id='star-wars-in-machete-order'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_ratings_type_rating_get(client):
    """Test case for users_id_ratings_type_rating_get

    Get ratings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/ratings/{type}/{rating}'.format(id='sean', type='movies', rating=9),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_recommendations_type_sort_get(client):
    """Test case for users_id_recommendations_type_sort_get

    Get personal recommendations
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/recommendations/{type}/{sort}'.format(id='sean', type='movies', sort='rank'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_watched_type_get(client):
    """Test case for users_id_watched_type_get

    Get watched
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/watched/{type}'.format(id='sean', type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_watchlist_type_sort_get(client):
    """Test case for users_id_watchlist_type_sort_get

    Get watchlist
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/watchlist/{type}/{sort}'.format(id='sean', type='movies', sort='rank'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

