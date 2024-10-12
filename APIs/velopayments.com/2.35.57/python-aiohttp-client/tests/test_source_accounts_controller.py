# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_source_account_response_v2 import ListSourceAccountResponseV2
from openapi_server.models.list_source_account_response_v3 import ListSourceAccountResponseV3
from openapi_server.models.set_notifications_request import SetNotificationsRequest
from openapi_server.models.set_notifications_request2 import SetNotificationsRequest2
from openapi_server.models.source_account_response_v2 import SourceAccountResponseV2
from openapi_server.models.source_account_response_v3 import SourceAccountResponseV3
from openapi_server.models.transfer_request_v2 import TransferRequestV2
from openapi_server.models.transfer_request_v3 import TransferRequestV3


pytestmark = pytest.mark.asyncio

async def test_get_source_account_v2(client):
    """Test case for get_source_account_v2

    Get Source Account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/sourceAccounts/{source_account_id}'.format(source_account_id='source_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_account_v3(client):
    """Test case for get_source_account_v3

    Get details about given source account.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/sourceAccounts/{source_account_id}'.format(source_account_id='source_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_accounts_v2(client):
    """Test case for get_source_accounts_v2

    Get list of source accounts
    """
    params = [('physicalAccountName', 'physical_account_name_example'),
                    ('physicalAccountId', 'physical_account_id_example'),
                    ('payorId', 'payor_id_example'),
                    ('fundingAccountId', 'funding_account_id_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'fundingRef:asc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/sourceAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_accounts_v3(client):
    """Test case for get_source_accounts_v3

    Get list of source accounts
    """
    params = [('physicalAccountName', 'physical_account_name_example'),
                    ('physicalAccountId', 'physical_account_id_example'),
                    ('payorId', 'payor_id_example'),
                    ('fundingAccountId', 'funding_account_id_example'),
                    ('includeUserDeleted', True),
                    ('type', 'type_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'fundingRef:asc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/sourceAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_notifications_request(client):
    """Test case for set_notifications_request

    Set notifications
    """
    body = {"minimumBalance":800828190}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/sourceAccounts/{source_account_id}/notifications'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_notifications_request_v3(client):
    """Test case for set_notifications_request_v3

    Set notifications
    """
    body = openapi_server.SetNotificationsRequest2()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/sourceAccounts/{source_account_id}/notifications'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer_funds_v2(client):
    """Test case for transfer_funds_v2

    Transfer Funds between source accounts
    """
    body = {"amount":800828191,"currency":"USD","toSourceAccountId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/sourceAccounts/{source_account_id}/transfers'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer_funds_v3(client):
    """Test case for transfer_funds_v3

    Transfer Funds between source accounts
    """
    body = {"amount":800828191,"currency":"USD","toSourceAccountId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/sourceAccounts/{source_account_id}/transfers'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

