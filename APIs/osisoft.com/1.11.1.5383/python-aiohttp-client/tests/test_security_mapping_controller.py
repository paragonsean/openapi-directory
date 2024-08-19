# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.security_mapping import SecurityMapping


pytestmark = pytest.mark.asyncio

async def test_security_mapping_delete(client):
    """Test case for security_mapping_delete

    Delete a security mapping.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/securitymappings/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_mapping_get(client):
    """Test case for security_mapping_get

    Retrieve a security mapping.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securitymappings/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_mapping_get_by_path(client):
    """Test case for security_mapping_get_by_path

    Retrieve a security mapping by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securitymappings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_mapping_get_security(client):
    """Test case for security_mapping_get_security

    Get the security information of the specified security item associated with the security mapping for a specified user.
    """
    params = [('userIdentity', ['user_identity_example']),
                    ('forceRefresh', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securitymappings/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_mapping_get_security_entries(client):
    """Test case for security_mapping_get_security_entries

    Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securitymappings/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_mapping_get_security_entry_by_name(client):
    """Test case for security_mapping_get_security_entry_by_name

    Retrieve the security entry associated with the security mapping with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securitymappings/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_security_mapping_update(client):
    """Test case for security_mapping_update

    Update a security mapping by replacing items in its definition.
    """
    security_mapping = {"Path":"\\\\MyAssetServer\\SecurityMappings[MySecurityMapping]","Account":"domain\\user","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1SMDqD5loBNH0erqeqJodtALAgu8UrMAZB0qWp9H7C4TAXQ","SecurityIdentityWebId":"I1SIEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","Links":{"SecurityIdentity":"SecurityIdentity","SecurityEntries":"SecurityEntries","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Id":"ac14ef82-19c0-4a07-96a7-d1fb0b84c05d","Name":"MySecurityMapping"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/securitymappings/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=security_mapping,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

