# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_mapping import ItemsSecurityMapping
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.security_identity import SecurityIdentity


pytestmark = pytest.mark.asyncio

async def test_security_identity_delete(client):
    """Test case for security_identity_delete

    Delete a security identity.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/securityidentities/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get(client):
    """Test case for security_identity_get

    Retrieve a security identity.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securityidentities/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get_by_path(client):
    """Test case for security_identity_get_by_path

    Retrieve a security identity by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securityidentities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get_security(client):
    """Test case for security_identity_get_security

    Get the security information of the specified security item associated with the security identity for a specified user.
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
        path='/piwebapi/securityidentities/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get_security_entries(client):
    """Test case for security_identity_get_security_entries

    Retrieve the security entries associated with the security identity based on the specified criteria. By default, all security entries for this security identity are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securityidentities/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get_security_entry_by_name(client):
    """Test case for security_identity_get_security_entry_by_name

    Retrieve the security entry associated with the security identity with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securityidentities/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_identity_get_security_mappings(client):
    """Test case for security_identity_get_security_mappings

    Get security mappings for the specified security identity.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/securityidentities/{web_id}/securitymappings'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_security_identity_update(client):
    """Test case for security_identity_update

    Update a security identity by replacing items in its definition.
    """
    security_identity = {"Path":"\\\\MyAssetServer\\SecurityIdentities[MySecurityIdentity]","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"IsEnabled":True,"WebId":"I1SIDqD5loBNH0erqeqJodtALASe6l8zgYokqdeeFilFI9tw","Links":{"SecurityEntries":"SecurityEntries","SecurityMappings":"SecurityMappings","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Id":"f3a5ee49-1838-4aa2-9d79-e16294523db7","Name":"MySecurityIdentity"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/securityidentities/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=security_identity,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

