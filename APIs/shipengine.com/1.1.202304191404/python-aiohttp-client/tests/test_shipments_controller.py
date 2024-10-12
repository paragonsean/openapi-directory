# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_shipments_request_body import CreateShipmentsRequestBody
from openapi_server.models.create_shipments_response_body import CreateShipmentsResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_shipment_by_external_id_response_body import GetShipmentByExternalIdResponseBody
from openapi_server.models.get_shipment_by_id_response_body import GetShipmentByIdResponseBody
from openapi_server.models.list_shipment_rates_response_body import ListShipmentRatesResponseBody
from openapi_server.models.list_shipments_response_body import ListShipmentsResponseBody
from openapi_server.models.parse_shipment_request_body import ParseShipmentRequestBody
from openapi_server.models.parse_shipment_response_body import ParseShipmentResponseBody
from openapi_server.models.shipment_status import ShipmentStatus
from openapi_server.models.shipments_sort_by import ShipmentsSortBy
from openapi_server.models.sort_dir import SortDir
from openapi_server.models.tag_shipment_response_body import TagShipmentResponseBody
from openapi_server.models.update_shipment_request_body import UpdateShipmentRequestBody
from openapi_server.models.update_shipment_response_body import UpdateShipmentResponseBody


pytestmark = pytest.mark.asyncio

async def test_cancel_shipments(client):
    """Test case for cancel_shipments

    Cancel a Shipment
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/shipments/{shipment_id}/cancel'.format(shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_shipments(client):
    """Test case for create_shipments

    Create Shipments
    """
    body = openapi_server.CreateShipmentsRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/shipments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipment_by_external_id(client):
    """Test case for get_shipment_by_external_id

    Get Shipment By External ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipments/external_shipment_id/{external_shipment_id}'.format(external_shipment_id='0bcb569d-1727-4ff9-ab49-b2fec0cee5ae'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipment_by_id(client):
    """Test case for get_shipment_by_id

    Get Shipment By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipments/{shipment_id}'.format(shipment_id='shipment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_shipment_rates(client):
    """Test case for list_shipment_rates

    Get Shipment Rates
    """
    params = [('created_at_start', '2019-03-12T19:24:13.657Z')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipments/{shipment_id}/rates'.format(shipment_id='shipment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_shipments(client):
    """Test case for list_shipments

    List Shipments
    """
    params = [('shipment_status', openapi_server.ShipmentStatus()),
                    ('batch_id', 'batch_id_example'),
                    ('tag', 'Letters_to_santa'),
                    ('created_at_start', '2019-03-12T19:24:13.657Z'),
                    ('created_at_end', '2019-03-12T19:24:13.657Z'),
                    ('modified_at_start', '2019-03-12T19:24:13.657Z'),
                    ('modified_at_end', '2019-03-12T19:24:13.657Z'),
                    ('page', 1),
                    ('page_size', 25),
                    ('sales_order_id', 'sales_order_id_example'),
                    ('sort_dir', openapi_server.SortDir()),
                    ('sort_by', openapi_server.ShipmentsSortBy())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_shipment(client):
    """Test case for parse_shipment

    Parse shipping info
    """
    body = {"shipment":{"service_code":"usps_first_class_mail","ship_from":{"address_line1":"587 Shotwell St.","address_line2":"Suite 201","address_residential_indicator":true,"city_locality":"San Francisco","company_name":"My Awesome Store","country_code":"US","phone":"555-555-5555","postal_code":94110,"state_province":"CA"}},"text":"I have a 4oz package that's 5x10x14in, and I need to ship it to Margie McMiller at 3800 North Lamar suite 200 in austin, tx 78652. Please send it via USPS first class and require an adult signature. It also needs to be insured for $400.\n"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/shipments/recognize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_shipment(client):
    """Test case for tag_shipment

    Add Tag to Shipment
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/shipments/{shipment_id}/tags/{tag_name}'.format(shipment_id='shipment_id_example', tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_shipment(client):
    """Test case for untag_shipment

    Remove Tag from Shipment
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/shipments/{shipment_id}/tags/{tag_name}'.format(shipment_id='shipment_id_example', tag_name='tag_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_shipment(client):
    """Test case for update_shipment

    Update Shipment By ID
    """
    body = openapi_server.UpdateShipmentRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/shipments/{shipment_id}'.format(shipment_id='shipment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

