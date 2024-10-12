# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationvalue_specification_value_id_get200_response import ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response
from openapi_server.models.get_spec_field_value import GetSpecFieldValue
from openapi_server.models.specifications_insert_field_value_request import SpecificationsInsertFieldValueRequest
from openapi_server.models.specifications_update_field_value_request import SpecificationsUpdateFieldValueRequest


pytestmark = pytest.mark.asyncio

async def test_specifications_get_field_value(client):
    """Test case for specifications_get_field_value

    Get Specification Field Value
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/specification/fieldValue/{field_value_id}'.format(field_value_id='143'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_insert_field_value(client):
    """Test case for specifications_insert_field_value

    Create Specification Field Value
    """
    body = {"FieldId":34,"FieldValueId":143,"IsActive":True,"Name":"Cotton","Position":100,"Text":"Cotton fibers"}
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
        path='/api/catalog_system/pvt/specification/fieldValue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_update_field_value(client):
    """Test case for specifications_update_field_value

    Update Specification Field Value
    """
    body = {"FieldId":1,"FieldValueId":143,"IsActive":True,"Name":"Cotton","Position":100,"Text":"Cotton fibers"}
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
        path='/api/catalog_system/pvt/specification/fieldValue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_values_by_field_id(client):
    """Test case for specifications_values_by_field_id

    Get Specification Values By Field ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/specification/fieldvalue/{field_id}'.format(field_id=34),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

