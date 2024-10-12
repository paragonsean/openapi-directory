# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection


pytestmark = pytest.mark.asyncio

async def test_collections_add_metadata(client):
    """Test case for collections_add_metadata

    Add Metadata or Subjects to a Entity in a Collection
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection_id}/collected_metadata'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_collected_metadata(client):
    """Test case for collections_collected_metadata

    Retrieve subject data for a specific piece of metadata info for a collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}/subjects'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_create(client):
    """Test case for collections_create

    Create a Collection
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_delete(client):
    """Test case for collections_delete

    Delete a Collection
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection_id}'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_detail(client):
    """Test case for collections_detail

    Retrieve a Collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_nodes_list(client):
    """Test case for collections_linked_nodes_list

    List All Linked Nodes for a Collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/linked_nodes'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_nodes_relationships(client):
    """Test case for collections_linked_nodes_relationships

    Link Nodes to Collection
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection_id}/linked_nodes/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_nodes_relationships_create(client):
    """Test case for collections_linked_nodes_relationships_create

    Give a Sparse List of Node Ids
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/linked_nodes/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_nodes_relationships_delete(client):
    """Test case for collections_linked_nodes_relationships_delete

    Remove Nodes From Collection
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection_id}/linked_nodes/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_preprints_list(client):
    """Test case for collections_linked_preprints_list

    List All Linked Preprints for a Collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/linked_preprints'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_registrations_list(client):
    """Test case for collections_linked_registrations_list

    List All Linked Registrations for a Collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/linked_registrations'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_registrations_relationships(client):
    """Test case for collections_linked_registrations_relationships

    Link Registrations to Collection
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection_id}/linked_registrations/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_registrations_relationships_create(client):
    """Test case for collections_linked_registrations_relationships_create

    Give a Sparse List of Registrations Ids
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/linked_registrations/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_linked_registrations_relationships_delete(client):
    """Test case for collections_linked_registrations_relationships_delete

    Remove Registrations From Collection
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection_id}/linked_registrations/relationships'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_list(client):
    """Test case for collections_list

    List all Collections
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_delete(client):
    """Test case for collections_metadata_delete

    Delete Collection Metadata from entitiy
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_detail(client):
    """Test case for collections_metadata_detail

    Add Metadata or Subjects to an Entity in a Collection
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_registrations_detail(client):
    """Test case for collections_metadata_registrations_detail

    Retrieve Specific Metadata for a Collection
    """
    headers = { 
        'Accept': 'meta',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_registrations_list(client):
    """Test case for collections_metadata_registrations_list

    Retrieve a list of collected metadata for a collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/collected_metadata'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_subjects_relationships(client):
    """Test case for collections_metadata_subjects_relationships

    Retrieve subject metadata for a specific piece of metadata in a collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_metadata_subjects_relationships_update(client):
    """Test case for collections_metadata_subjects_relationships_update

    Update subjects for a specific piece of metadata in a collection
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects'.format(collection_id='collection_id_example', cgm_id='cgm_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

