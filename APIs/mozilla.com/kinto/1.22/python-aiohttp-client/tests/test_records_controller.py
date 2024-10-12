# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.object_schema import ObjectSchema
from openapi_server.models.schema3 import Schema3


pytestmark = pytest.mark.asyncio

async def test_get_record(client):
    """Test case for get_record

    
    """
    params = [('_fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/buckets/{bucket_id}/collections/{collection_id}/records/{id}'.format(bucket_id='bucket_id_example', collection_id='collection_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_records(client):
    """Test case for get_records

    
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
        path='/v1/buckets/{bucket_id}/collections/{collection_id}/records'.format(bucket_id='bucket_id_example', collection_id='collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

