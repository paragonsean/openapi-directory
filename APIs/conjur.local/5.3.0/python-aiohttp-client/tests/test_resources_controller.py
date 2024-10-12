# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.show_resources_for_all_accounts200_response_inner import ShowResourcesForAllAccounts200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_show_resource(client):
    """Test case for show_resource

    Shows a description of a single resource.
    """
    params = [('permitted_roles', true),
                    ('privilege', 'execute'),
                    ('check', true),
                    ('role', 'myorg:host:host1')]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources/{account}/{kind}/{identifier}'.format(account='account_example', kind='user', identifier='conjur/authn-iam/test'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_resources_for_account(client):
    """Test case for show_resources_for_account

    Lists resources within an organization account.
    """
    params = [('kind', 'user'),
                    ('search', openapi_server.ERRORUNKNOWN()),
                    ('offset', 56),
                    ('limit', 56),
                    ('count', True),
                    ('role', 'myorg:host:host1'),
                    ('acting_as', 'myorg:host:host1')]
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources/{account}'.format(account='account_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_resources_for_all_accounts(client):
    """Test case for show_resources_for_all_accounts

    Lists resources within an organization account.
    """
    params = [('account', 'myorg'),
                    ('kind', 'user'),
                    ('search', 'db'),
                    ('offset', 56),
                    ('limit', 56),
                    ('count', True),
                    ('role', 'myorg:host:host1'),
                    ('acting_as', 'myorg:host:host1')]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_resources_for_kind(client):
    """Test case for show_resources_for_kind

    Lists resources of the same kind within an organization account.
    """
    params = [('search', openapi_server.ERRORUNKNOWN()),
                    ('offset', 56),
                    ('limit', 56),
                    ('count', True),
                    ('role', 'myorg:host:host1'),
                    ('acting_as', 'myorg:host:host1')]
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/resources/{account}/{kind}'.format(account='account_example', kind='user'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

