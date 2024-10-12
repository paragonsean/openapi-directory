# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_status_history_search_result_interface import SalesDataOrderStatusHistorySearchResultInterface
from openapi_server.models.sales_order_management_v1_add_comment_post_request import SalesOrderManagementV1AddCommentPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_order_management_v1_add_comment_post(client):
    """Test case for sales_order_management_v1_add_comment_post

    orders/{id}/comments
    """
    body = openapi_server.SalesOrderManagementV1AddCommentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/orders/{id}/comments'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_order_management_v1_get_comments_list_get(client):
    """Test case for sales_order_management_v1_get_comments_list_get

    orders/{id}/comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/orders/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

