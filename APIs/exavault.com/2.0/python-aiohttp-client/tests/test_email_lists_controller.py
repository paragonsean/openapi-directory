# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_email_list_request_body import AddEmailListRequestBody
from openapi_server.models.email_list_collection_response import EmailListCollectionResponse
from openapi_server.models.email_list_response import EmailListResponse
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_email_list_request_body import UpdateEmailListRequestBody


pytestmark = pytest.mark.asyncio

async def test_add_email_list(client):
    """Test case for add_email_list

    Create new email list
    """
    body = {"emails":["johns@example.com","jdoe@example.com"],"name":"My friends list"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/email-lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_email_list_by_id(client):
    """Test case for delete_email_list_by_id

    Delete an email group with given id
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/email-lists/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_email_list_by_id(client):
    """Test case for get_email_list_by_id

    Get individual email group
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/email-lists/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_email_lists(client):
    """Test case for get_email_lists

    Get all email groups
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/email-lists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_email_list_by_id(client):
    """Test case for update_email_list_by_id

    Update an email group
    """
    body = {"emails":["yuk@example.com","jdoe@example.com"],"name":"My friends list"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/email-lists/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

