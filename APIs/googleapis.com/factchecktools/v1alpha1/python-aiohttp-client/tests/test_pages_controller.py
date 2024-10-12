# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_factchecking_factchecktools_v1alpha1_claim_review_markup_page import GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage
from openapi_server.models.google_factchecking_factchecktools_v1alpha1_list_claim_review_markup_pages_response import GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse


pytestmark = pytest.mark.asyncio

async def test_factchecktools_pages_create(client):
    """Test case for factchecktools_pages_create

    
    """
    body = {"versionId":"versionId","claimReviewAuthor":{"imageUrl":"imageUrl","name":"name"},"name":"name","publishDate":"publishDate","pageUrl":"pageUrl","claimReviewMarkups":[{"claimLocation":"claimLocation","claimReviewed":"claimReviewed","claimFirstAppearance":"claimFirstAppearance","claimDate":"claimDate","claimAuthor":{"imageUrl":"imageUrl","jobTitle":"jobTitle","name":"name","sameAs":"sameAs"},"rating":{"bestRating":0,"textualRating":"textualRating","imageUrl":"imageUrl","ratingValue":6,"worstRating":1,"ratingExplanation":"ratingExplanation"},"claimAppearances":["claimAppearances","claimAppearances"],"url":"url"},{"claimLocation":"claimLocation","claimReviewed":"claimReviewed","claimFirstAppearance":"claimFirstAppearance","claimDate":"claimDate","claimAuthor":{"imageUrl":"imageUrl","jobTitle":"jobTitle","name":"name","sameAs":"sameAs"},"rating":{"bestRating":0,"textualRating":"textualRating","imageUrl":"imageUrl","ratingValue":6,"worstRating":1,"ratingExplanation":"ratingExplanation"},"claimAppearances":["claimAppearances","claimAppearances"],"url":"url"}]}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/pages',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factchecktools_pages_delete(client):
    """Test case for factchecktools_pages_delete

    
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
        method='DELETE',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factchecktools_pages_get(client):
    """Test case for factchecktools_pages_get

    
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
        method='GET',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factchecktools_pages_list(client):
    """Test case for factchecktools_pages_list

    
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
                    ('offset', 56),
                    ('organization', 'organization_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/pages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factchecktools_pages_update(client):
    """Test case for factchecktools_pages_update

    
    """
    body = {"versionId":"versionId","claimReviewAuthor":{"imageUrl":"imageUrl","name":"name"},"name":"name","publishDate":"publishDate","pageUrl":"pageUrl","claimReviewMarkups":[{"claimLocation":"claimLocation","claimReviewed":"claimReviewed","claimFirstAppearance":"claimFirstAppearance","claimDate":"claimDate","claimAuthor":{"imageUrl":"imageUrl","jobTitle":"jobTitle","name":"name","sameAs":"sameAs"},"rating":{"bestRating":0,"textualRating":"textualRating","imageUrl":"imageUrl","ratingValue":6,"worstRating":1,"ratingExplanation":"ratingExplanation"},"claimAppearances":["claimAppearances","claimAppearances"],"url":"url"},{"claimLocation":"claimLocation","claimReviewed":"claimReviewed","claimFirstAppearance":"claimFirstAppearance","claimDate":"claimDate","claimAuthor":{"imageUrl":"imageUrl","jobTitle":"jobTitle","name":"name","sameAs":"sameAs"},"rating":{"bestRating":0,"textualRating":"textualRating","imageUrl":"imageUrl","ratingValue":6,"worstRating":1,"ratingExplanation":"ratingExplanation"},"claimAppearances":["claimAppearances","claimAppearances"],"url":"url"}]}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

