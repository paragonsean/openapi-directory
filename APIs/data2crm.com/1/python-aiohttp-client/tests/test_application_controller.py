# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_entity import ApplicationEntity
from openapi_server.models.application_entity_list import ApplicationEntityList
from openapi_server.models.application_entity_relation import ApplicationEntityRelation
from openapi_server.models.application_entity_write import ApplicationEntityWrite
from openapi_server.models.count import Count


pytestmark = pytest.mark.asyncio

async def test_create_application_entity(client):
    """Test case for create_application_entity

    POST for application
    """
    body = {"authorization":"authorization","credential":"{}","description":"description","type":"Bitrix24"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='POST',
        path='/v1/application',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application_entity(client):
    """Test case for delete_application_entity

    DELETE for application
    """
    headers = { 
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/application/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_collection(client):
    """Test case for get_application_collection

    GET for application
    """
    params = [('page_size', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('fields', 'fields_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_count_collection(client):
    """Test case for get_application_count_collection

    COUNT for application
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_entity(client):
    """Test case for get_application_entity

    GET for application
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/application/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_application_entity(client):
    """Test case for update_application_entity

    PUT for application
    """
    body = {"authorization":"authorization","credential":"{}","description":"description","type":"Bitrix24"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='PUT',
        path='/v1/application/{key}'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

