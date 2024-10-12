# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_data_list import CategoryDataList
from openapi_server.models.collection import Collection
from openapi_server.models.collection_create_request import CollectionCreateRequest
from openapi_server.models.collection_create_response import CollectionCreateResponse
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.collection_item_request import CollectionItemRequest
from openapi_server.models.collection_update_request import CollectionUpdateRequest
from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.featured_collection import FeaturedCollection
from openapi_server.models.featured_collection_data_list import FeaturedCollectionDataList
from openapi_server.models.language import Language
from openapi_server.models.license_video_request import LicenseVideoRequest
from openapi_server.models.license_video_result_data_list import LicenseVideoResultDataList
from openapi_server.models.redownload_video import RedownloadVideo
from openapi_server.models.suggestions import Suggestions
from openapi_server.models.updated_media_data_list import UpdatedMediaDataList
from openapi_server.models.url import Url
from openapi_server.models.video import Video
from openapi_server.models.video_collection_item_data_list import VideoCollectionItemDataList
from openapi_server.models.video_data_list import VideoDataList
from openapi_server.models.video_search_results import VideoSearchResults


pytestmark = pytest.mark.asyncio

async def test_add_video_collection_items(client):
    """Test case for add_video_collection_items

    Add videos to collections
    """
    body = {"items":[{"added_time":"2020-05-29T12:10:22-05:00","id":"1690105108","media_type":"image"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/videos/collections/{id}/items'.format(id='17555176'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_video_collection(client):
    """Test case for create_video_collection

    Create video collections
    """
    body = {"name":"Test Collection 19cf"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/videos/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_collection(client):
    """Test case for delete_video_collection

    Delete video collections
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/videos/collections/{id}'.format(id='17555176'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_collection_items(client):
    """Test case for delete_video_collection_items

    Remove videos from collections
    """
    params = [('item_id', ['item_id_example'])]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/videos/collections/{id}/items'.format(id='17555176'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_videos(client):
    """Test case for download_videos

    Download videos
    """
    body = {"size":"web"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/videos/licenses/{id}/downloads'.format(id='e123'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_similar_videos(client):
    """Test case for find_similar_videos

    List similar videos
    """
    params = [('language', openapi_server.Language()),
                    ('page', 1),
                    ('per_page', 20),
                    ('view', minimal)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/{id}/similar'.format(id='2140697'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_video_collection(client):
    """Test case for get_featured_video_collection

    Get the details of featured video collections
    """
    params = [('embed', 'embed_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections/featured/{id}'.format(id='136351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_video_collection_items(client):
    """Test case for get_featured_video_collection_items

    Get the contents of featured video collections
    """
    params = [('page', 1),
                    ('per_page', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections/featured/{id}/items'.format(id='136351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_video_collection_list(client):
    """Test case for get_featured_video_collection_list

    List featured video collections
    """
    params = [('embed', 'share_url')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections/featured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_updated_videos(client):
    """Test case for get_updated_videos

    List updated videos
    """
    params = [('start_date', '2020-05-29'),
                    ('end_date', '2021-05-29'),
                    ('interval', '1 HOUR'),
                    ('page', 1),
                    ('per_page', 100),
                    ('sort', newest)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video(client):
    """Test case for get_video

    Get details about videos
    """
    params = [('language', openapi_server.Language()),
                    ('view', full),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/{id}'.format(id='639703'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_collection(client):
    """Test case for get_video_collection

    Get the details of video collections
    """
    params = [('embed', ['embed_example']),
                    ('share_code', 'share_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections/{id}'.format(id='17555176'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_collection_items(client):
    """Test case for get_video_collection_items

    Get the contents of video collections
    """
    params = [('page', 1),
                    ('per_page', 100),
                    ('share_code', 'share_code_example'),
                    ('sort', oldest)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections/{id}/items'.format(id='17555176'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_collection_list(client):
    """Test case for get_video_collection_list

    List video collections
    """
    params = [('page', 1),
                    ('per_page', 100),
                    ('embed', ['share_code'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_license_list(client):
    """Test case for get_video_license_list

    List video licenses
    """
    params = [('video_id', '12345678'),
                    ('license', 'standard'),
                    ('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('username', 'aUniqueUsername'),
                    ('start_date', '2021-03-29T13:25:13.521Z'),
                    ('end_date', '2021-03-29T13:25:13.521Z'),
                    ('download_availability', all),
                    ('team_history', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_list(client):
    """Test case for get_video_list

    List videos
    """
    params = [('id', ['[\"639703\",\"993721\"]']),
                    ('view', minimal),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_suggestions(client):
    """Test case for get_video_suggestions

    Get suggestions for a search term
    """
    params = [('query', 'cats'),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/search/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_videos(client):
    """Test case for license_videos

    License videos
    """
    body = {"videos":[{"size":"hd","subscription_id":"s12345678","video_id":"2140697"}]}
    params = [('subscription_id', 's12345678'),
                    ('size', web),
                    ('search_id', 'search_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/videos/licenses',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_video_categories(client):
    """Test case for list_video_categories

    List video categories
    """
    params = [('language', openapi_server.Language())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_video_collection(client):
    """Test case for rename_video_collection

    Rename video collections
    """
    body = {"name":"My collection with a new name"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/videos/collections/{id}'.format(id='17555176'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_videos(client):
    """Test case for search_videos

    Search for videos
    """
    params = [('added_date', '2020-05-29'),
                    ('added_date_start', '2020-05-29'),
                    ('added_date_end', '2020-05-29'),
                    ('aspect_ratio', '43'),
                    ('category', 'category_example'),
                    ('contributor', ['[12345678]']),
                    ('contributor_country', ['US']),
                    ('duration', 56),
                    ('duration_from', 60),
                    ('duration_to', 180),
                    ('fps', 3.4),
                    ('fps_from', 24),
                    ('fps_to', 60),
                    ('keyword_safe_search', True),
                    ('language', openapi_server.Language()),
                    ('license', ['[\"commercial\",\"editorial\"]']),
                    ('model', ['[\"442583\",\"434750\"]']),
                    ('page', 1),
                    ('per_page', 20),
                    ('people_age', '20s'),
                    ('people_ethnicity', ['hispanic']),
                    ('people_gender', 'female'),
                    ('people_number', 2),
                    ('people_model_released', true),
                    ('query', 'dogs running on the beach'),
                    ('resolution', '4k'),
                    ('safe', True),
                    ('sort', popular),
                    ('view', minimal)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/videos/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

