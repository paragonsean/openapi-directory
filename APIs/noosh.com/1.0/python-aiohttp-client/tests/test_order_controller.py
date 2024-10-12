# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.order_detail_vo import OrderDetailVO
from openapi_server.models.order_detail_with_indicator_vo import OrderDetailWithIndicatorVO
from openapi_server.models.order_expand_workgroup_level_vo import OrderExpandWorkgroupLevelVO
from openapi_server.models.order_list_vo import OrderListVO
from openapi_server.models.order_po import OrderPO
from openapi_server.models.order_upd_persist_vo import OrderUpdPersistVO
from openapi_server.models.order_vo import OrderVO
from openapi_server.models.order_workgroup_level_list_vo import OrderWorkgroupLevelListVO


pytestmark = pytest.mark.asyncio

async def test_get_buy_order(client):
    """Test case for get_buy_order

    Get a specific buy order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buy_order_list(client):
    """Test case for get_buy_order_list

    List the buy orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buy_order_list_of_workgroup(client):
    """Test case for get_buy_order_list_of_workgroup

    List the buy orders of workgroup
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/buyOrders'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_buy_order_of_workgroup(client):
    """Test case for get_buy_order_of_workgroup

    Get a specific buy order of workgroup
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/buyOrders/{order_id}'.format(workgroup_id='workgroup_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    Get a specific buy/sell order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/orders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sell_order(client):
    """Test case for get_sell_order

    Get a specific sell order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sell_order_list(client):
    """Test case for get_sell_order_list

    List the sell orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sell_order_list_of_workgroup(client):
    """Test case for get_sell_order_list_of_workgroup

    List the sell orders of workgrop
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/sellOrders'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sell_order_of_workgroup(client):
    """Test case for get_sell_order_of_workgroup

    Get a specific sell order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/sellOrders/{order_id}'.format(workgroup_id='workgroup_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_buy_order(client):
    """Test case for post_buy_order

    Create a quick buy order
    """
    body = {"invoice_or_billing_recipient":1,"comments":"sample comments","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"tax":"sample tax","supplier_reference":"sample supplier_reference","buyer_user_id":1,"title":"sample title","payment_reference_no":"sample payment_reference_no","order_completion_date":"2000-01-23","payment_method_id":1,"sellOrder":False,"supplier_selection_reason_id":1,"shipping":"","other_selection_reason":"sample other_selection_reason","supplier_user_id":1,"order_items":[{"ex_tax_value_calculated":"","spec_reference_id":1,"notes":"sample notes","quantity":"","shipping":"","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"price":"","spec_id":1,"completion_date":"2000-01-23","tax":"sample tax","per":1},{"ex_tax_value_calculated":"","spec_reference_id":1,"notes":"sample notes","quantity":"","shipping":"","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"price":"","spec_id":1,"completion_date":"2000-01-23","tax":"sample tax","per":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_buy_order(client):
    """Test case for put_buy_order

    Update a specific buy order
    """
    body = {"comments":"sample comments","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"reject_reason":"sample reject_reason","payment_reference_no":"sample payment_reference_no","order_completion_date":"2000-01-23","payment_method_id":1,"unders_percent":"","overs_percent":"","supplier_selection_reason_id":1,"other_selection_reason":"sample other_selection_reason","action":"sample action","budget_type_field_id":1,"order_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_sell_order(client):
    """Test case for put_sell_order

    Update / Accept or Reject a specific sell order
    """
    body = {"comments":"sample comments","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"reject_reason":"sample reject_reason","payment_reference_no":"sample payment_reference_no","order_completion_date":"2000-01-23","payment_method_id":1,"unders_percent":"","overs_percent":"","supplier_selection_reason_id":1,"other_selection_reason":"sample other_selection_reason","action":"sample action","budget_type_field_id":1,"order_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

