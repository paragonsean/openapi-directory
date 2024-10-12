# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add_member_to_role(client):
    """Test case for add_member_to_role

    Update or modify an existing role membership
    """
    params = [('members', 'members_example'),
                    ('member', 'member_example')]
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/roles/{account}/{kind}/{identifier}'.format(account='account_example', kind='user', identifier='admin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_member_from_role(client):
    """Test case for remove_member_from_role

    Deletes an existing role membership
    """
    params = [('members', 'members_example'),
                    ('member', 'member_example')]
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/roles/{account}/{kind}/{identifier}'.format(account='account_example', kind='user', identifier='admin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_role(client):
    """Test case for show_role

    Get role information
    """
    params = [('all', 'all_example'),
                    ('memberships', 'memberships_example'),
                    ('members', 'members_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('count', True),
                    ('search', 'user'),
                    ('graph', '')]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/roles/{account}/{kind}/{identifier}'.format(account='account_example', kind='user', identifier='admin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

