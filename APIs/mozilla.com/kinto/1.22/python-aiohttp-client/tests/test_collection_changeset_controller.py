# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_collection_changeset(client):
    """Test case for get_collection_changeset

    
    """
    params = [('_since', 'since_example'),
                    ('_expected', 'expected_example'),
                    ('_limit', 56),
                    ('bucket', 'bucket_example'),
                    ('collection', 'collection_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/buckets/{bid}/collections/{cid}/changeset'.format(bid='bid_example', cid='cid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

