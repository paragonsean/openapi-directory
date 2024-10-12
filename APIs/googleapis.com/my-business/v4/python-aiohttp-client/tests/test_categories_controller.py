# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_get_business_categories_response import BatchGetBusinessCategoriesResponse
from openapi_server.models.list_business_categories_response import ListBusinessCategoriesResponse


pytestmark = pytest.mark.asyncio

async def test_mybusiness_categories_batch_get(client):
    """Test case for mybusiness_categories_batch_get

    
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
                    ('categoryIds', ['category_ids_example']),
                    ('languageCode', 'language_code_example'),
                    ('regionCode', 'region_code_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/categories:batchGet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_categories_list(client):
    """Test case for mybusiness_categories_list

    
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
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('regionCode', 'region_code_example'),
                    ('searchTerm', 'search_term_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

