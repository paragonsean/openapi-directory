# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_items_to_collection_request import AddItemsToCollectionRequest
from openapi_server.models.add_items_to_personal_recommendations_request import AddItemsToPersonalRecommendationsRequest
from openapi_server.models.add_items_to_watched_history_request import AddItemsToWatchedHistoryRequest
from openapi_server.models.add_items_to_watchlist_request import AddItemsToWatchlistRequest
from openapi_server.models.add_new_ratings_request import AddNewRatingsRequest
from openapi_server.models.remove_items_from_collection_request import RemoveItemsFromCollectionRequest
from openapi_server.models.remove_items_from_history_request import RemoveItemsFromHistoryRequest
from openapi_server.models.remove_items_from_personal_recommendations_request import RemoveItemsFromPersonalRecommendationsRequest
from openapi_server.models.reorder_personally_recommended_items_request import ReorderPersonallyRecommendedItemsRequest


pytestmark = pytest.mark.asyncio

async def test_add_items_to_collection(client):
    """Test case for add_items_to_collection

    Add items to collection
    """
    body = openapi_server.AddItemsToCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/collection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_items_to_personal_recommendations(client):
    """Test case for add_items_to_personal_recommendations

    Add items to personal recommendations
    """
    body = openapi_server.AddItemsToPersonalRecommendationsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/recommendations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_items_to_watched_history(client):
    """Test case for add_items_to_watched_history

    Add items to watched history
    """
    body = openapi_server.AddItemsToWatchedHistoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/history',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_items_to_watchlist(client):
    """Test case for add_items_to_watchlist

    Add items to watchlist
    """
    body = openapi_server.AddItemsToWatchlistRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/watchlist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_new_ratings(client):
    """Test case for add_new_ratings

    Add new ratings
    """
    body = openapi_server.AddNewRatingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/ratings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection(client):
    """Test case for get_collection

    Get collection
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/collection/{type}'.format(type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_activity(client):
    """Test case for get_last_activity

    Get last activity
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/last_activities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personal_recommendations(client):
    """Test case for get_personal_recommendations

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
        path='/sync/recommendations/{type}/{sort}'.format(type='movies', sort='rank'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playback_progress(client):
    """Test case for get_playback_progress

    Get playback progress
    """
    params = [('start_at', '2016-06-01T00:00:00.000Z'),
                    ('end_at', '2016-07-01T23:59:59.000Z')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/playback/{type}'.format(type='movies'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ratings(client):
    """Test case for get_ratings

    Get ratings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/ratings/{type}/{rating}'.format(type='movies', rating=9),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watched(client):
    """Test case for get_watched

    Get watched
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/watched/{type}'.format(type='movies'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watched_history(client):
    """Test case for get_watched_history

    Get watched history
    """
    params = [('start_at', '2016-06-01T00:00:00.000Z'),
                    ('end_at', '2016-07-01T23:59:59.000Z')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/history/{type}/{id}'.format(type='movies', id=123),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watchlist(client):
    """Test case for get_watchlist

    Get watchlist
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sync/watchlist/{type}/{sort}'.format(type='movies', sort='rank'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_a_playback_item(client):
    """Test case for remove_a_playback_item

    Remove a playback item
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sync/playback/{id}'.format(id=13),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_items_from_collection(client):
    """Test case for remove_items_from_collection

    Remove items from collection
    """
    body = openapi_server.RemoveItemsFromCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/collection/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_items_from_history(client):
    """Test case for remove_items_from_history

    Remove items from history
    """
    body = openapi_server.RemoveItemsFromHistoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/history/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_items_from_personal_recommendations(client):
    """Test case for remove_items_from_personal_recommendations

    Remove items from personal recommendations
    """
    body = openapi_server.RemoveItemsFromPersonalRecommendationsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/recommendations/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_items_from_watchlist(client):
    """Test case for remove_items_from_watchlist

    Remove items from watchlist
    """
    body = openapi_server.RemoveItemsFromCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/watchlist/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_ratings(client):
    """Test case for remove_ratings

    Remove ratings
    """
    body = openapi_server.RemoveItemsFromCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sync/ratings/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_personally_recommended_items(client):
    """Test case for reorder_personally_recommended_items

    Reorder personally recommended items
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
        path='/sync/recommendations/reorder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_watchlist_items(client):
    """Test case for reorder_watchlist_items

    Reorder watchlist items
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
        path='/sync/watchlist/reorder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

