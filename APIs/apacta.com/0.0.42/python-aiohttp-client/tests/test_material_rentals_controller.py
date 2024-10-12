# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.materials_material_id_rentals_checkout_post_request import MaterialsMaterialIdRentalsCheckoutPostRequest
from openapi_server.models.materials_material_id_rentals_get200_response import MaterialsMaterialIdRentalsGet200Response
from openapi_server.models.materials_material_id_rentals_material_rental_id_get200_response import MaterialsMaterialIdRentalsMaterialRentalIdGet200Response
from openapi_server.models.materials_material_id_rentals_post_request import MaterialsMaterialIdRentalsPostRequest


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_checkout_post(client):
    """Test case for materials_material_id_rentals_checkout_post

    Checkout material rental
    """
    body = openapi_server.MaterialsMaterialIdRentalsCheckoutPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/materials/{material_id}/rentals/checkout'.format(material_id='material_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_get(client):
    """Test case for materials_material_id_rentals_get

    Show list of rentals for specific material
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/materials/{material_id}/rentals'.format(material_id='material_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_material_rental_id_delete(client):
    """Test case for materials_material_id_rentals_material_rental_id_delete

    Delete material rental
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/materials/{material_id}/rentals/{material_rental_id}'.format(material_id='material_id_example', material_rental_id='material_rental_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_material_rental_id_get(client):
    """Test case for materials_material_id_rentals_material_rental_id_get

    Show rental foor materi
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/materials/{material_id}/rentals/{material_rental_id}'.format(material_id='material_id_example', material_rental_id='material_rental_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_material_rental_id_put(client):
    """Test case for materials_material_id_rentals_material_rental_id_put

    Edit material rental
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/materials/{material_id}/rentals/{material_rental_id}'.format(material_id='material_id_example', material_rental_id='material_rental_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_materials_material_id_rentals_post(client):
    """Test case for materials_material_id_rentals_post

    Add material rental
    """
    body = openapi_server.MaterialsMaterialIdRentalsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/materials/{material_id}/rentals'.format(material_id='material_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

