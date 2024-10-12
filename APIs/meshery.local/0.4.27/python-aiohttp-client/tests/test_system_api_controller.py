# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.adapter import Adapter
from openapi_server.models.k8_s_config import K8SConfig
from openapi_server.models.k8_s_context import K8SContext
from openapi_server.models.preference import Preference
from openapi_server.models.service import Service
from openapi_server.models.version import Version


pytestmark = pytest.mark.asyncio

async def test_id_delete_adapter_config(client):
    """Test case for id_delete_adapter_config

    Handle DELETE requests to delete adapter config
    """
    params = [('adapter', 'adapter_example')]
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/system/adapter/manage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_delete_k8_s_config(client):
    """Test case for id_delete_k8_s_config

    Handle DELETE request for Kubernetes Config
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/system/kubernetes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_kubernetes_ping(client):
    """Test case for id_get_kubernetes_ping

    Handle GET request for Kubernetes ping
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/kubernetes/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_system_adapters(client):
    """Test case for id_get_system_adapters

    Handle GET request for adapters
    """
    params = [('adapter', 'adapter_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/adapters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_system_version(client):
    """Test case for id_get_system_version

    Handle GET request for system/server version
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_mesh_sync_grafana(client):
    """Test case for id_mesh_sync_grafana

    Handle GET request for mesh-sync grafana
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/meshsync/grafana',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_mesh_sync_prometheus(client):
    """Test case for id_mesh_sync_prometheus

    Handle GET request for fetching prometheus
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/meshsync/prometheus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_id_post_adapter_config(client):
    """Test case for id_post_adapter_config

    Handle POST requests to persist adapter config
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/system/adapter/manage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_adapter_operation(client):
    """Test case for id_post_adapter_operation

    Handle POST requests for Adapter Operations
    """
    params = [('adapter', 'adapter_example'),
                    ('query', 'query_example'),
                    ('customBody', 'custom_body_example'),
                    ('namespace', 'namespace_example'),
                    ('deleteOp', 'delete_op_example')]
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/system/adapter/operation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_k8_s_config(client):
    """Test case for id_post_k8_s_config

    Handle POST request for Kubernetes Config
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/system/kubernetes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_k8_s_contexts(client):
    """Test case for id_post_k8_s_contexts

    Handle POST requests for Kubernetes Context list
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/system/kubernetes/contexts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_system_sync(client):
    """Test case for id_system_sync

    Handle GET request for config sync
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/system/sync',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

