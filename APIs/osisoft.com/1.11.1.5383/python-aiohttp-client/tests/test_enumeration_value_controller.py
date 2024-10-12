# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.enumeration_value import EnumerationValue


pytestmark = pytest.mark.asyncio

async def test_enumeration_value_delete_enumeration_value(client):
    """Test case for enumeration_value_delete_enumeration_value

    Delete an enumeration value from an enumeration set.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/enumerationvalues/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_value_get(client):
    """Test case for enumeration_value_get

    Retrieve an enumeration value mapping
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationvalues/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enumeration_value_get_by_path(client):
    """Test case for enumeration_value_get_by_path

    Retrieve an enumeration value by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/enumerationvalues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_enumeration_value_update_enumeration_value(client):
    """Test case for enumeration_value_update_enumeration_value

    Update an enumeration value by replacing items in its definition.
    """
    enumeration_value = {"Path":"\\\\MyAssetServer\\MyDatabase\\EnumerationSets[Model Number]\\CarBrand|Model3","SerializePath":True,"Description":"Model Number of CarBrand","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"Parent":"CarBrand","SerializeId":True,"Name":"CarBrand|Model3","SerializeWebId":True,"WebId":"I1MVRDqD5loBNH0erqeqJodtALAT_x3jpGsKUCB1vtmvQHUMQlIYqmOlvs0ygEQnSeGSe7w","Value":2005,"Links":{"EnumerationSet":"EnumerationSet","Parent":"Parent","Self":"Self"},"SerializeLinks":True,"Id":"982a8694-6fe9-4cb3-a011-09d278649eef","SerializeDescription":True}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/enumerationvalues/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=enumeration_value,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

