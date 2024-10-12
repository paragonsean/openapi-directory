# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.discussion_folder_contract import DiscussionFolderContract
from openapi_server.models.discussion_folder_optional_fields import DiscussionFolderOptionalFields
from openapi_server.models.discussion_topic_contract import DiscussionTopicContract
from openapi_server.models.discussion_topic_contract_partial_find_result import DiscussionTopicContractPartialFindResult
from openapi_server.models.discussion_topic_optional_fields import DiscussionTopicOptionalFields
from openapi_server.models.discussion_topic_sort_rule import DiscussionTopicSortRule


pytestmark = pytest.mark.asyncio

async def test_api_discussions_comments_comment_id_delete(client):
    """Test case for api_discussions_comments_comment_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/discussions/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_discussions_comments_comment_id_post(client):
    """Test case for api_discussions_comments_comment_id_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/discussions/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_discussions_folders_folder_id_topics_get(client):
    """Test case for api_discussions_folders_folder_id_topics_get

    
    """
    params = [('fields', openapi_server.DiscussionTopicOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/discussions/folders/{folder_id}/topics'.format(folder_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_discussions_folders_folder_id_topics_post(client):
    """Test case for api_discussions_folders_folder_id_topics_post

    
    """
    body = {"comments":[{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"},{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}],"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"created":"2000-01-23T04:56:07.000+00:00","name":"name","lastComment":{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"},"id":1,"locked":True,"content":"content","folderId":6,"commentCount":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/discussions/folders/{folder_id}/topics'.format(folder_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_discussions_folders_get(client):
    """Test case for api_discussions_folders_get

    
    """
    params = [('fields', openapi_server.DiscussionFolderOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/discussions/folders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_discussions_folders_post(client):
    """Test case for api_discussions_folders_post

    
    """
    body = {"name":"name","description":"description","topicCount":6,"lastTopicAuthor":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"id":0,"lastTopicDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/discussions/folders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_discussions_topics_get(client):
    """Test case for api_discussions_topics_get

    
    """
    params = [('folderId', 56),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.DiscussionTopicSortRule()),
                    ('fields', openapi_server.DiscussionTopicOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/discussions/topics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_discussions_topics_topic_id_comments_post(client):
    """Test case for api_discussions_topics_topic_id_comments_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/discussions/topics/{topic_id}/comments'.format(topic_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_discussions_topics_topic_id_delete(client):
    """Test case for api_discussions_topics_topic_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/discussions/topics/{topic_id}'.format(topic_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_discussions_topics_topic_id_get(client):
    """Test case for api_discussions_topics_topic_id_get

    
    """
    params = [('fields', openapi_server.DiscussionTopicOptionalFields())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/discussions/topics/{topic_id}'.format(topic_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_discussions_topics_topic_id_post(client):
    """Test case for api_discussions_topics_topic_id_post

    
    """
    body = {"comments":[{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"},{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}],"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"created":"2000-01-23T04:56:07.000+00:00","name":"name","lastComment":{"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"},"id":1,"locked":True,"content":"content","folderId":6,"commentCount":0}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/discussions/topics/{topic_id}'.format(topic_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

