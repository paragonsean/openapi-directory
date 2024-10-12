# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.create_collection_request import CreateCollectionRequest
from openapi_server.models.guid_collection import GuidCollection
from openapi_server.models.id4n import Id4n
from openapi_server.models.list_of_id4n_properties import ListOfId4nProperties
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid
from openapi_server.models.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_elements_to_collection(client):
    """Test case for add_elements_to_collection

    Add elements to collection
    """
    body = {"id4ns":["id4ns","id4ns"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/collections/{id4n}/elements'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_collection(client):
    """Test case for create_collection

    Create collection
    """
    body = {"organizationId":"de.acme","length":25,"label":"label","type":"ROUTING_COLLECTION"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection(client):
    """Test case for delete_collection

    Delete collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/collections/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_properties(client):
    """Test case for delete_properties

    Delete ID4n properties
    """
    body = ['body_example']
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/id4ns/{id4n}/properties'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_collection(client):
    """Test case for find_collection

    Find collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/collections/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_collections_of_organization(client):
    """Test case for get_all_collections_of_organization

    Get collections of organization
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('label', 'label_example'),
                    ('labelPrefix', 'label_prefix_example'),
                    ('property', ['_property_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/collections'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_properties(client):
    """Test case for get_multiple_properties

    Get multiple ID4n properties
    """
    params = [('id4ns', ['id4ns_example']),
                    ('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/multiple/id4ns/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_properties(client):
    """Test case for get_properties

    Retrieve ID4n properties
    """
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/id4ns/{id4n}/properties'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_elements_of_collection(client):
    """Test case for list_elements_of_collection

    List contents of the collection
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/collections/{id4n}/elements'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_patch_properties(client):
    """Test case for patch_properties

    Patch ID4n properties
    """
    body = {'key': 'body_example'}
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/id4ns/{id4n}/properties'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_remove_elements_from_collection(client):
    """Test case for remove_elements_from_collection

    Remove elements from collection
    """
    body = {"id4ns":["id4ns","id4ns"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/collections/{id4n}/elements'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_collection(client):
    """Test case for update_collection

    Update collection
    """
    body = {"physicalState":"UNATTACHED","id4n":"id4n","ownerOrganizationId":"ownerOrganizationId","holderOrganizationId":"holderOrganizationId","createdTimestamp":0,"label":"label","type":"ROUTING_COLLECTION"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/collections/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

