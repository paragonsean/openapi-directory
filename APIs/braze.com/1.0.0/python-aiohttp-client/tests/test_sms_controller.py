# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_users_subscription_group_sms_0(client):
    """Test case for list_users_subscription_group_sms_0

    List User's Subscription Group - SMS
    """
    params = [('external_id', '{{external_id}}'),
                    ('limit', '100'),
                    ('offset', '1'),
                    ('phone', '+11112223333')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/subscription/user/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_users_subscription_group_status_sms_0(client):
    """Test case for list_users_subscription_group_status_sms_0

    List User's  Subscription Group Status - SMS
    """
    params = [('subscription_group_id', '{{subscription_group_id}}'),
                    ('external_id', '{{external_identifier}}'),
                    ('phone', '+11112223333')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/subscription/status/get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

