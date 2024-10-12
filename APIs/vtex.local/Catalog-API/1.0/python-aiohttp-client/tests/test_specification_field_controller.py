# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.specifications_field200_response import SpecificationsField200Response
from openapi_server.models.specifications_insert_field_request import SpecificationsInsertFieldRequest
from openapi_server.models.specifications_insert_field_update_request import SpecificationsInsertFieldUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_specifications_field(client):
    """Test case for specifications_field

    Get Specification Field
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
        path='/api/catalog_system/pub/specification/fieldGet/{field_id}'.format(field_id=88),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_insert_field(client):
    """Test case for specifications_insert_field

    Create Specification Field
    """
    body = {"CategoryId":4,"DefaultValue":null,"Description":"Composition of the product.","FieldGroupId":20,"FieldGroupName":"Clothes specifications","FieldId":88,"FieldTypeId":1,"FieldValueId":1,"IsActive":True,"IsFilter":True,"IsOnProductDetails":False,"IsRequired":True,"IsSideMenuLinkActive":True,"IsStockKeepingUnit":False,"IsTopMenuLinkActive":True,"IsWizard":False,"Name":"Material","Position":1}
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
        path='/api/catalog_system/pvt/specification/field',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_insert_field_update(client):
    """Test case for specifications_insert_field_update

    Update Specification Field
    """
    body = {"CategoryId":0,"IsTopMenuLinkActive":True,"Description":"Description","FieldGroupId":6,"FieldTypeId":5,"IsOnProductDetails":True,"IsSideMenuLinkActive":False,"Position":2,"IsActive":True,"FieldValueId":5,"IsWizard":True,"Name":"Name","DefaultValue":"DefaultValue","IsFilter":True,"IsRequired":True,"FieldId":1,"IsStockKeepingUnit":True,"FieldGroupName":"FieldGroupName"}
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
        path='/api/catalog_system/pvt/specification/field',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

