# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.unit import Unit


pytestmark = pytest.mark.asyncio

async def test_unit_delete(client):
    """Test case for unit_delete

    Delete a unit.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/units/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_get(client):
    """Test case for unit_get

    Retrieve a unit.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/units/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unit_get_by_path(client):
    """Test case for unit_get_by_path

    Retrieve a unit by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/units',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_unit_update(client):
    """Test case for unit_update

    Update a unit.
    """
    unit_dto = {"Abbreviation":"Hz","Path":"\\\\MyAssetServer\\UOMDatabase\\Hertz","Description":"Hertz Unit","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ReferenceOffset":0.0,"Name":"Hertz","Offset":0.0,"ReferenceUnitAbbreviation":"","ReferenceFactor":1.0,"WebId":"I1UtDqD5loBNH0erqeqJodtALAjqwhgeI8lEeV4xeD1db0_A","Factor":1.0,"Links":{"ReferenceUnit":"ReferenceUnit","Class":"Class","Self":"Self"},"Id":"8121ac8e-3ce2-4794-95e3-1783d5d6f4fc"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/units/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=unit_dto,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

