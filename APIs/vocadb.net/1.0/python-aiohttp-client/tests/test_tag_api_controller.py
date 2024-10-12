# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.comment_for_api_contract_partial_find_result import CommentForApiContractPartialFindResult
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_type import EntryType
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.tag_base_contract import TagBaseContract
from openapi_server.models.tag_for_api_contract import TagForApiContract
from openapi_server.models.tag_for_api_contract_partial_find_result import TagForApiContractPartialFindResult
from openapi_server.models.tag_optional_fields import TagOptionalFields
from openapi_server.models.tag_report_type import TagReportType
from openapi_server.models.tag_sort_rule import TagSortRule
from openapi_server.models.tag_target_types import TagTargetTypes


pytestmark = pytest.mark.asyncio

async def test_api_tags_by_name_name_get(client):
    """Test case for api_tags_by_name_name_get

    
    """
    params = [('fields', openapi_server.TagOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/byName/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_category_names_get(client):
    """Test case for api_tags_category_names_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/categoryNames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_comments_comment_id_delete(client):
    """Test case for api_tags_comments_comment_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/tags/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_tags_comments_comment_id_post(client):
    """Test case for api_tags_comments_comment_id_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/tags/comments/{comment_id}'.format(comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_get(client):
    """Test case for api_tags_get

    
    """
    params = [('query', ''),
                    ('allowChildren', True),
                    ('categoryName', ''),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('sort', openapi_server.TagSortRule()),
                    ('preferAccurateMatches', False),
                    ('fields', openapi_server.TagOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('target', openapi_server.TagTargetTypes())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_id_delete(client):
    """Test case for api_tags_id_delete

    
    """
    params = [('notes', ''),
                    ('hardDelete', False)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/tags/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_id_get(client):
    """Test case for api_tags_id_get

    
    """
    params = [('fields', openapi_server.TagOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_names_get(client):
    """Test case for api_tags_names_get

    
    """
    params = [('query', ''),
                    ('allowAliases', True),
                    ('maxResults', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_post(client):
    """Test case for api_tags_post

    
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_tag_id_children_get(client):
    """Test case for api_tags_tag_id_children_get

    
    """
    params = [('fields', openapi_server.TagOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/{tag_id}/children'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_tag_id_comments_get(client):
    """Test case for api_tags_tag_id_comments_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/{tag_id}/comments'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_tags_tag_id_comments_post(client):
    """Test case for api_tags_tag_id_comments_post

    
    """
    body = {"entry":{"eventCategory":"Unspecified","description":"description","mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"artistString":"artistString","activityDate":"2000-01-23T04:56:07.000+00:00","discType":"Unknown","webLinks":[{"description":"description","disabled":True,"category":"Official","url":"url"},{"description":"description","disabled":True,"category":"Official","url":"url"}],"id":5,"defaultName":"defaultName","additionalNames":"additionalNames","createDate":"2000-01-23T04:56:07.000+00:00","urlSlug":"urlSlug","entryType":"Undefined","defaultNameLanguage":"Unspecified","songListFeaturedCategory":"Nothing","artistType":"Unknown","pvs":[{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"},{"pvType":"Original","author":"author","length":7,"publishDate":"2000-01-23T04:56:07.000+00:00","url":"url","createdBy":5,"pvId":"pvId","service":"NicoNicoDouga","extendedMetadata":{"json":"json"},"name":"name","disabled":True,"id":2,"thumbUrl":"thumbUrl"}],"songType":"Unspecified","version":2,"tags":[{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}},{"count":9,"tag":{"urlSlug":"urlSlug","name":"name","id":3,"categoryName":"categoryName","additionalNames":"additionalNames"}}],"names":[{"value":"value"},{"value":"value"}],"releaseEventSeriesName":"releaseEventSeriesName","name":"name","tagCategoryName":"tagCategoryName"},"author":{"memberSince":"2000-01-23T04:56:07.000+00:00","groupId":"Nothing","name":"name","verifiedArtist":True,"active":True,"mainPicture":{"urlOriginal":"urlOriginal","urlSmallThumb":"urlSmallThumb","mime":"mime","name":"name","urlThumb":"urlThumb","urlTinyThumb":"urlTinyThumb"},"id":0,"oldUsernames":[{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"},{"date":"2000-01-23T04:56:07.000+00:00","oldName":"oldName"}],"knownLanguages":[{"cultureCode":"cultureCode","proficiency":"Nothing"},{"cultureCode":"cultureCode","proficiency":"Nothing"}]},"authorName":"authorName","created":"2000-01-23T04:56:07.000+00:00","id":0,"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/api/tags/{tag_id}/comments'.format(tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_tag_id_reports_post(client):
    """Test case for api_tags_tag_id_reports_post

    
    """
    params = [('reportType', openapi_server.TagReportType()),
                    ('notes', 'notes_example'),
                    ('versionNumber', 56)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/tags/{tag_id}/reports'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_tags_top_get(client):
    """Test case for api_tags_top_get

    
    """
    params = [('categoryName', 'category_name_example'),
                    ('entryType', openapi_server.EntryType()),
                    ('maxResults', 15),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/tags/top',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

