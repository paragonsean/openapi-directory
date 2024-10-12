# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface


pytestmark = pytest.mark.asyncio

async def test_sales_creditmemo_management_v1_cancel_put(client):
    """Test case for sales_creditmemo_management_v1_cancel_put

    creditmemo/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/creditmemo/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_creditmemo_repository_v1_get_get(client):
    """Test case for sales_creditmemo_repository_v1_get_get

    creditmemo/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/creditmemo/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

