# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_list_node_agent_skus_result import AccountListNodeAgentSkusResult
from openapi_server.models.batch_error import BatchError
from openapi_server.models.pool_node_counts_list_result import PoolNodeCountsListResult


pytestmark = pytest.mark.asyncio

async def test_account_list_node_agent_skus(client):
    """Test case for account_list_node_agent_skus

    Lists all node agent SKUs supported by the Azure Batch service.
    """
    params = [('$filter', 'filter_example'),
                    ('maxresults', 1000),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/nodeagentskus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_list_pool_node_counts(client):
    """Test case for account_list_pool_node_counts

    
    """
    params = [('$filter', 'filter_example'),
                    ('maxresults', 10),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/nodecounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

