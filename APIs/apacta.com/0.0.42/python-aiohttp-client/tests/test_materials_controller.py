# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.materials_get200_response import MaterialsGet200Response
from openapi_server.models.materials_material_id_get200_response import MaterialsMaterialIdGet200Response
from openapi_server.models.materials_post_request import MaterialsPostRequest


pytestmark = pytest.mark.asyncio

async def test_materials_get(client):
    """Test case for materials_get

    View list of all materials
    """
    params = [('barcode', 'barcode_example'),
                    ('name', 'name_example'),
                    ('project_id', 'project_id_example'),
                    ('currently_rented', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/materials',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_delete(client):
    """Test case for materials_material_id_delete

    Delete material
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/materials/{material_id}'.format(material_id='material_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_get(client):
    """Test case for materials_material_id_get

    View material
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/materials/{material_id}'.format(material_id='material_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_put(client):
    """Test case for materials_material_id_put

    Edit material
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/materials/{material_id}'.format(material_id='material_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_post(client):
    """Test case for materials_post

    Add material
    """
    body = openapi_server.MaterialsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/materials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

