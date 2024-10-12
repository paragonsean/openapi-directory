# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.create_guid_request import CreateGuidRequest
from openapi_server.models.guid import Guid
from openapi_server.models.guid_alias import GuidAlias
from openapi_server.models.id4n_presentation import Id4nPresentation
from openapi_server.models.import_gs1_codes_request import ImportGS1CodesRequest
from openapi_server.models.list_of_id4n_properties import ListOfId4nProperties
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_guid import PaginatedResponseOfGuid
from openapi_server.models.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_guid_alias_0(client):
    """Test case for add_guid_alias_0

    Add alias for GUID or Collection
    """
    body = {"alias":"alias"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/id4ns/{id4n}/alias/{alias_type}'.format(id4n='id4n_example', alias_type='alias_type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_guid(client):
    """Test case for create_guid

    Create GUID(s)
    """
    body = {"organizationId":"de.acme","count":1,"length":40}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/guids',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_delete_properties_0(client):
    """Test case for delete_properties_0

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

async def test_get_collections(client):
    """Test case for get_collections

    Retrieve collections of an ID
    """
    params = [('organizationId', 'organization_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/id4ns/{id4n}/collections'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guid(client):
    """Test case for get_guid

    Retrieve GUID information
    """
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/guids/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guid_aliases_0(client):
    """Test case for get_guid_aliases_0

    Get all aliases for the given GUID or Collection.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/id4ns/{id4n}/alias'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guids_without_collection(client):
    """Test case for get_guids_without_collection

    Retrieve GUIDs not in any collection
    """
    params = [('organizationId', 'organization_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/guids/withoutCollection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_id4n(client):
    """Test case for get_id4n

    Retrieve ID4n information
    """
    params = [('organizationId', 'organization_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/id4ns/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_properties_0(client):
    """Test case for get_multiple_properties_0

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

async def test_get_properties_0(client):
    """Test case for get_properties_0

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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_import_gs1_codes(client):
    """Test case for import_gs1_codes

    Import GS1/MAPP codes
    """
    body = {"organizationId":"de.acme","listOfGS1s":{"codes":["codes","codes"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/import/gs1',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_patch_properties_0(client):
    """Test case for patch_properties_0

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

async def test_remove_guid_alias_0(client):
    """Test case for remove_guid_alias_0

    Remove aliases from GUID or Collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/id4ns/{id4n}/alias/{alias_type}'.format(id4n='id4n_example', alias_type='alias_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_guid(client):
    """Test case for update_guid

    Change GUID information.
    """
    body = {"physicalState":"UNATTACHED","id4n":"3THvgrWxqgTFC4","ownerOrganizationId":"ownerOrganizationId","holderOrganizationId":"holderOrganizationId","createdTimestamp":1517232722,"properties":"de.example"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/guids/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

