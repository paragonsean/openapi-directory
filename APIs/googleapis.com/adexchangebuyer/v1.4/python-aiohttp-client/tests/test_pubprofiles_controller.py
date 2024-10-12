# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_publisher_profiles_by_account_id_response import GetPublisherProfilesByAccountIdResponse


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_pubprofiles_list(client):
    """Test case for adexchangebuyer_pubprofiles_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/publisher/{account_id}/profiles'.format(account_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

