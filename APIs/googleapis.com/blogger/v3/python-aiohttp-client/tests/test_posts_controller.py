# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post import Post
from openapi_server.models.post_list import PostList


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_delete(client):
    """Test case for blogger_posts_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('useTrash', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/blogs/{blog_id}/posts/{post_id}'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_get(client):
    """Test case for blogger_posts_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fetchBody', True),
                    ('fetchImages', True),
                    ('maxComments', 56),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/blogs/{blog_id}/posts/{post_id}'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_get_by_path(client):
    """Test case for blogger_posts_get_by_path

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('path', 'path_example'),
                    ('maxComments', 56),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/blogs/{blog_id}/posts/bypath'.format(blog_id='blog_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_insert(client):
    """Test case for blogger_posts_insert

    
    """
    body = {"images":[{"url":"url"},{"url":"url"}],"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","customMetaData":"customMetaData","published":"published","blog":{"id":"id"},"title":"title","content":"content","url":"url","labels":["labels","labels"],"selfLink":"selfLink","replies":{"totalItems":"totalItems","items":[{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"},{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"}],"selfLink":"selfLink"},"readerComments":"ALLOW","etag":"etag","location":{"lng":1.4658129805029452,"name":"name","lat":6.027456183070403,"span":"span"},"id":"id","titleLink":"titleLink","updated":"updated","status":"LIVE","trashed":"trashed"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fetchBody', True),
                    ('fetchImages', True),
                    ('isDraft', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/blogs/{blog_id}/posts'.format(blog_id='blog_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_list(client):
    """Test case for blogger_posts_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('endDate', 'end_date_example'),
                    ('fetchBodies', True),
                    ('fetchImages', True),
                    ('labels', 'labels_example'),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('sortOption', 'sort_option_example'),
                    ('startDate', 'start_date_example'),
                    ('status', ['status_example']),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/blogs/{blog_id}/posts'.format(blog_id='blog_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_patch(client):
    """Test case for blogger_posts_patch

    
    """
    body = {"images":[{"url":"url"},{"url":"url"}],"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","customMetaData":"customMetaData","published":"published","blog":{"id":"id"},"title":"title","content":"content","url":"url","labels":["labels","labels"],"selfLink":"selfLink","replies":{"totalItems":"totalItems","items":[{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"},{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"}],"selfLink":"selfLink"},"readerComments":"ALLOW","etag":"etag","location":{"lng":1.4658129805029452,"name":"name","lat":6.027456183070403,"span":"span"},"id":"id","titleLink":"titleLink","updated":"updated","status":"LIVE","trashed":"trashed"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fetchBody', True),
                    ('fetchImages', True),
                    ('maxComments', 56),
                    ('publish', True),
                    ('revert', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/blogs/{blog_id}/posts/{post_id}'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_publish(client):
    """Test case for blogger_posts_publish

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('publishDate', 'publish_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/blogs/{blog_id}/posts/{post_id}/publish'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_revert(client):
    """Test case for blogger_posts_revert

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/blogs/{blog_id}/posts/{post_id}/revert'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_search(client):
    """Test case for blogger_posts_search

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('q', 'q_example'),
                    ('fetchBodies', True),
                    ('orderBy', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/blogs/{blog_id}/posts/search'.format(blog_id='blog_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blogger_posts_update(client):
    """Test case for blogger_posts_update

    
    """
    body = {"images":[{"url":"url"},{"url":"url"}],"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","customMetaData":"customMetaData","published":"published","blog":{"id":"id"},"title":"title","content":"content","url":"url","labels":["labels","labels"],"selfLink":"selfLink","replies":{"totalItems":"totalItems","items":[{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"},{"post":{"id":"id"},"author":{"image":{"url":"url"},"displayName":"displayName","id":"id","url":"url"},"kind":"kind","inReplyTo":{"id":"id"},"id":"id","published":"published","blog":{"id":"id"},"updated":"updated","content":"content","selfLink":"selfLink","status":"LIVE"}],"selfLink":"selfLink"},"readerComments":"ALLOW","etag":"etag","location":{"lng":1.4658129805029452,"name":"name","lat":6.027456183070403,"span":"span"},"id":"id","titleLink":"titleLink","updated":"updated","status":"LIVE","trashed":"trashed"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fetchBody', True),
                    ('fetchImages', True),
                    ('maxComments', 56),
                    ('publish', True),
                    ('revert', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/blogs/{blog_id}/posts/{post_id}'.format(blog_id='blog_id_example', post_id='post_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

