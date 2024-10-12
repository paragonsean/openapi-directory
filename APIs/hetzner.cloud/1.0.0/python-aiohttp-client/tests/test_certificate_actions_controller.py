# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse


pytestmark = pytest.mark.asyncio

async def test_certificates_id_actions_action_id_get(client):
    """Test case for certificates_id_actions_action_id_get

    Get an Action for a Certificate
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_id_actions_get(client):
    """Test case for certificates_id_actions_get

    Get all Actions for a Certificate
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/certificates/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_id_actions_retry_post(client):
    """Test case for certificates_id_actions_retry_post

    Retry Issuance or Renewal
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/certificates/{id}/actions/retry'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

