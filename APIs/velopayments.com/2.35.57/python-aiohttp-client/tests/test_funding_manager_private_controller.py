# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_funding_account_request_v2 import CreateFundingAccountRequestV2
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409


pytestmark = pytest.mark.asyncio

async def test_create_funding_account_v2(client):
    """Test case for create_funding_account_v2

    Create Funding Account
    """
    body = {"accountName":"accountName","accountNumber":"accountNumber","currency":"USD","name":"name","payorId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","routingNumber":"routingNumber","type":"FBO"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/fundingAccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_source_account_v3(client):
    """Test case for delete_source_account_v3

    Delete a source account by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/sourceAccounts/{source_account_id}'.format(source_account_id='source_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

