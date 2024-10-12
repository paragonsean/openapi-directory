# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_invoice_comment_interface import SalesDataInvoiceCommentInterface
from openapi_server.models.sales_invoice_comment_repository_v1_save_post_request import SalesInvoiceCommentRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_invoice_comment_repository_v1_save_post(client):
    """Test case for sales_invoice_comment_repository_v1_save_post

    invoices/comments
    """
    body = openapi_server.SalesInvoiceCommentRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/invoices/comments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

