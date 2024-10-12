# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_creditmemo_comment_repository_v1_save_post_request import SalesCreditmemoCommentRepositoryV1SavePostRequest
from openapi_server.models.sales_data_creditmemo_comment_interface import SalesDataCreditmemoCommentInterface
from openapi_server.models.sales_data_creditmemo_comment_search_result_interface import SalesDataCreditmemoCommentSearchResultInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_creditmemo_comment_repository_v1_save_post(client):
    """Test case for sales_creditmemo_comment_repository_v1_save_post

    creditmemo/{id}/comments
    """
    body = openapi_server.SalesCreditmemoCommentRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/creditmemo/{id}/comments'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_creditmemo_management_v1_get_comments_list_get(client):
    """Test case for sales_creditmemo_management_v1_get_comments_list_get

    creditmemo/{id}/comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/creditmemo/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

