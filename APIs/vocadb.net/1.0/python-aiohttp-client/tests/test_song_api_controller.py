# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.artist_album_participation_status import ArtistAlbumParticipationStatus
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.lyrics_for_song_contract import LyricsForSongContract
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.pv_service import PVService
from openapi_server.models.pv_services import PVServices
from openapi_server.models.rated_song_for_user_for_api_contract import RatedSongForUserForApiContract
from openapi_server.models.related_songs_contract import RelatedSongsContract
from openapi_server.models.song_for_api_contract import SongForApiContract
from openapi_server.models.song_for_api_contract_partial_find_result import SongForApiContractPartialFindResult
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.song_rating_contract import SongRatingContract
from openapi_server.models.song_sort_rule import SongSortRule
from openapi_server.models.song_vocalist_selection import SongVocalistSelection
from openapi_server.models.top_songs_date_filter_type import TopSongsDateFilterType
from openapi_server.models.user_optional_fields import UserOptionalFields


pytestmark = pytest.mark.asyncio

async def test_api_songs_by_pv_get(client):
    """Test case for api_songs_by_pv_get

    
    """
    params = [('pvService', openapi_server.PVService()),
                    ('pvId', 'pv_id_example'),
                    ('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/byPv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_comments_comment_id_delete(client):
    """Test case for api_songs_comments_comment_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/songs/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_songs_comments_comment_id_post(client):
    """Test case for api_songs_comments_comment_id_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/songs/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_get(client):
    """Test case for api_songs_get

    
    """
    params = [('query', ''),
                    ('songTypes', 'song_types_example'),
                    ('afterDate', '2013-10-20T19:20:30+01:00'),
                    ('beforeDate', '2013-10-20T19:20:30+01:00'),
                    ('tagName[]', ['tag_name_example']),
                    ('tagId[]', [56]),
                    ('childTags', False),
                    ('unifyTypesAndTags', False),
                    ('artistId[]', [56]),
                    ('artistParticipationStatus', openapi_server.ArtistAlbumParticipationStatus()),
                    ('childVoicebanks', False),
                    ('includeMembers', False),
                    ('onlyWithPvs', False),
                    ('pvServices', openapi_server.PVServices()),
                    ('since', 56),
                    ('minScore', 56),
                    ('userCollectionId', 56),
                    ('releaseEventId', 56),
                    ('parentSongId', 56),
                    ('status', openapi_server.EntryStatus()),
                    ('advancedFilters', [openapi_server.AdvancedSearchFilterParams()]),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.SongSortRule()),
                    ('preferAccurateMatches', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('minMilliBpm', 56),
                    ('maxMilliBpm', 56),
                    ('minLength', 56),
                    ('maxLength', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_highlighted_get(client):
    """Test case for api_songs_highlighted_get

    
    """
    params = [('languagePreference', openapi_server.ContentLanguagePreference()),
                    ('fields', openapi_server.SongOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/highlighted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_comments_get(client):
    """Test case for api_songs_id_comments_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_songs_id_comments_post(client):
    """Test case for api_songs_id_comments_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/songs/{id}/comments'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_delete(client):
    """Test case for api_songs_id_delete

    
    """
    params = [('notes', '')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/songs/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_derived_get(client):
    """Test case for api_songs_id_derived_get

    
    """
    params = [('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/{id}/derived'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_get(client):
    """Test case for api_songs_id_get

    
    """
    params = [('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_ratings_get(client):
    """Test case for api_songs_id_ratings_get

    
    """
    params = [('userFields', openapi_server.UserOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/{id}/ratings'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_songs_id_ratings_post(client):
    """Test case for api_songs_id_ratings_post

    
    """
    body = {"rating":"Nothing"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/songs/{id}/ratings'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_id_related_get(client):
    """Test case for api_songs_id_related_get

    
    """
    params = [('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/{id}/related'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_lyrics_lyrics_id_get(client):
    """Test case for api_songs_lyrics_lyrics_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/lyrics/{lyrics_id}'.format(lyrics_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_names_get(client):
    """Test case for api_songs_names_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('maxResults', 15)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_songs_top_rated_get(client):
    """Test case for api_songs_top_rated_get

    
    """
    params = [('durationHours', 56),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('filterBy', openapi_server.TopSongsDateFilterType()),
                    ('vocalist', openapi_server.SongVocalistSelection()),
                    ('maxResults', 25),
                    ('fields', openapi_server.SongOptionalFields()),
                    ('languagePreference', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/songs/top-rated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

