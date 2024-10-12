# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.namespace_patch import NamespacePatch
from openapi_server.models.namespace_post import NamespacePost
from openapi_server.models.namespace_response import NamespaceResponse


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_namespaces_get(client):
    """Test case for apps_app_id_namespaces_get

    Lists namespaces
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{app_id}/namespaces'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_namespaces_namespace_id_delete(client):
    """Test case for apps_app_id_namespaces_namespace_id_delete

    Deletes a namespace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/apps/{app_id}/namespaces/{namespace_id}'.format(app_id='app_id_example', namespace_id='namespace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_namespaces_namespace_id_patch(client):
    """Test case for apps_app_id_namespaces_namespace_id_patch

    Updates a namespace
    """
    body = openapi_server.NamespacePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/apps/{app_id}/namespaces/{namespace_id}'.format(app_id='app_id_example', namespace_id='namespace_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_namespaces_post(client):
    """Test case for apps_app_id_namespaces_post

    Creates a namespace
    """
    body = openapi_server.NamespacePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/apps/{app_id}/namespaces'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

