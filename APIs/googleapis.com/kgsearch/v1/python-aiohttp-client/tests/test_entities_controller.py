# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_kgsearch_entities_search(client):
    """Test case for kgsearch_entities_search

    
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
                    ('ids', ['ids_example']),
                    ('indent', True),
                    ('languages', ['languages_example']),
                    ('limit', 56),
                    ('prefix', True),
                    ('query', 'query_example'),
                    ('types', ['types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/entities:search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

