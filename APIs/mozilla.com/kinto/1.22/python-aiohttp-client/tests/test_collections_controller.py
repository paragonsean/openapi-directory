# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.object_schema1 import ObjectSchema1
from openapi_server.models.schema2 import Schema2


pytestmark = pytest.mark.asyncio

async def test_get_collection(client):
    """Test case for get_collection

    
    """
    params = [('_fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/buckets/{bucket_id}/collections/{id}'.format(bucket_id='bucket_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collections(client):
    """Test case for get_collections

    
    """
    params = [('_limit', 56),
                    ('_sort', ['sort_example']),
                    ('_token', 'token_example'),
                    ('_since', 56),
                    ('_to', 56),
                    ('_before', 56),
                    ('id', 'id_example'),
                    ('last_modified', 56),
                    ('_fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/buckets/{bucket_id}/collections'.format(bucket_id='bucket_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

