# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.azure_firewall_fqdn_tag_list_result import AzureFirewallFqdnTagListResult


pytestmark = pytest.mark.asyncio

async def test_azure_firewall_fqdn_tags_list_all(client):
    """Test case for azure_firewall_fqdn_tags_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/azureFirewallFqdnTags'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

