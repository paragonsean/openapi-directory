# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advanced_search_filter_params import AdvancedSearchFilterParams
from openapi_server.models.album_for_user_for_api_contract import AlbumForUserForApiContract
from openapi_server.models.album_for_user_for_api_contract_partial_find_result import AlbumForUserForApiContractPartialFindResult
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.album_sort_rule import AlbumSortRule
from openapi_server.models.artist_for_user_for_api_contract import ArtistForUserForApiContract
from openapi_server.models.artist_for_user_for_api_contract_partial_find_result import ArtistForUserForApiContractPartialFindResult
from openapi_server.models.artist_optional_fields import ArtistOptionalFields
from openapi_server.models.artist_sort_rule import ArtistSortRule
from openapi_server.models.artist_type import ArtistType
from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.create_report_model import CreateReportModel
from openapi_server.models.disc_type import DiscType
from openapi_server.models.entry_edit_data_contract import EntryEditDataContract
from openapi_server.models.entry_type import EntryType
from openapi_server.models.logical_grouping import LogicalGrouping
from openapi_server.models.media_type import MediaType
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.pv_services import PVServices
from openapi_server.models.purchase_status import PurchaseStatus
from openapi_server.models.purchase_statuses import PurchaseStatuses
from openapi_server.models.rated_song_for_user_for_api_contract_partial_find_result import RatedSongForUserForApiContractPartialFindResult
from openapi_server.models.rated_song_for_user_sort_rule import RatedSongForUserSortRule
from openapi_server.models.release_event_for_api_contract import ReleaseEventForApiContract
from openapi_server.models.song_list_for_api_contract_partial_find_result import SongListForApiContractPartialFindResult
from openapi_server.models.song_list_optional_fields import SongListOptionalFields
from openapi_server.models.song_list_sort_rule import SongListSortRule
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.song_vote_rating import SongVoteRating
from openapi_server.models.user_event_relationship_type import UserEventRelationshipType
from openapi_server.models.user_for_api_contract import UserForApiContract
from openapi_server.models.user_for_api_contract_partial_find_result import UserForApiContractPartialFindResult
from openapi_server.models.user_group_id import UserGroupId
from openapi_server.models.user_inbox_type import UserInboxType
from openapi_server.models.user_message_contract import UserMessageContract
from openapi_server.models.user_message_contract_partial_find_result import UserMessageContractPartialFindResult
from openapi_server.models.user_optional_fields import UserOptionalFields
from openapi_server.models.user_sort_rule import UserSortRule


pytestmark = pytest.mark.asyncio

