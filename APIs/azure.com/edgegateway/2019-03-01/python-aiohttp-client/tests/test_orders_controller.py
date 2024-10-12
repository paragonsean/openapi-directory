# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.order import Order
from openapi_server.models.order_list import OrderList


pytestmark = pytest.mark.asyncio

async def test_orders_create_or_update(client):
    """Test case for orders_create_or_update

    Creates or updates an order.
    """
    order = {"properties":{"contactInformation":{"emailList":["emailList","emailList"],"phone":"phone","companyName":"companyName","contactPerson":"contactPerson"},"serialNumber":"serialNumber","currentStatus":{"comments":"comments","updateDateTime":"2000-01-23T04:56:07.000+00:00","status":"Untracked"},"shippingAddress":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","addressLine3":"addressLine3","state":"state"},"orderHistory":[{"comments":"comments","updateDateTime":"2000-01-23T04:56:07.000+00:00","status":"Untracked"},{"comments":"comments","updateDateTime":"2000-01-23T04:56:07.000+00:00","status":"Untracked"}],"deliveryTrackingInfo":[{"serialNumber":"serialNumber","carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"},{"serialNumber":"serialNumber","carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"}],"returnTrackingInfo":[{"serialNumber":"serialNumber","carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"},{"serialNumber":"serialNumber","carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/orders/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=order,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_delete(client):
    """Test case for orders_delete

    Deletes the order related to the device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/orders/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_get(client):
    """Test case for orders_get

    Gets a specific order by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/orders/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_list_by_data_box_edge_device(client):
    """Test case for orders_list_by_data_box_edge_device

    Lists all the orders related to a data box edge/gateway device.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/orders'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

