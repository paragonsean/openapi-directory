# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_create_shipment_api_model import BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_shipment import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_shipment_with_label_result import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult
from openapi_server.models.rechnungsdruck_web_app_controllers_api_shipment_with_label import RechnungsdruckWebAppControllersApiShipmentWithLabel


pytestmark = pytest.mark.asyncio

async def test_shipment_get_list(client):
    """Test case for shipment_get_list

    Get a list of all shipments optionally filtered by date. All parameters are optional.
    """
    params = [('page', 56),
                    ('pageSize', 56),
                    ('createdAtMin', '2013-10-20T19:20:30+01:00'),
                    ('createdAtMax', '2013-10-20T19:20:30+01:00'),
                    ('orderId', 56),
                    ('minimumShipmentId', 56),
                    ('shippingProviderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/shipment/shipments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipment_get_ping(client):
    """Test case for shipment_get_ping

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/shipment/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipment_get_shipping_carrier(client):
    """Test case for shipment_get_shipping_carrier

    Queries the currently available shipping carriers.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/shipment/shippingcarriers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipment_get_shippingproviders(client):
    """Test case for shipment_get_shippingproviders

    Query all defined shipping providers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/shipment/shippingproviders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shipment_post_shipment(client):
    """Test case for shipment_post_shipment

    Creates a new shipment with the selected Shippingprovider
    """
    body = openapi_server.BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/shipment/shipment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shipment_ship_with_label(client):
    """Test case for shipment_ship_with_label

    Creates a shipment for an order in billbee
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiShipmentWithLabel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/shipment/shipwithlabel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

