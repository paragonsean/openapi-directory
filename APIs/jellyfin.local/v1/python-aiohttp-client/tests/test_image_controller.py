# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.image_format import ImageFormat
from openapi_server.models.image_info import ImageInfo
from openapi_server.models.image_type import ImageType
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_delete_item_image(client):
    """Test case for delete_item_image

    Delete an item's image.
    """
    params = [('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Items/{item_id}/Images/{image_type}'.format(item_id='item_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item_image_by_index(client):
    """Test case for delete_item_image_by_index

    Delete an item's image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Items/{item_id}/Images/{image_type}/{image_index}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_image(client):
    """Test case for delete_user_image

    Delete the user's image.
    """
    params = [('index', 56)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Users/{user_id}/Images/{image_type}'.format(user_id='user_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_image_by_index(client):
    """Test case for delete_user_image_by_index

    Delete the user's image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Users/{user_id}/Images/{image_type}/{index}'.format(user_id='user_id_example', image_type=openapi_server.ImageType(), index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_artist_image(client):
    """Test case for get_artist_image

    Get artist image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Artists/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genre_image(client):
    """Test case for get_genre_image

    Get genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Genres/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genre_image_by_index(client):
    """Test case for get_genre_image_by_index

    Get genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Genres/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_image(client):
    """Test case for get_item_image

    Gets the item's image.
    """
    params = [('maxWidth', 56),
                    ('maxHeight', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('tag', 'tag_example'),
                    ('cropWhitespace', True),
                    ('format', openapi_server.ImageFormat()),
                    ('addPlayedIndicator', True),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Images/{image_type}'.format(item_id='item_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_image2(client):
    """Test case for get_item_image2

    Gets the item's image.
    """
    params = [('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Images/{image_type}/{image_index}/{tag}/{format}/{max_width}/{max_height}/{percent_played}/{unplayed_count}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), max_width=56, max_height=56, tag='tag_example', format=openapi_server.ImageFormat(), percent_played=3.4, unplayed_count=56, image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_image_by_index(client):
    """Test case for get_item_image_by_index

    Gets the item's image.
    """
    params = [('maxWidth', 56),
                    ('maxHeight', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('tag', 'tag_example'),
                    ('cropWhitespace', True),
                    ('format', openapi_server.ImageFormat()),
                    ('addPlayedIndicator', True),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Images/{image_type}/{image_index}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_image_infos(client):
    """Test case for get_item_image_infos

    Get item image infos.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/Images'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_genre_image(client):
    """Test case for get_music_genre_image

    Get music genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_genre_image_by_index(client):
    """Test case for get_music_genre_image_by_index

    Get music genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_person_image(client):
    """Test case for get_person_image

    Get person image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Persons/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_person_image_by_index(client):
    """Test case for get_person_image_by_index

    Get person image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Persons/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_studio_image(client):
    """Test case for get_studio_image

    Get studio image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Studios/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_studio_image_by_index(client):
    """Test case for get_studio_image_by_index

    Get studio image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Studios/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_image(client):
    """Test case for get_user_image

    Get user profile image.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Images/{image_type}'.format(user_id='user_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_image_by_index(client):
    """Test case for get_user_image_by_index

    Get user profile image.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}/Images/{image_type}/{image_index}'.format(user_id='user_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_artist_image(client):
    """Test case for head_artist_image

    Get artist image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Artists/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_genre_image(client):
    """Test case for head_genre_image

    Get genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Genres/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_genre_image_by_index(client):
    """Test case for head_genre_image_by_index

    Get genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Genres/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_item_image(client):
    """Test case for head_item_image

    Gets the item's image.
    """
    params = [('maxWidth', 56),
                    ('maxHeight', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('tag', 'tag_example'),
                    ('cropWhitespace', True),
                    ('format', openapi_server.ImageFormat()),
                    ('addPlayedIndicator', True),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Items/{item_id}/Images/{image_type}'.format(item_id='item_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_item_image2(client):
    """Test case for head_item_image2

    Gets the item's image.
    """
    params = [('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Items/{item_id}/Images/{image_type}/{image_index}/{tag}/{format}/{max_width}/{max_height}/{percent_played}/{unplayed_count}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), max_width=56, max_height=56, tag='tag_example', format=openapi_server.ImageFormat(), percent_played=3.4, unplayed_count=56, image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_item_image_by_index(client):
    """Test case for head_item_image_by_index

    Gets the item's image.
    """
    params = [('maxWidth', 56),
                    ('maxHeight', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('tag', 'tag_example'),
                    ('cropWhitespace', True),
                    ('format', openapi_server.ImageFormat()),
                    ('addPlayedIndicator', True),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Items/{item_id}/Images/{image_type}/{image_index}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_music_genre_image(client):
    """Test case for head_music_genre_image

    Get music genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/MusicGenres/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_music_genre_image_by_index(client):
    """Test case for head_music_genre_image_by_index

    Get music genre image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/MusicGenres/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_person_image(client):
    """Test case for head_person_image

    Get person image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Persons/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_person_image_by_index(client):
    """Test case for head_person_image_by_index

    Get person image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Persons/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_studio_image(client):
    """Test case for head_studio_image

    Get studio image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Studios/{name}/Images/{image_type}'.format(name='name_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_studio_image_by_index(client):
    """Test case for head_studio_image_by_index

    Get studio image by name.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Studios/{name}/Images/{image_type}/{image_index}'.format(name='name_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_user_image(client):
    """Test case for head_user_image

    Get user profile image.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example'),
                    ('imageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Users/{user_id}/Images/{image_type}'.format(user_id='user_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_user_image_by_index(client):
    """Test case for head_user_image_by_index

    Get user profile image.
    """
    params = [('tag', 'tag_example'),
                    ('format', openapi_server.ImageFormat()),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('percentPlayed', 3.4),
                    ('unplayedCount', 56),
                    ('width', 56),
                    ('height', 56),
                    ('quality', 56),
                    ('cropWhitespace', True),
                    ('addPlayedIndicator', True),
                    ('blur', 56),
                    ('backgroundColor', 'background_color_example'),
                    ('foregroundLayer', 'foreground_layer_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/Users/{user_id}/Images/{image_type}/{image_index}'.format(user_id='user_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_user_image(client):
    """Test case for post_user_image

    Sets the user image.
    """
    params = [('index', 56)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Images/{image_type}'.format(user_id='user_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_user_image_by_index(client):
    """Test case for post_user_image_by_index

    Sets the user image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Images/{image_type}/{index}'.format(user_id='user_id_example', image_type=openapi_server.ImageType(), index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_item_image(client):
    """Test case for set_item_image

    Set item image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/Images/{image_type}'.format(item_id='item_id_example', image_type=openapi_server.ImageType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_item_image_by_index(client):
    """Test case for set_item_image_by_index

    Set item image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/Images/{image_type}/{image_index}'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item_image_index(client):
    """Test case for update_item_image_index

    Updates the index for an item image.
    """
    params = [('newIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/{item_id}/Images/{image_type}/{image_index}/Index'.format(item_id='item_id_example', image_type=openapi_server.ImageType(), image_index=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

