# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.requisition_list_data_requisition_list_interface import RequisitionListDataRequisitionListInterface
from openapi_server.models.requisition_list_requisition_list_repository_v1_save_post_request import RequisitionListRequisitionListRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_requisition_list_requisition_list_repository_v1_save_post(client):
    """Test case for requisition_list_requisition_list_repository_v1_save_post

    requisition_lists
    """
    body = openapi_server.RequisitionListRequisitionListRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/requisition_lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

