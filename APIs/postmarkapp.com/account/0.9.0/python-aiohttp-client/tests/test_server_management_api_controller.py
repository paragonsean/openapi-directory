# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_server_payload import CreateServerPayload
from openapi_server.models.edit_server_payload import EditServerPayload
from openapi_server.models.extended_server_info import ExtendedServerInfo
from openapi_server.models.server_listing_response import ServerListingResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_create_server(client):
    """Test case for create_server

    Create a Server
    """
    body = {"ClickHookUrl":"ClickHookUrl","Color":"Color","DeliveryHookUrl":"DeliveryHookUrl","RawEmailEnabled":True,"TrackLinks":"None","InboundSpamThreshold":0,"OpenHookUrl":"OpenHookUrl","BounceHookUrl":"BounceHookUrl","InboundHookUrl":"InboundHookUrl","Name":"Name","TrackOpens":True,"PostFirstOpenOnly":True,"InboundDomain":"InboundDomain","SmtpApiActivated":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='POST',
        path='/servers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_server(client):
    """Test case for delete_server

    Delete a Server
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}'.format(serverid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_server_information(client):
    """Test case for edit_server_information

    Edit a Server
    """
    body = {"ClickHookUrl":"ClickHookUrl","Color":"Color","DeliveryHookUrl":"DeliveryHookUrl","RawEmailEnabled":True,"TrackLinks":"None","InboundSpamThreshold":0,"OpenHookUrl":"OpenHookUrl","BounceHookUrl":"BounceHookUrl","InboundHookUrl":"InboundHookUrl","Name":"Name","TrackOpens":True,"PostFirstOpenOnly":True,"InboundDomain":"InboundDomain","SmtpApiActivated":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}'.format(serverid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_information(client):
    """Test case for get_server_information

    Get a Server
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}'.format(serverid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_servers(client):
    """Test case for list_servers

    List servers
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_account_token': 'x_postmark_account_token_example',
    }
    response = await client.request(
        method='GET',
        path='/servers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

