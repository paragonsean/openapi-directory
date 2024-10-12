# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.buckets import Buckets
from openapi_server.models.error import Error
from openapi_server.models.health_check import HealthCheck
from openapi_server.models.source import Source
from openapi_server.models.sources import Sources


pytestmark = pytest.mark.asyncio

async def test_delete_sources_id(client):
    """Test case for delete_sources_id

    Delete a source
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/sources/{source_id}'.format(source_id='source_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sources(client):
    """Test case for get_sources

    List all sources
    """
    params = [('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/sources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sources_id(client):
    """Test case for get_sources_id

    Retrieve a source
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/sources/{source_id}'.format(source_id='source_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sources_id_buckets(client):
    """Test case for get_sources_id_buckets

    Get buckets in a source
    """
    params = [('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/sources/{source_id}/buckets'.format(source_id='source_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sources_id_health(client):
    """Test case for get_sources_id_health

    Get the health of a source
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/sources/{source_id}/health'.format(source_id='source_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_sources_id(client):
    """Test case for patch_sources_id

    Update a Source
    """
    body = {"languages":["flux","flux"],"defaultRP":"defaultRP","type":"v1","orgID":"orgID","url":"https://openapi-generator.tech","token":"token","default":True,"password":"password","telegraf":"telegraf","insecureSkipVerify":True,"name":"name","links":{"buckets":"buckets","query":"query","health":"health","self":"self"},"metaUrl":"https://openapi-generator.tech","id":"id","sharedSecret":"sharedSecret","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/sources/{source_id}'.format(source_id='source_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_sources(client):
    """Test case for post_sources

    Create a source
    """
    body = {"languages":["flux","flux"],"defaultRP":"defaultRP","type":"v1","orgID":"orgID","url":"https://openapi-generator.tech","token":"token","default":True,"password":"password","telegraf":"telegraf","insecureSkipVerify":True,"name":"name","links":{"buckets":"buckets","query":"query","health":"health","self":"self"},"metaUrl":"https://openapi-generator.tech","id":"id","sharedSecret":"sharedSecret","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/sources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

