# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_query_hard_bounced_emails(client):
    """Test case for query_hard_bounced_emails

    Query Hard Bounced Emails
    """
    params = [('start_date', '2019-01-01'),
                    ('end_date', '2019-02-01'),
                    ('limit', '100'),
                    ('offset', '1'),
                    ('email', 'example@braze.com')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/email/hard_bounces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_list_of_unsubscribed_email_addresses(client):
    """Test case for query_list_of_unsubscribed_email_addresses

    Query List of Unsubscribed Email Addresses
    """
    params = [('start_date', '2020-01-01'),
                    ('end_date', '2020-02-01'),
                    ('limit', '1'),
                    ('offset', '1'),
                    ('sort_direction', 'desc'),
                    ('email', 'example@braze.com')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/email/unsubscribes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

