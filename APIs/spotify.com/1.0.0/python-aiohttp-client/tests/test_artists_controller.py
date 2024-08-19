# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artist_object import ArtistObject
from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.get_an_artists_top_tracks200_response import GetAnArtistsTopTracks200Response
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_artists200_response import GetMultipleArtists200Response
from openapi_server.models.paging_simplified_album_object import PagingSimplifiedAlbumObject
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest


pytestmark = pytest.mark.asyncio

async def test_check_current_user_follows_0(client):
    """Test case for check_current_user_follows_0

    Check If User Follows Artists or Users 
    """
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/following/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_follow_artists_users_0(client):
    """Test case for follow_artists_users_0

    Follow Artists or Users 
    """
    body = openapi_server.FollowArtistsUsersRequest()
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/following',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_artist(client):
    """Test case for get_an_artist

    Get Artist 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_artists_albums(client):
    """Test case for get_an_artists_albums

    Get Artist's Albums 
    """
    params = [('include_groups', 'single,appears_on'),
                    ('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}/albums'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_artists_related_artists(client):
    """Test case for get_an_artists_related_artists

    Get Artist's Related Artists 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}/related-artists'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_artists_top_tracks(client):
    """Test case for get_an_artists_top_tracks

    Get Artist's Top Tracks 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}/top-tracks'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_followed_1(client):
    """Test case for get_followed_1

    Get Followed Artists 
    """
    params = [('type', 'artist'),
                    ('after', '0I2XqVXqHScXjHhk6AYYRe'),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/following',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_artists(client):
    """Test case for get_multiple_artists

    Get Several Artists 
    """
    params = [('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_artists_users_0(client):
    """Test case for unfollow_artists_users_0

    Unfollow Artists or Users 
    """
    body = openapi_server.UnfollowArtistsUsersRequest()
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/following',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

