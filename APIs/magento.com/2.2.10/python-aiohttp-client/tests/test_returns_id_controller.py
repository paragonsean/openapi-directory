# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rma_data_rma_interface import RmaDataRmaInterface
from openapi_server.models.rma_rma_management_v1_save_rma_post_request import RmaRmaManagementV1SaveRmaPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rma_rma_management_v1_save_rma_put(client):
    """Test case for rma_rma_management_v1_save_rma_put

    returns/{id}
    """
    body = openapi_server.RmaRmaManagementV1SaveRmaPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/returns/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rma_rma_repository_v1_delete_delete(client):
    """Test case for rma_rma_repository_v1_delete_delete

    returns/{id}
    """
    body = openapi_server.RmaRmaManagementV1SaveRmaPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/returns/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rma_rma_repository_v1_get_get(client):
    """Test case for rma_rma_repository_v1_get_get

    returns/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/returns/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

