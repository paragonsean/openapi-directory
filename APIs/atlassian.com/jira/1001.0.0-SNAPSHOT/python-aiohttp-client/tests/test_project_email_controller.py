# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.project_email_address import ProjectEmailAddress


pytestmark = pytest.mark.asyncio

async def test_get_project_email(client):
    """Test case for get_project_email

    Get project's sender email
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id}/email'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_email(client):
    """Test case for update_project_email

    Set project's sender email
    """
    body = {"emailAddress":"emailAddress","emailAddressStatus":["emailAddressStatus","emailAddressStatus"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id}/email'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

