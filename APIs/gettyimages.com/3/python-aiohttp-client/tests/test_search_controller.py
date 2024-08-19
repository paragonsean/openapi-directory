# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.age_of_people_filter_type import AgeOfPeopleFilterType
from openapi_server.models.blended_image_sort_order import BlendedImageSortOrder
from openapi_server.models.collections_filter_type import CollectionsFilterType
from openapi_server.models.compositions_filter_type import CompositionsFilterType
from openapi_server.models.create_image_search_facets_fields import CreateImageSearchFacetsFields
from openapi_server.models.create_video_search_facets_fields import CreateVideoSearchFacetsFields
from openapi_server.models.creative_image_search_results import CreativeImageSearchResults
from openapi_server.models.creative_image_sort_order import CreativeImageSortOrder
from openapi_server.models.creative_images_field_values import CreativeImagesFieldValues
from openapi_server.models.creative_video_search_results import CreativeVideoSearchResults
from openapi_server.models.creative_video_sort_order import CreativeVideoSortOrder
from openapi_server.models.creative_videos_field_values import CreativeVideosFieldValues
from openapi_server.models.editorial_graphical_style import EditorialGraphicalStyle
from openapi_server.models.editorial_image_search_facets_fields import EditorialImageSearchFacetsFields
from openapi_server.models.editorial_image_search_results import EditorialImageSearchResults
from openapi_server.models.editorial_images_field_values import EditorialImagesFieldValues
from openapi_server.models.editorial_segment_contract import EditorialSegmentContract
from openapi_server.models.editorial_video_search_facets_fields import EditorialVideoSearchFacetsFields
from openapi_server.models.editorial_video_search_results import EditorialVideoSearchResults
from openapi_server.models.editorial_video_type import EditorialVideoType
from openapi_server.models.editorial_videos_field_values import EditorialVideosFieldValues
from openapi_server.models.ethnicity_filter_type import EthnicityFilterType
from openapi_server.models.event_field_values import EventFieldValues
from openapi_server.models.event_search_sort_order import EventSearchSortOrder
from openapi_server.models.events_search_result import EventsSearchResult
from openapi_server.models.graphical_style import GraphicalStyle
from openapi_server.models.graphical_styles_filter_type import GraphicalStylesFilterType
from openapi_server.models.image_orientation_request import ImageOrientationRequest
from openapi_server.models.image_search_item_search_results import ImageSearchItemSearchResults
from openapi_server.models.image_techniques_filter_type import ImageTechniquesFilterType
from openapi_server.models.images_field_values import ImagesFieldValues
from openapi_server.models.license_model_video_request import LicenseModelVideoRequest
from openapi_server.models.number_of_people_filter_type import NumberOfPeopleFilterType
from openapi_server.models.release_status import ReleaseStatus
from openapi_server.models.search_by_image_resource_results import SearchByImageResourceResults
from openapi_server.models.search_file_type import SearchFileType
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.tee_shirt_size import TeeShirtSize
from openapi_server.models.video_aspect_ratio_filter_type import VideoAspectRatioFilterType
from openapi_server.models.video_formats_request import VideoFormatsRequest
from openapi_server.models.video_frame_rates import VideoFrameRates
from openapi_server.models.video_orientation_request import VideoOrientationRequest
from openapi_server.models.viewpoints_filter_type import ViewpointsFilterType


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v3_search_by_image_uploads_file_name_put(client):
    """Test case for v3_search_by_image_uploads_file_name_put

    Upload image for use by the search creative images/videos operations
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'image/jpeg',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/search/by-image/uploads/{file_name}'.format(file_name='file_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_events_get(client):
    """Test case for v3_search_events_get

    Search for events
    """
    params = [('editorial_segment', openapi_server.EditorialSegmentContract()),
                    ('date_from', '2013-10-20T19:20:30+01:00'),
                    ('date_to', '2013-10-20T19:20:30+01:00'),
                    ('fields', [openapi_server.EventFieldValues()]),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', ''),
                    ('sort_order', openapi_server.EventSearchSortOrder())]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_images_creative_by_image_get(client):
    """Test case for v3_search_images_creative_by_image_get

    Search for creative images based on url
    """
    params = [('asset_id', 'asset_id_example'),
                    ('exclude_editorial_use_only', True),
                    ('facet_fields', [openapi_server.CreateImageSearchFacetsFields()]),
                    ('facet_max_count', 300),
                    ('fields', [openapi_server.CreativeImagesFieldValues()]),
                    ('image_url', 'image_url_example'),
                    ('include_facets', True),
                    ('page', 1),
                    ('page_size', 30),
                    ('product_types', ['product_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/images/creative/by-image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_images_creative_get(client):
    """Test case for v3_search_images_creative_get

    Search for creative images only
    """
    params = [('age_of_people', [openapi_server.AgeOfPeopleFilterType()]),
                    ('artists', 'artists_example'),
                    ('collection_codes', ['collection_codes_example']),
                    ('collections_filter_type', openapi_server.CollectionsFilterType()),
                    ('color', 'color_example'),
                    ('compositions', [openapi_server.CompositionsFilterType()]),
                    ('download_product', 'download_product_example'),
                    ('embed_content_only', False),
                    ('ethnicity', [openapi_server.EthnicityFilterType()]),
                    ('exclude_keyword_ids', [56]),
                    ('exclude_nudity', False),
                    ('exclude_editorial_use_only', True),
                    ('fields', [openapi_server.CreativeImagesFieldValues()]),
                    ('file_types', [openapi_server.SearchFileType()]),
                    ('graphical_styles', [openapi_server.GraphicalStyle()]),
                    ('graphical_styles_filter_type', openapi_server.GraphicalStylesFilterType()),
                    ('include_related_searches', False),
                    ('keyword_ids', [56]),
                    ('minimum_size', openapi_server.TeeShirtSize()),
                    ('number_of_people', [openapi_server.NumberOfPeopleFilterType()]),
                    ('orientations', [openapi_server.ImageOrientationRequest()]),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', ''),
                    ('safe_search', False),
                    ('sort_order', openapi_server.CreativeImageSortOrder()),
                    ('facet_fields', [openapi_server.CreateImageSearchFacetsFields()]),
                    ('include_facets', True),
                    ('facet_max_count', 300)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/images/creative',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_images_editorial_get(client):
    """Test case for v3_search_images_editorial_get

    Search for editorial images only
    """
    params = [('age_of_people', [openapi_server.AgeOfPeopleFilterType()]),
                    ('artists', 'artists_example'),
                    ('collection_codes', ['collection_codes_example']),
                    ('collections_filter_type', openapi_server.CollectionsFilterType()),
                    ('compositions', [openapi_server.CompositionsFilterType()]),
                    ('date_from', '2013-10-20T19:20:30+01:00'),
                    ('date_to', '2013-10-20T19:20:30+01:00'),
                    ('download_product', 'download_product_example'),
                    ('editorial_segments', [openapi_server.EditorialSegmentContract()]),
                    ('embed_content_only', False),
                    ('ethnicity', [openapi_server.EthnicityFilterType()]),
                    ('event_ids', [56]),
                    ('exclude_keyword_ids', [56]),
                    ('fields', [openapi_server.EditorialImagesFieldValues()]),
                    ('file_types', [openapi_server.SearchFileType()]),
                    ('graphical_styles', [openapi_server.EditorialGraphicalStyle()]),
                    ('graphical_styles_filter_type', openapi_server.GraphicalStylesFilterType()),
                    ('include_related_searches', False),
                    ('keyword_ids', [56]),
                    ('minimum_size', openapi_server.TeeShirtSize()),
                    ('number_of_people', [openapi_server.NumberOfPeopleFilterType()]),
                    ('orientations', [openapi_server.ImageOrientationRequest()]),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', 'phrase_example'),
                    ('sort_order', openapi_server.SortOrder()),
                    ('specific_people', ['specific_people_example']),
                    ('minimum_quality_rank', 56),
                    ('facet_fields', [openapi_server.EditorialImageSearchFacetsFields()]),
                    ('include_facets', True),
                    ('facet_max_count', 300)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/images/editorial',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_images_get(client):
    """Test case for v3_search_images_get

    Search for both creative and editorial images - *** DEPRECATED ***
    """
    params = [('age_of_people', [openapi_server.AgeOfPeopleFilterType()]),
                    ('artists', 'artists_example'),
                    ('collection_codes', ['collection_codes_example']),
                    ('collections_filter_type', openapi_server.CollectionsFilterType()),
                    ('color', 'color_example'),
                    ('compositions', [openapi_server.CompositionsFilterType()]),
                    ('download_product', 'download_product_example'),
                    ('embed_content_only', False),
                    ('event_ids', [56]),
                    ('ethnicity', [openapi_server.EthnicityFilterType()]),
                    ('exclude_nudity', False),
                    ('fields', [openapi_server.ImagesFieldValues()]),
                    ('file_types', [openapi_server.SearchFileType()]),
                    ('graphical_styles', [openapi_server.GraphicalStyle()]),
                    ('graphical_styles_filter_type', openapi_server.GraphicalStylesFilterType()),
                    ('include_related_searches', False),
                    ('keyword_ids', [56]),
                    ('minimum_size', openapi_server.TeeShirtSize()),
                    ('number_of_people', [openapi_server.NumberOfPeopleFilterType()]),
                    ('orientations', [openapi_server.ImageOrientationRequest()]),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', 'phrase_example'),
                    ('sort_order', openapi_server.BlendedImageSortOrder()),
                    ('specific_people', ['specific_people_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_videos_creative_by_image_get(client):
    """Test case for v3_search_videos_creative_by_image_get

    Search for creative videos based on url
    """
    params = [('asset_id', 'asset_id_example'),
                    ('exclude_editorial_use_only', True),
                    ('facet_fields', [openapi_server.CreateVideoSearchFacetsFields()]),
                    ('facet_max_count', 300),
                    ('fields', [openapi_server.CreativeVideosFieldValues()]),
                    ('image_url', 'image_url_example'),
                    ('include_facets', True),
                    ('page', 1),
                    ('page_size', 30),
                    ('product_types', ['product_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/videos/creative/by-image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_videos_creative_get(client):
    """Test case for v3_search_videos_creative_get

    Search for creative videos
    """
    params = [('age_of_people', [openapi_server.AgeOfPeopleFilterType()]),
                    ('artists', 'artists_example'),
                    ('aspect_ratios', [openapi_server.VideoAspectRatioFilterType()]),
                    ('collection_codes', ['collection_codes_example']),
                    ('collections_filter_type', openapi_server.CollectionsFilterType()),
                    ('compositions', [openapi_server.CompositionsFilterType()]),
                    ('download_product', 'download_product_example'),
                    ('exclude_nudity', False),
                    ('exclude_editorial_use_only', True),
                    ('exclude_keyword_ids', [56]),
                    ('fields', [openapi_server.CreativeVideosFieldValues()]),
                    ('format_available', openapi_server.VideoFormatsRequest()),
                    ('frame_rates', [openapi_server.VideoFrameRates()]),
                    ('image_techniques', [openapi_server.ImageTechniquesFilterType()]),
                    ('include_related_searches', False),
                    ('keyword_ids', [56]),
                    ('license_models', [openapi_server.LicenseModelVideoRequest()]),
                    ('orientations', [openapi_server.VideoOrientationRequest()]),
                    ('min_clip_length', 0),
                    ('max_clip_length', 0),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', ''),
                    ('safe_search', False),
                    ('sort_order', openapi_server.CreativeVideoSortOrder()),
                    ('release_status', openapi_server.ReleaseStatus()),
                    ('facet_fields', [openapi_server.CreateVideoSearchFacetsFields()]),
                    ('facet_max_count', 300),
                    ('include_facets', True),
                    ('viewpoints', [openapi_server.ViewpointsFilterType()])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/videos/creative',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_search_videos_editorial_get(client):
    """Test case for v3_search_videos_editorial_get

    Search for editorial videos
    """
    params = [('age_of_people', [openapi_server.AgeOfPeopleFilterType()]),
                    ('artists', 'artists_example'),
                    ('aspect_ratios', [openapi_server.VideoAspectRatioFilterType()]),
                    ('collection_codes', ['collection_codes_example']),
                    ('collections_filter_type', openapi_server.CollectionsFilterType()),
                    ('compositions', [openapi_server.CompositionsFilterType()]),
                    ('date_from', '2013-10-20T19:20:30+01:00'),
                    ('date_to', '2013-10-20T19:20:30+01:00'),
                    ('download_product', 'download_product_example'),
                    ('editorial_video_types', [openapi_server.EditorialVideoType()]),
                    ('fields', [openapi_server.EditorialVideosFieldValues()]),
                    ('format_available', openapi_server.VideoFormatsRequest()),
                    ('frame_rates', [openapi_server.VideoFrameRates()]),
                    ('image_techniques', [openapi_server.ImageTechniquesFilterType()]),
                    ('include_related_searches', False),
                    ('keyword_ids', [56]),
                    ('min_clip_length', 0),
                    ('max_clip_length', 0),
                    ('orientations', [openapi_server.VideoOrientationRequest()]),
                    ('page', 1),
                    ('page_size', 30),
                    ('phrase', ''),
                    ('sort_order', openapi_server.SortOrder()),
                    ('specific_people', ['specific_people_example']),
                    ('release_status', openapi_server.ReleaseStatus()),
                    ('facet_fields', [openapi_server.EditorialVideoSearchFacetsFields()]),
                    ('include_facets', True),
                    ('facet_max_count', 300),
                    ('viewpoints', [openapi_server.ViewpointsFilterType()])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'gi_country_code': 'gi_country_code_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/videos/editorial',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

