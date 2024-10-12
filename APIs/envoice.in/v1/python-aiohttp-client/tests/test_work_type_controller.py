# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.work_type_create_api_model import WorkTypeCreateApiModel
from openapi_server.models.work_type_delete_api_model import WorkTypeDeleteApiModel
from openapi_server.models.work_type_details_api_model import WorkTypeDetailsApiModel
from openapi_server.models.work_type_update_api_model import WorkTypeUpdateApiModel


pytestmark = pytest.mark.asyncio

async def test_work_type_api_all(client):
    """Test case for work_type_api_all

    Return all work types for the account
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/worktype/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_work_type_api_delete(client):
    """Test case for work_type_api_delete

    Delete an existing work type
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/worktype/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_type_api_details(client):
    """Test case for work_type_api_details

    Return work type details
    """
    params = [('workTypeId', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/worktype/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_work_type_api_new(client):
    """Test case for work_type_api_new

    Create a work type
    """
    body = {"Title":"Title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/worktype/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_type_api_search(client):
    """Test case for work_type_api_search

    Return all work types for the account that match the query param
    """
    params = [('queryOptions.query', 'query_options_query_example'),
                    ('queryOptions.orderBy', 'query_options_order_by_example'),
                    ('queryOptions.order', 'query_options_order_example'),
                    ('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/worktype/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_work_type_api_update(client):
    """Test case for work_type_api_update

    Update an existing work type
    """
    body = {"Title":"Title","Id":0}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/worktype/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

