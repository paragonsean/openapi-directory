# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.echo200_response import Echo200Response
from openapi_server.models.get_album_by_id200_response import GetAlbumByID200Response
from openapi_server.models.get_albums_by_person_id200_response import GetAlbumsByPersonID200Response
from openapi_server.models.get_favorites_by_person_id200_response import GetFavoritesByPersonID200Response
from openapi_server.models.get_favorites_context_by_id200_response import GetFavoritesContextByID200Response
from openapi_server.models.get_gallery_photos_by_id200_response import GetGalleryPhotosByID200Response
from openapi_server.models.get_group_by_id200_response import GetGroupByID200Response
from openapi_server.models.get_group_discussions_by_id200_response import GetGroupDiscussionsByID200Response
from openapi_server.models.get_group_topic_by_id200_response import GetGroupTopicByID200Response
from openapi_server.models.get_group_topic_replies_by_id200_response import GetGroupTopicRepliesByID200Response
from openapi_server.models.get_license_by_id200_response import GetLicenseByID200Response
from openapi_server.models.get_person_by_id200_response import GetPersonByID200Response
from openapi_server.models.get_photo_by_id200_response import GetPhotoByID200Response
from openapi_server.models.get_photo_exif_by_id200_response import GetPhotoExifByID200Response
from openapi_server.models.get_photo_sizes_by_id200_response import GetPhotoSizesByID200Response


pytestmark = pytest.mark.asyncio

async def test_echo(client):
    """Test case for echo

    
    """
    params = [('api_key', 'api_key_example'),
                    ('echo', 'echo_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.test.echo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_token(client):
    """Test case for get_access_token

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_token', 'oauth_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/oauth/access_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_by_id(client):
    """Test case for get_album_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photoset_id', 'photoset_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photosets.getPhotos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_context_by_id(client):
    """Test case for get_album_context_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example'),
                    ('photoset_id', 'photoset_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photosets.getContext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_albums_by_person_id(client):
    """Test case for get_albums_by_person_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('user_id', 'user_id_example'),
                    ('page', 3.4),
                    ('per_page', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photosets.getList',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_favorites_by_person_id(client):
    """Test case for get_favorites_by_person_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('user_id', 'user_id_example'),
                    ('min_fave_date', 3.4),
                    ('max_fave_date', 3.4),
                    ('page', 3.4),
                    ('per_page', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.favorites.getList',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_favorites_context_by_id(client):
    """Test case for get_favorites_context_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example'),
                    ('user_id', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.favorites.getContext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gallery_photos_by_id(client):
    """Test case for get_gallery_photos_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('gallery_id', 'gallery_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.galleries.getPhotos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_by_id(client):
    """Test case for get_group_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('group_id', 'group_id_example'),
                    ('group_path_alias', 'group_path_alias_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_discussions_by_id(client):
    """Test case for get_group_discussions_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('group_id', 'group_id_example'),
                    ('page', 3.4),
                    ('per_page', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.discuss.topics.getList',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_photos_by_id(client):
    """Test case for get_group_photos_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('group_id', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.pools.getPhotos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_topic_by_id(client):
    """Test case for get_group_topic_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('group_id', 'group_id_example'),
                    ('topic_id', 'topic_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.discuss.topics.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_topic_replies_by_id(client):
    """Test case for get_group_topic_replies_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('group_id', 'group_id_example'),
                    ('topic_id', 'topic_id_example'),
                    ('reply_id', 'reply_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.discuss.replies.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_license_by_id(client):
    """Test case for get_license_by_id

    
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.licenses.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_by_person_id(client):
    """Test case for get_media_by_person_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('user_id', 'user_id_example'),
                    ('safe_search', 3.4),
                    ('min_upload_date', 3.4),
                    ('max_upload_date', 3.4),
                    ('min_taken_date', 3.4),
                    ('max_taken_date', 3.4),
                    ('content_type', 3.4),
                    ('privacy_filter', 3.4),
                    ('page', 3.4),
                    ('per_page', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.people.getPhotos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_by_search(client):
    """Test case for get_media_by_search

    
    """
    params = [('api_key', 'api_key_example'),
                    ('text', 'text_example'),
                    ('tags', 'tags_example'),
                    ('user_id', 'user_id_example'),
                    ('min_upload_date', 'min_upload_date_example'),
                    ('max_upload_date', 'max_upload_date_example'),
                    ('min_taken_date', 'min_taken_date_example'),
                    ('max_taken_date', 'max_taken_date_example'),
                    ('license', 'license_example'),
                    ('sort', 'sort_example'),
                    ('privacy_filter', 3.4),
                    ('bbox', 'bbox_example'),
                    ('accuracy', 'accuracy_example'),
                    ('safe_search', 3.4),
                    ('content_type', 3.4),
                    ('machine_tags', 'machine_tags_example'),
                    ('machine_tag_mode', 'machine_tag_mode_example'),
                    ('group_id', 'group_id_example'),
                    ('contacts', 'contacts_example'),
                    ('woe_id', 'woe_id_example'),
                    ('place_id', 'place_id_example'),
                    ('media', 'media_example'),
                    ('has_geo', 'has_geo_example'),
                    ('geo_context', 'geo_context_example'),
                    ('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('radius', 3.4),
                    ('radius_units', 'radius_units_example'),
                    ('is_commons', True),
                    ('in_gallery', True),
                    ('is_getty', True),
                    ('per_page', 3.4),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_person_by_id(client):
    """Test case for get_person_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('user_id', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.people.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_photo_by_id(client):
    """Test case for get_photo_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.getInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_photo_exif_by_id(client):
    """Test case for get_photo_exif_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example'),
                    ('secret', 'secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.getExif',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_photo_sizes_by_id(client):
    """Test case for get_photo_sizes_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.getSizes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_photolist_context_by_id(client):
    """Test case for get_photolist_context_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example'),
                    ('photolist_id', 'photolist_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photolist.getContext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_photostream_context_by_id(client):
    """Test case for get_photostream_context_by_id

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.photos.getContext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_request_token(client):
    """Test case for get_request_token

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_callback', 'oauth_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/oauth/request_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restmethodflickr_groups_pools_get_context_get(client):
    """Test case for restmethodflickr_groups_pools_get_context_get

    
    """
    params = [('api_key', 'api_key_example'),
                    ('photo_id', 'photo_id_example'),
                    ('group_id', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services/rest?method=flickr.groups.pools.getContext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_photo(client):
    """Test case for upload_photo

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_key', 'api_key_example')
    data.add_field('content_type', 'content_type_example')
    data.add_field('description', 'description_example')
    data.add_field('hidden', 'hidden_example')
    data.add_field('is_family', 'is_family_example')
    data.add_field('is_friend', 'is_friend_example')
    data.add_field('is_public', 'is_public_example')
    data.add_field('photo', '/path/to/file')
    data.add_field('safety_level', 'safety_level_example')
    data.add_field('tags', 'tags_example')
    data.add_field('title', 'title_example')
    response = await client.request(
        method='POST',
        path='/services/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

