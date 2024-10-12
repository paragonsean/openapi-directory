# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.shipment_expand_vo import ShipmentExpandVO
from openapi_server.models.shipment_list_vo import ShipmentListVO
from openapi_server.models.shipment_location_persist_vo import ShipmentLocationPersistVO
from openapi_server.models.shipment_location_post_persist_vo import ShipmentLocationPostPersistVO
from openapi_server.models.shipment_locations_post_result_vo import ShipmentLocationsPOSTResultVO


pytestmark = pytest.mark.asyncio

async def test_get_shipment(client):
    """Test case for get_shipment

    Get a specific shipment.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipment_list(client):
    """Test case for get_shipment_list

    List shipments of project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/shipments'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_shipment(client):
    """Test case for post_shipment

    Create a shipment
    """
    body = {"request_type":"sample request_type","city":"sample city","requested_quantity":1,"pallet_lablel":"sample pallet_lablel","description_or_title":"sample description_or_title","shpping_method":"sample shpping_method","shipping_carrier":"sample shipping_carrier","address_line3":"sample address_line3","address_line2":"sample address_line2","address_line1":"sample address_line1","batch_label":"sample batch_label","work_phone_number":"sample work_phone_number","workgroup_name":"sample workgroup_name","state":"sample state","first_name":"sample first_name","email":"sample email","poof_type":"sample poof_type","shipment_request_custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"last_name":"sample last_name","inner_carton_label":"sample inner_carton_label","middle_name":"sample middle_name","shipment_custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"spec_ids":"sample spec_ids","delivery_date":"2000-01-23","country_iso_code":"sample country_iso_code","outer_carton_label":"sample outer_carton_label","shipping_instruction":"sample shipping_instruction","company_name":"sample company_name","postal_code":"sample postal_code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/shipments'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_shipment_location(client):
    """Test case for put_shipment_location

    Update a specific shipment location
    """
    body = {"received_date":"2000-01-23","shipping_cost":"","shipped_date":"2000-01-23","due_date":"2000-01-23","qty_received":1,"qty_shipped":1,"type":"sample type","qty_requested":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id}/locations/{location_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', shipment_id='shipment_id_example', location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

