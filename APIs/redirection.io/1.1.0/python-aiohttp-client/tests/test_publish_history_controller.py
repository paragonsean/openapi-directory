# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.publish_history_read import PublishHistoryRead


pytestmark = pytest.mark.asyncio

async def test_get_publish_history_collection(client):
    """Test case for get_publish_history_collection

    Retrieves the collection of PublishHistory resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('createdAt[before]', 'created_at_before_example'),
                    ('createdAt[strictly_before]', 'created_at_strictly_before_example'),
                    ('createdAt[after]', 'created_at_after_example'),
                    ('createdAt[strictly_after]', 'created_at_strictly_after_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/publish-histories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_publish_history_item(client):
    """Test case for get_publish_history_item

    Retrieves a PublishHistory resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/publish-histories/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

