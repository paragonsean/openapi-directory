# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_validate_documentby_clusters(client):
    """Test case for validate_documentby_clusters

    Validate Document by Clusters
    """
    body = [{"name":"male","rule":"gender=male"},{"name":"complex","rule":"((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"},{"name":"complex2","rule":"((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"},{"name":"createdIn","rule":"createdIn between 2015-10-28 AND 2015-10-30"}]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/dataentities/{acronym}/documents/{id}/clusters'.format(acronym='{{acronym}}', id='{{id}}'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

