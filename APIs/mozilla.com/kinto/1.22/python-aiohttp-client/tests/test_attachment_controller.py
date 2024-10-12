# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_attachment(client):
    """Test case for create_attachment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v1/buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment'.format(bucket_id='bucket_id_example', collection_id='collection_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_attachment(client):
    """Test case for delete_attachment

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/buckets/{bucket_id}/collections/{collection_id}/records/{id}/attachment'.format(bucket_id='bucket_id_example', collection_id='collection_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

