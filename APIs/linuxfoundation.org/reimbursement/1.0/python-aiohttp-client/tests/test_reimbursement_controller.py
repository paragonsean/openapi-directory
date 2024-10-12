# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_reimbursement_request import CreateReimbursementRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.policy_update_input import PolicyUpdateInput


pytestmark = pytest.mark.asyncio

async def test_create_reimbursement(client):
    """Test case for create_reimbursement

    Create Reimbursement
    """
    body = openapi_server.CreateReimbursementRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/reimbursement/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_reimbursement(client):
    """Test case for update_reimbursement

    Update Reimbursement
    """
    body = openapi_server.PolicyUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/reimbursement/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

