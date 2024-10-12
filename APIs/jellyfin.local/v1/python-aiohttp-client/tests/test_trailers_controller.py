# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.item_filter import ItemFilter
from openapi_server.models.location_type import LocationType
from openapi_server.models.series_status import SeriesStatus
from openapi_server.models.video_type import VideoType


pytestmark = pytest.mark.asyncio

async def test_get_trailers(client):
    """Test case for get_trailers

    Finds movies and trailers similar to a given trailer.
    """
    params = [('userId', 'user_id_example'),
                    ('maxOfficialRating', 'max_official_rating_example'),
                    ('hasThemeSong', True),
                    ('hasThemeVideo', True),
                    ('hasSubtitles', True),
                    ('hasSpecialFeature', True),
                    ('hasTrailer', True),
                    ('adjacentTo', 'adjacent_to_example'),
                    ('parentIndexNumber', 56),
                    ('hasParentalRating', True),
                    ('isHd', True),
                    ('is4K', True),
                    ('locationTypes', [openapi_server.LocationType()]),
                    ('excludeLocationTypes', [openapi_server.LocationType()]),
                    ('isMissing', True),
                    ('isUnaired', True),
                    ('minCommunityRating', 3.4),
                    ('minCriticRating', 3.4),
                    ('minPremiereDate', '2013-10-20T19:20:30+01:00'),
                    ('minDateLastSaved', '2013-10-20T19:20:30+01:00'),
                    ('minDateLastSavedForUser', '2013-10-20T19:20:30+01:00'),
                    ('maxPremiereDate', '2013-10-20T19:20:30+01:00'),
                    ('hasOverview', True),
                    ('hasImdbId', True),
                    ('hasTmdbId', True),
                    ('hasTvdbId', True),
                    ('excludeItemIds', ['exclude_item_ids_example']),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('recursive', True),
                    ('searchTerm', 'search_term_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('parentId', 'parent_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('excludeItemTypes', ['exclude_item_types_example']),
                    ('filters', [openapi_server.ItemFilter()]),
                    ('isFavorite', True),
                    ('mediaTypes', ['media_types_example']),
                    ('imageTypes', [openapi_server.ImageType()]),
                    ('sortBy', 'sort_by_example'),
                    ('isPlayed', True),
                    ('genres', ['genres_example']),
                    ('officialRatings', ['official_ratings_example']),
                    ('tags', ['tags_example']),
                    ('years', [56]),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('person', 'person_example'),
                    ('personIds', ['person_ids_example']),
                    ('personTypes', ['person_types_example']),
                    ('studios', ['studios_example']),
                    ('artists', ['artists_example']),
                    ('excludeArtistIds', ['exclude_artist_ids_example']),
                    ('artistIds', ['artist_ids_example']),
                    ('albumArtistIds', ['album_artist_ids_example']),
                    ('contributingArtistIds', ['contributing_artist_ids_example']),
                    ('albums', ['albums_example']),
                    ('albumIds', ['album_ids_example']),
                    ('ids', ['ids_example']),
                    ('videoTypes', [openapi_server.VideoType()]),
                    ('minOfficialRating', 'min_official_rating_example'),
                    ('isLocked', True),
                    ('isPlaceHolder', True),
                    ('hasOfficialRating', True),
                    ('collapseBoxSetItems', True),
                    ('minWidth', 56),
                    ('minHeight', 56),
                    ('maxWidth', 56),
                    ('maxHeight', 56),
                    ('is3D', True),
                    ('seriesStatus', [openapi_server.SeriesStatus()]),
                    ('nameStartsWithOrGreater', 'name_starts_with_or_greater_example'),
                    ('nameStartsWith', 'name_starts_with_example'),
                    ('nameLessThan', 'name_less_than_example'),
                    ('studioIds', ['studio_ids_example']),
                    ('genreIds', ['genre_ids_example']),
                    ('enableTotalRecordCount', True),
                    ('enableImages', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Trailers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

