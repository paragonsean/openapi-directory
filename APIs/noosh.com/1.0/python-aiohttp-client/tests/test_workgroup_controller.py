# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_workgroup_expand_vo import ClientWorkgroupExpandVO
from openapi_server.models.client_workgroup_list_vo import ClientWorkgroupListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.supplier_workgroup_expand_vo import SupplierWorkgroupExpandVO
from openapi_server.models.supplier_workgroup_list_vo import SupplierWorkgroupListVO
from openapi_server.models.workgroup_expand_vo import WorkgroupExpandVO
from openapi_server.models.workgroup_http_status_vo import WorkgroupHTTPStatusVO
from openapi_server.models.workgroup_list_vo import WorkgroupListVO
from openapi_server.models.workgroup_upd_persist_vo import WorkgroupUpdPersistVO


pytestmark = pytest.mark.asyncio

async def test_get_client_workgroup_list(client):
    """Test case for get_client_workgroup_list

    List client workgroups
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/clientWorkgroups'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_specific_client_workgroup(client):
    """Test case for get_specific_client_workgroup

    Get a specific client workgroups
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}'.format(workgroup_id='workgroup_id_example', client_workgroup_id='client_workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_supplier_workgroup_detail(client):
    """Test case for get_supplier_workgroup_detail

    Get the specific supplier of My Group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/supplierWorkgroups/{bu_supplier_workgroup_id}'.format(workgroup_id='workgroup_id_example', bu_supplier_workgroup_id='bu_supplier_workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_supplier_workgroup_list(client):
    """Test case for get_supplier_workgroup_list

    List supplier workgroups
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/supplierWorkgroups'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workgroup_detail(client):
    """Test case for get_workgroup_detail

    Detail workgroup info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/detail'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workgroup_list(client):
    """Test case for get_workgroup_list

    List the workgroups
    """
    params = [('workgroup_name', 'workgroup_name_example'),
                    ('workgroup_types', ['workgroup_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_workgroup(client):
    """Test case for put_workgroup

    Update a specific Workgroup
    """
    body = {"country":"sample country","address_line3":"sample address_line3","address_line2":"sample address_line2","address_line1":"sample address_line1","city":"sample city","workgroup_name":"sample workgroup_name","custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"postal":"sample postal","state":"sample state","decimal_places":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/detail'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

