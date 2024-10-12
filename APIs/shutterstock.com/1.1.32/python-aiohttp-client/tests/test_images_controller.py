# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_image_search_results import BulkImageSearchResults
from openapi_server.models.bulk_search_images_contributor_country_parameter import BulkSearchImagesContributorCountryParameter
from openapi_server.models.bulk_search_images_region_parameter import BulkSearchImagesRegionParameter
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
from openapi_server.models.image import Image
from openapi_server.models.image_data_list import ImageDataList
from openapi_server.models.image_search_results import ImageSearchResults
from openapi_server.models.language import Language
from openapi_server.models.license_image_request import LicenseImageRequest
from openapi_server.models.license_image_result_data_list import LicenseImageResultDataList
from openapi_server.models.recommendation_data_list import RecommendationDataList
from openapi_server.models.redownload_image import RedownloadImage
from openapi_server.models.search_entities_request import SearchEntitiesRequest
from openapi_server.models.search_entities_response import SearchEntitiesResponse
from openapi_server.models.search_image import SearchImage
from openapi_server.models.suggestions import Suggestions
from openapi_server.models.updated_media_data_list import UpdatedMediaDataList
from openapi_server.models.url import Url


pytestmark = pytest.mark.asyncio

async def test_add_image_collection_items(client):
    """Test case for add_image_collection_items

    Add images to collections
    """
    body = {"items":[{"added_time":"2020-05-29T12:10:22-05:00","id":"1690105108","media_type":"image"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/collections/{id}/items'.format(id='126351027'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_search_images(client):
    """Test case for bulk_search_images

    Run multiple image searches
    """
    body = {"license":["editorial"],"query":"cat","sort":"popular"}
    params = [('added_date', '2021-03-29'),
                    ('added_date_start', '2021-03-29'),
                    ('aspect_ratio_min', 1.7778),
                    ('aspect_ratio_max', 1.7778),
                    ('aspect_ratio', 1.7778),
                    ('added_date_end', '2021-03-29'),
                    ('category', 'category_example'),
                    ('color', '4F21EA'),
                    ('contributor', ['[\"123456\"]']),
                    ('contributor_country', openapi_server.BulkSearchImagesContributorCountryParameter()),
                    ('fields', 'fields_example'),
                    ('height', 56),
                    ('height_from', 1080),
                    ('height_to', 1080),
                    ('image_type', ['photo']),
                    ('keyword_safe_search', True),
                    ('language', openapi_server.Language()),
                    ('license', ['license_example']),
                    ('model', ['[\"12345\",\"67890\"]']),
                    ('orientation', 'vertical'),
                    ('page', 1),
                    ('per_page', 20),
                    ('people_model_released', true),
                    ('people_age', '20s'),
                    ('people_ethnicity', ['hispanic']),
                    ('people_gender', 'both'),
                    ('people_number', 2),
                    ('region', openapi_server.BulkSearchImagesRegionParameter()),
                    ('safe', True),
                    ('sort', popular),
                    ('spellcheck_query', True),
                    ('view', minimal),
                    ('width', 56),
                    ('width_from', 1920),
                    ('width_to', 1920)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/bulk_search/images',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_image_collection(client):
    """Test case for create_image_collection

    Create image collections
    """
    body = {"name":"Test Collection 19cf"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_collection(client):
    """Test case for delete_image_collection

    Delete image collections
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/images/collections/{id}'.format(id='136351027'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_collection_items(client):
    """Test case for delete_image_collection_items

    Remove images from collections
    """
    params = [('item_id', ['item_id_example'])]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/images/collections/{id}/items'.format(id='126351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_image(client):
    """Test case for download_image

    Download images
    """
    body = {"size":"small"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/licenses/{id}/downloads'.format(id='e123'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_image_collection(client):
    """Test case for get_featured_image_collection

    Get the details of featured image collections
    """
    params = [('embed', 'embed_example'),
                    ('asset_hint', 1x)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/collections/featured/{id}'.format(id='136351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_image_collection_items(client):
    """Test case for get_featured_image_collection_items

    Get the contents of featured image collections
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
        path='/v2/images/collections/featured/{id}/items'.format(id='136351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_image_collection_list(client):
    """Test case for get_featured_image_collection_list

    List featured image collections
    """
    params = [('embed', 'share_url'),
                    ('type', ['[\"photo\"]']),
                    ('asset_hint', 1x)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/collections/featured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image(client):
    """Test case for get_image

    Get details about images
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
        path='/v2/images/{id}'.format(id='465011609'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_collection(client):
    """Test case for get_image_collection

    Get the details of image collections
    """
    params = [('embed', ['embed_example']),
                    ('share_code', 'share_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/collections/{id}'.format(id='126351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_collection_items(client):
    """Test case for get_image_collection_items

    Get the contents of image collections
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
        path='/v2/images/collections/{id}/items'.format(id='126351027'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_collection_list(client):
    """Test case for get_image_collection_list

    List image collections
    """
    params = [('embed', ['share_code']),
                    ('page', 1),
                    ('per_page', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_keyword_suggestions(client):
    """Test case for get_image_keyword_suggestions

    Get keywords from text
    """
    body = {"text":"Planting flowers is a great way to make springtime more beautiful."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/search/suggestions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_license_list(client):
    """Test case for get_image_license_list

    List image licenses
    """
    params = [('image_id', '12345678'),
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
        path='/v2/images/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_list(client):
    """Test case for get_image_list

    List images
    """
    params = [('id', ['[\"1110335168\",\"465011609\"]']),
                    ('view', minimal),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_recommendations(client):
    """Test case for get_image_recommendations

    List recommended images
    """
    params = [('id', ['[465011609]']),
                    ('max_items', 20),
                    ('safe', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_suggestions(client):
    """Test case for get_image_suggestions

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
        path='/v2/images/search/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_updated_images(client):
    """Test case for get_updated_images

    List updated images
    """
    params = [('type', ['addition']),
                    ('start_date', '2021-03-29'),
                    ('end_date', '2021-03-29'),
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
        path='/v2/images/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_images(client):
    """Test case for license_images

    License images
    """
    body = {"images":[{"editorial_acknowledgement":True,"format":"jpg","image_id":"123456789","metadata":{"customer_id":"12345","geo_location":"US","number_viewed":"15","search_term":"dog"},"price":12.34,"show_modal":True,"size":"small","subscription_id":"s12345678"}]}
    params = [('subscription_id', 'subscription_id_example'),
                    ('format', 'format_example'),
                    ('size', huge),
                    ('search_id', 'search_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/licenses',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_image_categories(client):
    """Test case for list_image_categories

    List image categories
    """
    params = [('language', openapi_server.Language())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_similar_images(client):
    """Test case for list_similar_images

    List similar images
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
        path='/v2/images/{id}/similar'.format(id='465011609'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_image_collection(client):
    """Test case for rename_image_collection

    Rename image collections
    """
    body = {"name":"My collection with a new name"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/images/collections/{id}'.format(id='126351027'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_images(client):
    """Test case for search_images

    Search for images
    """
    params = [('added_date', '2021-03-29'),
                    ('added_date_start', '2021-03-29'),
                    ('aspect_ratio_min', 1.7778),
                    ('aspect_ratio_max', 1.7778),
                    ('aspect_ratio', 1.7778),
                    ('ai_search', True),
                    ('ai_labels_limit', 20),
                    ('ai_industry', 'ai_industry_example'),
                    ('ai_objective', 'ai_objective_example'),
                    ('added_date_end', '2021-03-29'),
                    ('category', 'category_example'),
                    ('color', '4F21EA'),
                    ('contributor', ['[\"123456\"]']),
                    ('contributor_country', openapi_server.BulkSearchImagesContributorCountryParameter()),
                    ('fields', 'fields_example'),
                    ('height', 56),
                    ('height_from', 1080),
                    ('height_to', 1080),
                    ('image_type', ['photo']),
                    ('keyword_safe_search', True),
                    ('language', openapi_server.Language()),
                    ('license', ['license_example']),
                    ('model', ['[\"12345\",\"67890\"]']),
                    ('orientation', 'vertical'),
                    ('page', 1),
                    ('per_page', 20),
                    ('people_model_released', true),
                    ('people_age', '20s'),
                    ('people_ethnicity', ['hispanic']),
                    ('people_gender', 'both'),
                    ('people_number', 2),
                    ('query', 'dogs on the beach'),
                    ('region', openapi_server.BulkSearchImagesRegionParameter()),
                    ('safe', True),
                    ('sort', popular),
                    ('spellcheck_query', True),
                    ('view', minimal),
                    ('width', 56),
                    ('width_from', 1920),
                    ('width_to', 1920)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/images/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

