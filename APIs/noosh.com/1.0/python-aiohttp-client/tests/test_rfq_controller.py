# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.rfq_expand_vo import RfqExpandVO
from openapi_server.models.rfq_list_vo import RfqListVO


pytestmark = pytest.mark.asyncio

async def test_get_rfq(client):
    """Test case for get_rfq

    Get a specific Rfq
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs/{rfq_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', rfq_id='rfq_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rfq_list(client):
    """Test case for get_rfq_list

    List the rfqs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

