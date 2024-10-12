# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.album_for_api_contract import AlbumForApiContract
from openapi_server.models.album_for_api_contract_partial_find_result import AlbumForApiContractPartialFindResult
from openapi_server.models.album_for_user_for_api_contract import AlbumForUserForApiContract
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.album_review_contract import AlbumReviewContract
from openapi_server.models.album_sort_rule import AlbumSortRule
from openapi_server.models.artist_album_participation_status import ArtistAlbumParticipationStatus
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.disc_type import DiscType
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.song_in_album_for_api_contract import SongInAlbumForApiContract
from openapi_server.models.song_optional_fields import SongOptionalFields


pytestmark = pytest.mark.asyncio

async def test_api_albums_comments_comment_id_delete(client):
    """Test case for api_albums_comments_comment_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/albums/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_albums_comments_comment_id_post(client):
    """Test case for api_albums_comments_comment_id_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/albums/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_get(client):
    """Test case for api_albums_get

    
    """
    params = [('query', ''),
                    ('discTypes', openapi_server.DiscType()),
                    ('tagName[]', ['tag_name_example']),
                    ('tagId[]', [56]),
                    ('childTags', False),
                    ('artistId[]', [56]),
                    ('artistParticipationStatus', openapi_server.ArtistAlbumParticipationStatus()),
                    ('childVoicebanks', False),
                    ('includeMembers', False),
                    ('barcode', 'barcode_example'),
                    ('status', openapi_server.EntryStatus()),
                    ('releaseDateAfter', '2013-10-20T19:20:30+01:00'),
                    ('releaseDateBefore', '2013-10-20T19:20:30+01:00'),
                    ('advancedFilters', [openapi_server.AdvancedSearchFilterParams()]),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.AlbumSortRule()),
                    ('preferAccurateMatches', False),
                    ('deleted', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.AlbumOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_comments_get(client):
    """Test case for api_albums_id_comments_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_albums_id_comments_post(client):
    """Test case for api_albums_id_comments_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/albums/{id}/comments'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_delete(client):
    """Test case for api_albums_id_delete

    
    """
    params = [('notes', '')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/albums/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_get(client):
    """Test case for api_albums_id_get

    
    """
    params = [('fields', openapi_server.AlbumOptionalFields()),
                    ('songFields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_reviews_get(client):
    """Test case for api_albums_id_reviews_get

    
    """
    params = [('languageCode', 'language_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}/reviews'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_albums_id_reviews_post(client):
    """Test case for api_albums_id_reviews_post

    
    """
    body = {"date":"2000-01-23T04:56:07.000+00:00","albumId":0,"id":6,"text":"text","languageCode":"languageCode","title":"title","user":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/albums/{id}/reviews'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_reviews_review_id_delete(client):
    """Test case for api_albums_id_reviews_review_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/albums/{id}/reviews/{review_id}'.format(review_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_tracks_fields_get(client):
    """Test case for api_albums_id_tracks_fields_get

    
    """
    params = [('field[]', ['_field_example']),
                    ('discNumber', 56),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}/tracks/fields'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_tracks_get(client):
    """Test case for api_albums_id_tracks_get

    
    """
    params = [('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}/tracks'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_id_user_collections_get(client):
    """Test case for api_albums_id_user_collections_get

    
    """
    params = [('languagePreference', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/{id}/user-collections'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_names_get(client):
    """Test case for api_albums_names_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('maxResults', 15)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_new_get(client):
    """Test case for api_albums_new_get

    
    """
    params = [('languagePreference', openapi_server.ContentLanguagePreference()),
                    ('fields', openapi_server.AlbumOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/new',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_albums_top_get(client):
    """Test case for api_albums_top_get

    
    """
    params = [('ignoreIds[]', [56]),
                    ('languagePreference', openapi_server.ContentLanguagePreference()),
                    ('fields', openapi_server.AlbumOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/albums/top',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

