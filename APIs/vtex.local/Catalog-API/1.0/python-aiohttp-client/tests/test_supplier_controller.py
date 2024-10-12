# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.supplier_request import SupplierRequest
from openapi_server.models.supplier_response import SupplierResponse


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_supplier_post(client):
    """Test case for api_catalog_pvt_supplier_post

    Create Supplier
    """
    body = {"CorportePhone":"5555555555","Email":"email@email.com","Cnpj":"33304981001272","IsActive":False,"Phone":"3333333333","StateInscription":"123456","CellPhone":"4444444444","CorporateName":"TopStore","Name":"Supplier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/supplier',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_supplier_supplier_id_delete(client):
    """Test case for api_catalog_pvt_supplier_supplier_id_delete

    Delete Supplier
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/supplier/{supplier_id}'.format(supplier_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_supplier_supplier_id_put(client):
    """Test case for api_catalog_pvt_supplier_supplier_id_put

    Update Supplier
    """
    body = {"CorportePhone":"5555555555","Email":"email@email.com","Cnpj":"33304981001272","IsActive":False,"Phone":"3333333333","StateInscription":"123456","CellPhone":"4444444444","CorporateName":"TopStore","Name":"Supplier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog/pvt/supplier/{supplier_id}'.format(supplier_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

