# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.unit import Unit
from openapi_server.models.unit_class import UnitClass


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unit_class_create_unit(client):
    """Test case for unit_class_create_unit

    Create a unit in the specified Unit Class.
    """
    unit_dto = {"Abbreviation":"Hz","Path":"\\\\MyAssetServer\\UOMDatabase\\Hertz","Description":"Hertz Unit","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ReferenceOffset":0.0,"Name":"Hertz","Offset":0.0,"ReferenceUnitAbbreviation":"","ReferenceFactor":1.0,"WebId":"I1UtDqD5loBNH0erqeqJodtALAjqwhgeI8lEeV4xeD1db0_A","Factor":1.0,"Links":{"ReferenceUnit":"ReferenceUnit","Class":"Class","Self":"Self"},"Id":"8121ac8e-3ce2-4794-95e3-1783d5d6f4fc"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/unitclasses/{web_id}/units'.format(web_id='web_id_example'),
        headers=headers,
        json=unit_dto,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_class_delete(client):
    """Test case for unit_class_delete

    Delete a unit class.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/unitclasses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_class_get(client):
    """Test case for unit_class_get

    Retrieve a unit class.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/unitclasses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_class_get_by_path(client):
    """Test case for unit_class_get_by_path

    Retrieve a unit class by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/unitclasses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_class_get_canonical_unit(client):
    """Test case for unit_class_get_canonical_unit

    Get the canonical unit of a unit class.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/unitclasses/{web_id}/canonicalunit'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_class_get_units(client):
    """Test case for unit_class_get_units

    Get a list of all units belonging to the unit class.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/unitclasses/{web_id}/units'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unit_class_update(client):
    """Test case for unit_class_update

    Update a unit class.
    """
    unit_class_dto = {"Path":"\\\\MyAssetServer\\UOMDatabase\\UOMClasses[Power]","Description":"Power Unit Class","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"CanonicalUnitAbbreviation":"W","WebId":"I1UCDqD5loBNH0erqeqJodtALATbkl-fxulEulDQAVw5HySQ","Links":{"CanonicalUnit":"CanonicalUnit","Self":"Self","AssetServer":"AssetServer","Units":"Units"},"Id":"f925b94d-6efc-4b94-a50d-0015c391f249","CanonicalUnitName":"watt","Name":"Power"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/unitclasses/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=unit_class_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

