# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.funding_account_response_v2 import FundingAccountResponseV2
from openapi_server.models.funding_request_v2 import FundingRequestV2
from openapi_server.models.funding_request_v3 import FundingRequestV3
from openapi_server.models.funding_response import FundingResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_funding_accounts_response_v2 import ListFundingAccountsResponseV2
from openapi_server.models.page_resource_funding_payor_status_audit_response_funding_payor_status_audit_response import PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse


pytestmark = pytest.mark.asyncio

async def test_create_funding_request_v2(client):
    """Test case for create_funding_request_v2

    Create Funding Request
    """
    body = {"amount":800828191}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/sourceAccounts/{source_account_id}/fundingRequest'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_funding_request_v3(client):
    """Test case for create_funding_request_v3

    Create Funding Request
    """
    body = {"amount":800828191,"fundingAccountId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/sourceAccounts/{source_account_id}/fundingRequest'.format(source_account_id='source_account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_funding_account_v2(client):
    """Test case for get_funding_account_v2

    Get Funding Account
    """
    params = [('sensitive', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/fundingAccounts/{funding_account_id}'.format(funding_account_id='funding_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_funding_accounts_v2(client):
    """Test case for get_funding_accounts_v2

    Get Funding Accounts
    """
    params = [('payorId', 'payor_id_example'),
                    ('name', 'name_example'),
                    ('country', 'US'),
                    ('currency', 'USD'),
                    ('type', 'type_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'accountName:asc'),
                    ('sensitive', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/fundingAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_funding_by_id_v1(client):
    """Test case for get_funding_by_id_v1

    Get Funding
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/fundings/{funding_id}'.format(funding_id='funding_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_funding_audit_deltas(client):
    """Test case for list_funding_audit_deltas

    Get Funding Audit Delta
    """
    params = [('payorId', 'payor_id_example'),
                    ('updatedSince', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/deltas/fundings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

