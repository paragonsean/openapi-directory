# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.internal_user_entity import InternalUserEntity
from openapi_server.models.internal_user_entity_relation import InternalUserEntityRelation


pytestmark = pytest.mark.asyncio

async def test_create_internal_user_entity(client):
    """Test case for create_internal_user_entity

    POST for internalUser
    """
    body = {"last_used_at":"2000-01-23T04:56:07.000+00:00","updated_at":"2000-01-23T04:56:07.000+00:00","internal_request_count":0,"phone":"(817) 569-8900","organization":"M&M","roles":["roles","roles"],"name":"Bill Wall","created_at":"2000-01-23T04:56:07.000+00:00","email":"bill.wall@mail.com","key":"21312411","request_count":6,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='POST',
        path='/v1/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_internal_user_entity(client):
    """Test case for delete_internal_user_entity

    DELETE for internalUser
    """
    headers = { 
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/user/{internal_user_id}'.format(internal_user_id='internal_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_internal_user_collection(client):
    """Test case for get_internal_user_collection

    GET for internalUser
    """
    params = [('page_size', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('fields', 'fields_example'),
                    ('sort', 'sort_example'),
                    ('application_request_start', '2013-10-20'),
                    ('application_request_end', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_internal_user_count_collection(client):
    """Test case for get_internal_user_count_collection

    COUNT for internalUser
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_internal_user_entity(client):
    """Test case for get_internal_user_entity

    GET for internalUser
    """
    params = [('fields', 'fields_example'),
                    ('application_request_start', '2013-10-20'),
                    ('application_request_end', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='GET',
        path='/v1/user/{internal_user_id}'.format(internal_user_id='internal_user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_internal_user_entity(client):
    """Test case for update_internal_user_entity

    PUT for internalUser
    """
    body = {"last_used_at":"2000-01-23T04:56:07.000+00:00","updated_at":"2000-01-23T04:56:07.000+00:00","internal_request_count":0,"phone":"(817) 569-8900","organization":"M&M","roles":["roles","roles"],"name":"Bill Wall","created_at":"2000-01-23T04:56:07.000+00:00","email":"bill.wall@mail.com","key":"21312411","request_count":6,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api2_crm_user_key': 'e2a6379ab878ae7e58119d4ec842bf9c',
    }
    response = await client.request(
        method='PUT',
        path='/v1/user/{internal_user_id}'.format(internal_user_id='internal_user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

