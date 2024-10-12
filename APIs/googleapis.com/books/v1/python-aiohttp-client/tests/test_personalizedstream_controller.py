# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.discoveryclusters import Discoveryclusters


pytestmark = pytest.mark.asyncio

async def test_books_personalizedstream_get(client):
    """Test case for books_personalizedstream_get

    
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
                    ('locale', 'locale_example'),
                    ('maxAllowedMaturityRating', 'max_allowed_maturity_rating_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/personalizedstream/get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

