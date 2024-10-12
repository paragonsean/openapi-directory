# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_shipment_comment_interface import SalesDataShipmentCommentInterface
from openapi_server.models.sales_data_shipment_comment_search_result_interface import SalesDataShipmentCommentSearchResultInterface
from openapi_server.models.sales_shipment_comment_repository_v1_save_post_request import SalesShipmentCommentRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_shipment_comment_repository_v1_save_post(client):
    """Test case for sales_shipment_comment_repository_v1_save_post

    shipment/{id}/comments
    """
    body = openapi_server.SalesShipmentCommentRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/shipment/{id}/comments'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_shipment_management_v1_get_comments_list_get(client):
    """Test case for sales_shipment_management_v1_get_comments_list_get

    shipment/{id}/comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/shipment/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

