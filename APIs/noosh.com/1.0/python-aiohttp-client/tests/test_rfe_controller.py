# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.rfe_expand_vo import RfeExpandVO
from openapi_server.models.rfe_list_vo import RfeListVO
from openapi_server.models.rfe_po import RfePO
from openapi_server.models.rfq_vo import RfqVO


pytestmark = pytest.mark.asyncio

async def test_get_rfe(client):
    """Test case for get_rfe

    Get a specific Rfe
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes/{rfe_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', rfe_id='rfe_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rfe_list(client):
    """Test case for get_rfe_list

    List the RFES
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_rfe(client):
    """Test case for post_rfe

    Create a RFE
    """
    body = {"specs":[{"quantity_5":1,"quantity_4":1,"spec_id":1,"quantity_1":1,"quantity_3":1,"quantity_2":1},{"quantity_5":1,"quantity_4":1,"spec_id":1,"quantity_1":1,"quantity_3":1,"quantity_2":1}],"proposed_order_completion_date":"2000-01-23","description":"sample description","details":"sample details","estimate_due_date":"2000-01-23","rfe_title":"sample rfe_title","supplier_user_ids":[1,1],"rfe_number":"sample rfe_number"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/rfes'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

