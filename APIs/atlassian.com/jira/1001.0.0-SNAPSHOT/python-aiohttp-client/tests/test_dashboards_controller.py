# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_dashboard_gadgets_response import AvailableDashboardGadgetsResponse
from openapi_server.models.dashboard import Dashboard
from openapi_server.models.dashboard_details import DashboardDetails
from openapi_server.models.dashboard_gadget import DashboardGadget
from openapi_server.models.dashboard_gadget_response import DashboardGadgetResponse
from openapi_server.models.dashboard_gadget_settings import DashboardGadgetSettings
from openapi_server.models.dashboard_gadget_update_request import DashboardGadgetUpdateRequest
from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_dashboard import PageBeanDashboard
from openapi_server.models.page_of_dashboards import PageOfDashboards
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_add_gadget(client):
    """Test case for add_gadget

    Add gadget to dashboard
    """
    body = {"color":"color","ignoreUriAndModuleKeyValidation":True,"position":"","title":"title","uri":"uri","moduleKey":"moduleKey"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/dashboard/{dashboard_id}/gadget'.format(dashboard_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_dashboard(client):
    """Test case for copy_dashboard

    Copy dashboard
    """
    body = {"editPermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}],"name":"name","description":"description","sharePermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/dashboard/{id}/copy'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_dashboard(client):
    """Test case for create_dashboard

    Create dashboard
    """
    body = {"editPermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}],"name":"name","description":"description","sharePermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/dashboard',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboard(client):
    """Test case for delete_dashboard

    Delete dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/dashboard/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dashboard_item_property(client):
    """Test case for delete_dashboard_item_property

    Delete dashboard item property
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(dashboard_id='dashboard_id_example', item_id='item_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_available_dashboard_gadgets(client):
    """Test case for get_all_available_dashboard_gadgets

    Get available gadgets
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/gadgets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_dashboards(client):
    """Test case for get_all_dashboards

    Get all dashboards
    """
    params = [('filter', 'filter_example'),
                    ('startAt', 0),
                    ('maxResults', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_gadgets(client):
    """Test case for get_all_gadgets

    Get gadgets
    """
    params = [('moduleKey', ['module_key_example']),
                    ('uri', ['uri_example']),
                    ('gadgetId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/{dashboard_id}/gadget'.format(dashboard_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard(client):
    """Test case for get_dashboard

    Get dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard_item_property(client):
    """Test case for get_dashboard_item_property

    Get dashboard item property
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(dashboard_id='dashboard_id_example', item_id='item_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard_item_property_keys(client):
    """Test case for get_dashboard_item_property_keys

    Get dashboard item property keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties'.format(dashboard_id='dashboard_id_example', item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboards_paginated(client):
    """Test case for get_dashboards_paginated

    Search for dashboards
    """
    params = [('dashboardName', 'dashboard_name_example'),
                    ('accountId', 'account_id_example'),
                    ('owner', 'owner_example'),
                    ('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('projectId', 56),
                    ('orderBy', name),
                    ('startAt', 0),
                    ('maxResults', 50),
                    ('status', active),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/dashboard/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_gadget(client):
    """Test case for remove_gadget

    Remove gadget from dashboard
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}'.format(dashboard_id=56, gadget_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_dashboard_item_property(client):
    """Test case for set_dashboard_item_property

    Set dashboard item property
    """
    body = {"number":5,"string":"string-value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(dashboard_id='dashboard_id_example', item_id='item_id_example', property_key='property_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dashboard(client):
    """Test case for update_dashboard

    Update dashboard
    """
    body = {"editPermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}],"name":"name","description":"description","sharePermissions":[{"role":"","project":"","id":6,"type":"user","user":"","group":""},{"role":"","project":"","id":6,"type":"user","user":"","group":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/dashboard/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_gadget(client):
    """Test case for update_gadget

    Update gadget on dashboard
    """
    body = {"color":"color","position":"","title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}'.format(dashboard_id=56, gadget_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

