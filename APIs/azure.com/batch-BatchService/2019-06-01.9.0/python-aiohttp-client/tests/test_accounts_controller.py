# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_list_supported_images_result import AccountListSupportedImagesResult
from openapi_server.models.batch_error import BatchError
from openapi_server.models.pool_node_counts_list_result import PoolNodeCountsListResult


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
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/nodecounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_list_supported_images(client):
    """Test case for account_list_supported_images

    Lists all Virtual Machine Images supported by the Azure Batch service.
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
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/supportedimages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

