# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_directive200_response import CheckDirective200Response
from openapi_server.models.create_directive200_response import CreateDirective200Response
from openapi_server.models.delete_directive200_response import DeleteDirective200Response
from openapi_server.models.directive import Directive
from openapi_server.models.directive_details200_response import DirectiveDetails200Response
from openapi_server.models.directive_new import DirectiveNew
from openapi_server.models.list_directives200_response import ListDirectives200Response
from openapi_server.models.update_directive200_response import UpdateDirective200Response


pytestmark = pytest.mark.asyncio

async def test_check_directive(client):
    """Test case for check_directive

    Check that update on a directive is valid
    """
    body = openapi_server.Directive()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/directives/{directive_id}/check'.format(directive_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_directive(client):
    """Test case for create_directive

    Create a directive
    """
    body = openapi_server.DirectiveNew()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/directives',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_directive(client):
    """Test case for delete_directive

    Delete a directive
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/directives/{directive_id}'.format(directive_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directive_details(client):
    """Test case for directive_details

    Get directive details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/directives/{directive_id}'.format(directive_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_directives(client):
    """Test case for list_directives

    List all directives
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/directives',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_directive(client):
    """Test case for update_directive

    Update a directive details
    """
    body = openapi_server.Directive()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/directives/{directive_id}'.format(directive_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

