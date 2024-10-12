# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.namespace_data import NamespaceData
from openapi_server.models.namespace_metadata import NamespaceMetadata


pytestmark = pytest.mark.asyncio

async def test_get_namespace(client):
    """Test case for get_namespace

    Get namespace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/namespaces/{namespace}'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespaces(client):
    """Test case for get_namespaces

    Get namespaces and repos
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

