# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specificationgroup_group_id_put200_response import ApiCatalogPvtSpecificationgroupGroupIdPut200Response
from openapi_server.models.request_body8 import RequestBody8
from openapi_server.models.specification_group_insert2200_response import SpecificationGroupInsert2200Response
from openapi_server.models.specification_group_insert_request import SpecificationGroupInsertRequest
from openapi_server.models.specifications_group import SpecificationsGroup


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_specificationgroup_group_id_put(client):
    """Test case for api_catalog_pvt_specificationgroup_group_id_put

    Update Specification Group
    """
    body = openapi_server.RequestBody8()
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
        path='/api/catalog/pvt/specificationgroup/{group_id}'.format(group_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specification_group_insert2(client):
    """Test case for specification_group_insert2

    Create Specification Group
    """
    body = {"CategoryId":1,"Name":"GroupName1"}
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
        path='/api/catalog/pvt/specificationgroup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_group_get(client):
    """Test case for specifications_group_get

    Get Specification Group
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
        path='/api/catalog_system/pub/specification/groupGet/{group_id}'.format(group_id='6'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_group_listby_category(client):
    """Test case for specifications_group_listby_category

    List Specification Group by Category
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
        path='/api/catalog_system/pvt/specification/groupbycategory/{category_id}'.format(category_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

