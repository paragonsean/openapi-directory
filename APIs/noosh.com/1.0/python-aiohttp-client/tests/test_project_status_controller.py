# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_status_list_vo import ProjectStatusListVO


pytestmark = pytest.mark.asyncio

async def test_get_project_status(client):
    """Test case for get_project_status

    List the project status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projectStatus'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_status_of_client(client):
    """Test case for get_project_status_of_client

    List the project status of client
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectStatus'.format(workgroup_id='workgroup_id_example', client_workgroup_id='client_workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

