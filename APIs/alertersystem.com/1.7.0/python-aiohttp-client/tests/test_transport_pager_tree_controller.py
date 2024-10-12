# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_transport_pager_tree_get_collection200_response import ApiTransportPagerTreeGetCollection200Response
from openapi_server.models.transport_pager_tree_get import TransportPagerTreeGet
from openapi_server.models.transport_pager_tree_jsonld_get import TransportPagerTreeJsonldGet
from openapi_server.models.transport_pager_tree_jsonld_post import TransportPagerTreeJsonldPost
from openapi_server.models.transport_pager_tree_jsonld_put import TransportPagerTreeJsonldPut
from openapi_server.models.transport_pager_tree_patch import TransportPagerTreePatch
from openapi_server.models.transport_pager_tree_post import TransportPagerTreePost
from openapi_server.models.transport_pager_tree_put import TransportPagerTreePut


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_tree_get_collection(client):
    """Test case for api_transport_pager_tree_get_collection

    Retrieves the collection of TransportPagerTree resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pager-tree',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_tree_id_delete(client):
    """Test case for api_transport_pager_tree_id_delete

    Removes the TransportPagerTree resource.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/transport-pager-tree/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_tree_id_get(client):
    """Test case for api_transport_pager_tree_id_get

    Retrieves a TransportPagerTree resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/transport-pager-tree/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_transport_pager_tree_id_patch(client):
    """Test case for api_transport_pager_tree_id_patch

    Updates the TransportPagerTree resource.
    """
    body = openapi_server.TransportPagerTreePatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/transport-pager-tree/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pager_tree_id_put(client):
    """Test case for api_transport_pager_tree_id_put

    Replaces the TransportPagerTree resource.
    """
    body = openapi_server.TransportPagerTreePut()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/transport-pager-tree/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_transport_pager_tree_post(client):
    """Test case for api_transport_pager_tree_post

    Creates a TransportPagerTree resource.
    """
    body = openapi_server.TransportPagerTreePost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/transport-pager-tree',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

