# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_flow_revision_response import ListFlowRevisionResponse
from openapi_server.models.studio_v2_flow_flow_revision import StudioV2FlowFlowRevision


pytestmark = pytest.mark.asyncio

async def test_fetch_flow_revision(client):
    """Test case for fetch_flow_revision

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Flows/{sid}/Revisions/{revision}'.format(sid='sid_example', revision='revision_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_flow_revision(client):
    """Test case for list_flow_revision

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Flows/{sid}/Revisions'.format(sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

