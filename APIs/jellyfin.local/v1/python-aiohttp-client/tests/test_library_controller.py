# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_theme_media_result import AllThemeMediaResult
from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.item_counts import ItemCounts
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.library_options_result_dto import LibraryOptionsResultDto
from openapi_server.models.media_update_info_dto import MediaUpdateInfoDto
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.theme_media_result import ThemeMediaResult


pytestmark = pytest.mark.asyncio

async def test_delete_item(client):
    """Test case for delete_item

    Deletes an item from the library and filesystem.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Items/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_items(client):
    """Test case for delete_items

    Deletes items from the library and filesystem.
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ancestors(client):
    """Test case for get_ancestors

    Gets all parents of an item.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Ancestors'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_critic_reviews(client):
    """Test case for get_critic_reviews

    Gets critic review for an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/CriticReviews'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_download(client):
    """Test case for get_download

    Downloads item media.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Download'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file(client):
    """Test case for get_file

    Get the original file of an item.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/File'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_counts(client):
    """Test case for get_item_counts

    Get item counts.
    """
    params = [('userId', 'user_id_example'),
                    ('isFavorite', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/Counts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_library_options_info(client):
    """Test case for get_library_options_info

    Gets the library options info.
    """
    params = [('libraryContentType', 'library_content_type_example'),
                    ('isNewLibrary', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Libraries/AvailableOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_folders(client):
    """Test case for get_media_folders

    Gets all user media folders.
    """
    params = [('isHidden', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Library/MediaFolders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_physical_paths(client):
    """Test case for get_physical_paths

    Gets a list of physical paths from virtual folders.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Library/PhysicalPaths',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_albums(client):
    """Test case for get_similar_albums

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Albums/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_artists(client):
    """Test case for get_similar_artists

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Artists/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_items(client):
    """Test case for get_similar_items

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_movies(client):
    """Test case for get_similar_movies

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Movies/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_shows(client):
    """Test case for get_similar_shows

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Shows/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_trailers(client):
    """Test case for get_similar_trailers

    Gets similar items.
    """
    params = [('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Trailers/{item_id}/Similar'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_theme_media(client):
    """Test case for get_theme_media

    Get theme songs and videos for an item.
    """
    params = [('userId', 'user_id_example'),
                    ('inheritFromParent', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/ThemeMedia'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_theme_songs(client):
    """Test case for get_theme_songs

    Get theme songs for an item.
    """
    params = [('userId', 'user_id_example'),
                    ('inheritFromParent', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/ThemeSongs'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_theme_videos(client):
    """Test case for get_theme_videos

    Get theme videos for an item.
    """
    params = [('userId', 'user_id_example'),
                    ('inheritFromParent', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/ThemeVideos'.format(item_id='item_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_added_movies(client):
    """Test case for post_added_movies

    Reports that new movies have been added by an external source.
    """
    params = [('tmdbId', 'tmdb_id_example'),
                    ('imdbId', 'imdb_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/Movies/Added',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_added_series(client):
    """Test case for post_added_series

    Reports that new episodes of a series have been added by an external source.
    """
    params = [('tvdbId', 'tvdb_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/Series/Added',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_updated_media(client):
    """Test case for post_updated_media

    Reports that new movies have been added by an external source.
    """
    body = {"Path":"Path","UpdateType":"UpdateType"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/Media/Updated',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_updated_movies(client):
    """Test case for post_updated_movies

    Reports that new movies have been added by an external source.
    """
    params = [('tmdbId', 'tmdb_id_example'),
                    ('imdbId', 'imdb_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/Movies/Updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_updated_series(client):
    """Test case for post_updated_series

    Reports that new episodes of a series have been added by an external source.
    """
    params = [('tvdbId', 'tvdb_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/Series/Updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_library(client):
    """Test case for refresh_library

    Starts a library scan.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Library/Refresh',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

