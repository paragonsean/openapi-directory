# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization import Authorization
from openapi_server.models.authorization_post_request import AuthorizationPostRequest
from openapi_server.models.authorization_update_request import AuthorizationUpdateRequest
from openapi_server.models.authorizations import Authorizations
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_delete_authorizations_id(client):
    """Test case for delete_authorizations_id

    Delete an authorization
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/authorizations/{auth_id}'.format(auth_id='auth_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authorizations(client):
    """Test case for get_authorizations

    List all authorizations
    """
    params = [('userID', 'user_id_example'),
                    ('user', 'user_example'),
                    ('orgID', 'org_id_example'),
                    ('org', 'org_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/authorizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authorizations_id(client):
    """Test case for get_authorizations_id

    Retrieve an authorization
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/authorizations/{auth_id}'.format(auth_id='auth_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_authorizations_id(client):
    """Test case for patch_authorizations_id

    Update an authorization to be active or inactive
    """
    body = {"description":"description","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/authorizations/{auth_id}'.format(auth_id='auth_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authorizations(client):
    """Test case for post_authorizations

    Create an authorization
    """
    body = {"permissions":[{"resource":{"org":"org","name":"name","id":"id","type":"authorizations","orgID":"orgID"},"action":"read"},{"resource":{"org":"org","name":"name","id":"id","type":"authorizations","orgID":"orgID"},"action":"read"}],"description":"description","userID":"userID","orgID":"orgID","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/authorizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

