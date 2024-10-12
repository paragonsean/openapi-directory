# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.cache_invalidation_request_schema import CacheInvalidationRequestSchema


pytestmark = pytest.mark.asyncio

async def test_cachekey_invalidate_post(client):
    """Test case for cachekey_invalidate_post

    
    """
    body = {"datasources":[{"schema":"schema","database_name":"database_name","datasource_type":"druid","datasource_name":"datasource_name"},{"schema":"schema","database_name":"database_name","datasource_type":"druid","datasource_name":"datasource_name"}],"datasource_uids":["datasource_uids","datasource_uids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/cachekey/invalidate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