async def test_api_users_current_album_collection_statuses_album_id_get(client):
    """Test case for api_users_current_album_collection_statuses_album_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/current/album-collection-statuses/{album_id}'.format(album_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_albums_album_id_post(client):
    """Test case for api_users_current_albums_album_id_post

    
    """
    params = [('collectionStatus', openapi_server.PurchaseStatus()),
                    ('mediaType', openapi_server.MediaType()),
                    ('rating', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/current/albums/{album_id}'.format(album_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_followed_artists_artist_id_get(client):
    """Test case for api_users_current_followed_artists_artist_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/current/followedArtists/{artist_id}'.format(artist_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_followed_tags_tag_id_delete(client):
    """Test case for api_users_current_followed_tags_tag_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/current/followedTags/{tag_id}'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_followed_tags_tag_id_post(client):
    """Test case for api_users_current_followed_tags_tag_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/users/current/followedTags/{tag_id}'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_get(client):
    """Test case for api_users_current_get

    
    """
    params = [('fields', openapi_server.UserOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/current',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_rated_songs_song_id_get(client):
    """Test case for api_users_current_rated_songs_song_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/current/ratedSongs/{song_id}'.format(song_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_refresh_entry_edit_post(client):
    """Test case for api_users_current_refresh_entry_edit_post

    
    """
    params = [('entryType', openapi_server.EntryType()),
                    ('entryId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/current/refreshEntryEdit',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_current_song_tags_song_id_post(client):
    """Test case for api_users_current_song_tags_song_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/users/current/songTags/{song_id}'.format(song_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_get(client):
    """Test case for api_users_get

    
    """
    params = [('query', ''),
                    ('groups', openapi_server.UserGroupId()),
                    ('joinDateAfter', '2013-10-20T19:20:30+01:00'),
                    ('joinDateBefore', '2013-10-20T19:20:30+01:00'),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.UserSortRule()),
                    ('includeDisabled', False),
                    ('onlyVerified', False),
                    ('knowsLanguage', 'knows_language_example'),
                    ('fields', openapi_server.UserOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_album_collection_statuses_album_id_get(client):
    """Test case for api_users_id_album_collection_statuses_album_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/album-collection-statuses/{album_id}'.format(id=56, album_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_albums_get(client):
    """Test case for api_users_id_albums_get

    
    """
    params = [('query', ''),
                    ('tagId', 56),
                    ('tag', 'tag_example'),
                    ('artistId', 56),
                    ('purchaseStatuses', openapi_server.PurchaseStatuses()),
                    ('releaseEventId', 0),
                    ('albumTypes', openapi_server.DiscType()),
                    ('advancedFilters', [openapi_server.AdvancedSearchFilterParams()]),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.AlbumSortRule()),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.AlbumOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('mediaType', openapi_server.MediaType())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/albums'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_events_get(client):
    """Test case for api_users_id_events_get

    
    """
    params = [('relationshipType', openapi_server.UserEventRelationshipType())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/events'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_followed_artists_artist_id_get(client):
    """Test case for api_users_id_followed_artists_artist_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/followedArtists/{artist_id}'.format(id=56, artist_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_followed_artists_get(client):
    """Test case for api_users_id_followed_artists_get

    
    """
    params = [('query', ''),
                    ('tagId[]', [56]),
                    ('artistType', openapi_server.ArtistType()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.ArtistSortRule()),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.ArtistOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/followedArtists'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_get(client):
    """Test case for api_users_id_get

    
    """
    params = [('fields', openapi_server.UserOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_messages_delete(client):
    """Test case for api_users_id_messages_delete

    
    """
    params = [('messageId', [56])]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/{id}/messages'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_messages_get(client):
    """Test case for api_users_id_messages_get

    
    """
    params = [('inbox', openapi_server.UserInboxType()),
                    ('unread', False),
                    ('anotherUserId', 56),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/messages'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_users_id_messages_post(client):
    """Test case for api_users_id_messages_post

    
    """
    body = {"highPriority":True,"read":True,"receiver":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"sender":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"subject":"subject","id":0,"body":"body","inbox":"Nothing","createdFormatted":"createdFormatted"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{id}/messages'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_profile_comments_get(client):
    """Test case for api_users_id_profile_comments_get

    
    """
    params = [('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/profileComments'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_users_id_profile_comments_post(client):
    """Test case for api_users_id_profile_comments_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{id}/profileComments'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_rated_songs_get(client):
    """Test case for api_users_id_rated_songs_get

    
    """
    params = [('query', ''),
                    ('tagName', 'tag_name_example'),
                    ('tagId[]', [56]),
                    ('artistId[]', [56]),
                    ('childVoicebanks', False),
                    ('artistGrouping', openapi_server.LogicalGrouping()),
                    ('rating', openapi_server.SongVoteRating()),
                    ('songListId', 56),
                    ('groupByRating', True),
                    ('pvServices', openapi_server.PVServices()),
                    ('advancedFilters', [openapi_server.AdvancedSearchFilterParams()]),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.RatedSongForUserSortRule()),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/ratedSongs'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_rated_songs_song_id_get(client):
    """Test case for api_users_id_rated_songs_song_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/ratedSongs/{song_id}'.format(id=56, song_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_users_id_reports_post(client):
    """Test case for api_users_id_reports_post

    
    """
    body = {"reportType":"MaliciousIP","reason":"reason"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{id}/reports'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_users_id_settings_setting_name_post(client):
    """Test case for api_users_id_settings_setting_name_post

    
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/{id}/settings/{setting_name}'.format(id=56, setting_name='setting_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_id_song_lists_get(client):
    """Test case for api_users_id_song_lists_get

    
    """
    params = [('query', ''),
                    ('tagId[]', [56]),
                    ('childTags', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.SongListSortRule()),
                    ('fields', openapi_server.SongListOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/{id}/songLists'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_messages_message_id_get(client):
    """Test case for api_users_messages_message_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/messages/{message_id}'.format(message_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_names_get(client):
    """Test case for api_users_names_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('maxResults', 10),
                    ('includeDisabled', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_users_profile_comments_comment_id_delete(client):
    """Test case for api_users_profile_comments_comment_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/profileComments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_users_profile_comments_comment_id_post(client):
    """Test case for api_users_profile_comments_comment_id_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/profileComments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

