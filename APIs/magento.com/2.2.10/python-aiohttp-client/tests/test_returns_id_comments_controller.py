# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_comment_management_v1_add_comment_post_request import RmaCommentManagementV1AddCommentPostRequest
from openapi_server.models.rma_data_comment_search_result_interface import RmaDataCommentSearchResultInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rma_comment_management_v1_add_comment_post(client):
    """Test case for rma_comment_management_v1_add_comment_post

    returns/{id}/comments
    """
    body = openapi_server.RmaCommentManagementV1AddCommentPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/returns/{id}/comments'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rma_comment_management_v1_comments_list_get(client):
    """Test case for rma_comment_management_v1_comments_list_get

    returns/{id}/comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/returns/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

