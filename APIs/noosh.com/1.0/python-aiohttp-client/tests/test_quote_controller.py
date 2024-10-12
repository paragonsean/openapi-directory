# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.object_state_list_vo import ObjectStateListVO
from openapi_server.models.quote_expand_vo import QuoteExpandVO
from openapi_server.models.quote_list_vo import QuoteListVO
from openapi_server.models.quote_of_wg_level_simple_vo import QuoteOfWgLevelSimpleVO
from openapi_server.models.quote_put_persist_vo import QuotePutPersistVO


pytestmark = pytest.mark.asyncio

async def test_get_quote(client):
    """Test case for get_quote

    Get a specific quote of project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_list(client):
    """Test case for get_quote_list

    List the quotes
    """
    params = [('quote_state_id, use filters&#x3D;{&quot;quote_state_id&quot;:111111}', 'quote_state_id_use_filtersquote_state_id111111_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/quotes'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_state_list(client):
    """Test case for get_quote_state_list

    List the quote states
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/quoteStates'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_quote(client):
    """Test case for put_quote

    Accept / Reject a Quote
    """
    body = {"po_number":"sample po_number","state_change_comments":"sample state_change_comments","quote_id":1,"action":"sample action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_workgroups_workgroup_id_quotes_get(client):
    """Test case for v1_workgroups_workgroup_id_quotes_get

    List the quotes of workgroup level
    """
    params = [('quote_state_id, use filters&#x3D;{&quot;quote_state_id&quot;:111111}', 'quote_state_id_use_filtersquote_state_id111111_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/quotes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

