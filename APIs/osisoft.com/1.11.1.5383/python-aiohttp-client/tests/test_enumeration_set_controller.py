# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.enumeration_value import EnumerationValue
from openapi_server.models.errors import Errors
from openapi_server.models.items_enumeration_value import ItemsEnumerationValue
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enumeration_set_create_security_entry(client):
    """Test case for enumeration_set_create_security_entry

    Create a security entry owned by the enumeration set.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/enumerationsets/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enumeration_set_create_value(client):
    """Test case for enumeration_set_create_value

    Create an enumeration value for a enumeration set.
    """
    enumeration_value = {"Path":"\\\\MyAssetServer\\MyDatabase\\EnumerationSets[Model Number]\\CarBrand|Model3","SerializePath":True,"Description":"Model Number of CarBrand","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Parent":"CarBrand","SerializeId":True,"Name":"CarBrand|Model3","SerializeWebId":True,"WebId":"I1MVRDqD5loBNH0erqeqJodtALAT_x3jpGsKUCB1vtmvQHUMQlIYqmOlvs0ygEQnSeGSe7w","Value":2005,"Links":{"EnumerationSet":"EnumerationSet","Parent":"Parent","Self":"Self"},"SerializeLinks":True,"Id":"982a8694-6fe9-4cb3-a011-09d278649eef","SerializeDescription":True}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/enumerationsets/{web_id}/enumerationvalues'.format(web_id='web_id_example'),
        headers=headers,
        json=enumeration_value,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_delete(client):
    """Test case for enumeration_set_delete

    Delete an enumeration set.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/enumerationsets/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_delete_security_entry(client):
    """Test case for enumeration_set_delete_security_entry

    Delete a security entry owned by the enumeration set.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/enumerationsets/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get(client):
    """Test case for enumeration_set_get

    Retrieve an enumeration set.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationsets/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get_by_path(client):
    """Test case for enumeration_set_get_by_path

    Retrieve an enumeration set by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationsets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get_security(client):
    """Test case for enumeration_set_get_security

    Get the security information of the specified security item associated with the enumeration set for a specified user.
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
        path='/piwebapi/enumerationsets/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get_security_entries(client):
    """Test case for enumeration_set_get_security_entries

    Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationsets/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get_security_entry_by_name(client):
    """Test case for enumeration_set_get_security_entry_by_name

    Retrieve the security entry associated with the enumeration set with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationsets/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_set_get_values(client):
    """Test case for enumeration_set_get_values

    Retrieve an enumeration set's values.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationsets/{web_id}/enumerationvalues'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enumeration_set_update(client):
    """Test case for enumeration_set_update

    Update an enumeration set by replacing items in its definition.
    """
    enumeration_set = {"Path":"\\\\MyAssetServer\\MyDatabase\\EnumerationSets[Model Number]","Description":"Model numbers by brand of vehicle","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1MSRDqD5loBNH0erqeqJodtALAT_x3jpGsKUCB1vtmvQHUMQ","Links":{"SecurityEntries":"SecurityEntries","DataServer":"DataServer","Database":"Database","Values":"Values","Self":"Self","Security":"Security"},"Id":"8e77fc4f-ac91-4029-81d6-fb66bd01d431","SerializeDescription":True,"Name":"Model Number"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/enumerationsets/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=enumeration_set,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enumeration_set_update_security_entry(client):
    """Test case for enumeration_set_update_security_entry

    Update a security entry owned by the enumeration set.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/enumerationsets/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

