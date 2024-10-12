# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.review import Review
from openapi_server.models.reviews_list_response import ReviewsListResponse
from openapi_server.models.reviews_reply_request import ReviewsReplyRequest
from openapi_server.models.reviews_reply_response import ReviewsReplyResponse


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_reviews_get(client):
    """Test case for androidpublisher_reviews_get

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('translationLanguage', 'translation_language_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/reviews/{review_id}'.format(package_name='package_name_example', review_id='review_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_reviews_list(client):
    """Test case for androidpublisher_reviews_list

    
    """
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('maxResults', 56),
                    ('startIndex', 56),
                    ('token', 'token_example'),
                    ('translationLanguage', 'translation_language_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidpublisher/v2/applications/{package_name}/reviews'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidpublisher_reviews_reply(client):
    """Test case for androidpublisher_reviews_reply

    
    """
    body = {"replyText":"replyText"}
    params = [('alt', json),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/androidpublisher/v2/applications/{package_name}/reviews/{review_idrepl}'.format(package_name='package_name_example', review_id='review_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

