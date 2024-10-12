# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_ui_modification_details import CreateUiModificationDetails
from openapi_server.models.page_bean_ui_modification_details import PageBeanUiModificationDetails
from openapi_server.models.ui_modification_identifiers import UiModificationIdentifiers
from openapi_server.models.update_ui_modification_details import UpdateUiModificationDetails


pytestmark = pytest.mark.asyncio

async def test_create_ui_modification(client):
    """Test case for create_ui_modification

    Create UI modification
    """
    body = {"data":"data","name":"name","description":"description","contexts":[{"isAvailable":True,"issueTypeId":"issueTypeId","viewType":"viewType","id":"id","projectId":"projectId"},{"isAvailable":True,"issueTypeId":"issueTypeId","viewType":"viewType","id":"id","projectId":"projectId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/uiModifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ui_modification(client):
    """Test case for delete_ui_modification

    Delete UI modification
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/uiModifications/{ui_modification_id}'.format(ui_modification_id='ui_modification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ui_modifications(client):
    """Test case for get_ui_modifications

    Get UI modifications
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/uiModifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ui_modification(client):
    """Test case for update_ui_modification

    Update UI modification
    """
    body = {"data":"data","name":"name","description":"description","contexts":[{"isAvailable":True,"issueTypeId":"issueTypeId","viewType":"viewType","id":"id","projectId":"projectId"},{"isAvailable":True,"issueTypeId":"issueTypeId","viewType":"viewType","id":"id","projectId":"projectId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/uiModifications/{ui_modification_id}'.format(ui_modification_id='ui_modification_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

