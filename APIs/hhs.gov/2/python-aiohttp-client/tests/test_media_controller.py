# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_item import MediaItem
from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.resources_media_id_youtube_meta_data_json_get200_response import ResourcesMediaIdYoutubeMetaDataJsonGet200Response
from openapi_server.models.syndicate_marshaller_wrapped import SyndicateMarshallerWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_media_featured_json_get(client):
    """Test case for resources_media_featured_json_get

    Get the list of featured content in the syndication system
    """
    params = [('sort', 'sort_example'),
                    ('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/featured.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_content_get(client):
    """Test case for resources_media_id_content_get

    Get content for MediaItem
    """
    params = [('calledByBuild', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/content'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_embed_json_get(client):
    """Test case for resources_media_id_embed_json_get

    Get embed code for MediaItem
    """
    params = [('flavor', 'flavor_example'),
                    ('width', 56),
                    ('height', 56),
                    ('iframeName', 'iframe_name_example'),
                    ('excludeJquery', False),
                    ('excludeDiv', False),
                    ('divId', 'div_id_example'),
                    ('displayMethod', 'display_method_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/embed.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_json_get(client):
    """Test case for resources_media_id_json_get

    Get MediaItem by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_preview_jpg_get(client):
    """Test case for resources_media_id_preview_jpg_get

    Get Tag by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/preview.jpg'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_related_media_format_get(client):
    """Test case for resources_media_id_related_media_format_get

    Get related MediaItems by ID
    """
    params = [('max', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/relatedMedia.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_syndicate_format_get(client):
    """Test case for resources_media_id_syndicate_format_get

    Get syndicated content for MediaItem
    """
    params = [('cssClass', 'syndicate'),
                    ('stripStyles', False),
                    ('stripScripts', False),
                    ('stripImages', False),
                    ('stripBreaks', False),
                    ('stripClasses', False),
                    ('font-size', 56),
                    ('imageFloat', 'image_float_example'),
                    ('imageMargin', 'image_margin_example'),
                    ('autoplay', True),
                    ('rel', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/syndicate.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_thumbnail_jpg_get(client):
    """Test case for resources_media_id_thumbnail_jpg_get

    Get JPG thumbnail for MediaItem
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/thumbnail.jpg'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_id_youtube_meta_data_json_get(client):
    """Test case for resources_media_id_youtube_meta_data_json_get

    Get Youtube metadata for MediaItem
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/{id}/youtubeMetaData.json'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_json_get(client):
    """Test case for resources_media_json_get

    Get MediaItems
    """
    params = [('max', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('order', 'order_example'),
                    ('mediaTypes', 'media_types_example'),
                    ('name', 'name_example'),
                    ('collectionId', 56),
                    ('nameContains', 'name_contains_example'),
                    ('descriptionContains', 'description_contains_example'),
                    ('sourceUrl', 'source_url_example'),
                    ('sourceUrlContains', 'source_url_contains_example'),
                    ('customThumbnailUrl', 'custom_thumbnail_url_example'),
                    ('customThumbnailUrlContains', 'custom_thumbnail_url_contains_example'),
                    ('dateContentAuthored', '2013-10-20'),
                    ('dateContentUpdated', '2013-10-20'),
                    ('dateContentPublished', '2013-10-20'),
                    ('dateContentReviewed', '2013-10-20'),
                    ('dateSyndicationCaptured', '2013-10-20'),
                    ('dateSyndicationUpdated', '2013-10-20'),
                    ('contentAuthoredSinceDate', '2013-10-20'),
                    ('contentAuthoredBeforeDate', '2013-10-20'),
                    ('contentAuthoredInRange', 'content_authored_in_range_example'),
                    ('contentUpdatedSinceDate', '2013-10-20'),
                    ('contentUpdatedBeforeDate', '2013-10-20'),
                    ('contentUpdatedInRange', 'content_updated_in_range_example'),
                    ('contentPublishedSinceDate', '2013-10-20'),
                    ('contentPublishedBeforeDate', '2013-10-20'),
                    ('contentPublishedInRange', 'content_published_in_range_example'),
                    ('contentReviewedSinceDate', '2013-10-20'),
                    ('contentReviewedBeforeDate', '2013-10-20'),
                    ('contentReviewedInRange', 'content_reviewed_in_range_example'),
                    ('syndicationCapturedSinceDate', '2013-10-20'),
                    ('syndicationCapturedBeforeDate', '2013-10-20'),
                    ('syndicationCapturedInRange', 'syndication_captured_in_range_example'),
                    ('syndicationUpdatedSinceDate', '2013-10-20'),
                    ('syndicationUpdatedBeforeDate', '2013-10-20'),
                    ('syndicationUpdatedInRange', 'syndication_updated_in_range_example'),
                    ('syndicationVisibleSinceDate', '2013-10-20'),
                    ('syndicationVisibleBeforeDate', '2013-10-20'),
                    ('syndicationVisibleInRange', '2013-10-20'),
                    ('languageId', 56),
                    ('languageName', 'language_name_example'),
                    ('languageIsoCode', 'language_iso_code_example'),
                    ('hash', 'hash_example'),
                    ('hashContains', 'hash_contains_example'),
                    ('sourceId', 56),
                    ('sourceName', 'source_name_example'),
                    ('sourceNameContains', 'source_name_contains_example'),
                    ('sourceAcronym', 'source_acronym_example'),
                    ('sourceAcronymContains', 'source_acronym_contains_example'),
                    ('tagIds', 'tag_ids_example'),
                    ('restrictToSet', 'restrict_to_set_example'),
                    ('createdBy', 'created_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_most_popular_media_format_get(client):
    """Test case for resources_media_most_popular_media_format_get

    Get MediaItems by popularity
    """
    params = [('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/mostPopularMedia.{format}'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_media_search_results_json_get(client):
    """Test case for resources_media_search_results_json_get

    Get MediaItems by search query
    """
    params = [('q', 'q_example'),
                    ('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/media/searchResults.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

