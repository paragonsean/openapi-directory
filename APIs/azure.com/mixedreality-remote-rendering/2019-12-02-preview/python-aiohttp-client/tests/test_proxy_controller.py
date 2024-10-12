# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.remote_rendering_account_page import RemoteRenderingAccountPage
from openapi_server.models.remote_rendering_accounts_list_by_subscription_default_response import RemoteRenderingAccountsListBySubscriptionDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_remote_rendering_accounts_list_by_subscription_0(client):
    """Test case for remote_rendering_accounts_list_by_subscription_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MixedReality/remoteRenderingAccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

