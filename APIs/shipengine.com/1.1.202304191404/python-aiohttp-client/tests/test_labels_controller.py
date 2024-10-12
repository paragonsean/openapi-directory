# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_label_from_rate_request_body import CreateLabelFromRateRequestBody
from openapi_server.models.create_label_from_rate_response_body import CreateLabelFromRateResponseBody
from openapi_server.models.create_label_from_shipment_request_body import CreateLabelFromShipmentRequestBody
from openapi_server.models.create_label_from_shipment_response_body import CreateLabelFromShipmentResponseBody
from openapi_server.models.create_label_request_body import CreateLabelRequestBody
from openapi_server.models.create_label_response_body import CreateLabelResponseBody
from openapi_server.models.create_return_label_request_body import CreateReturnLabelRequestBody
from openapi_server.models.create_return_label_response_body import CreateReturnLabelResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_label_by_external_shipment_id_response_body import GetLabelByExternalShipmentIdResponseBody
from openapi_server.models.get_label_by_id_response_body import GetLabelByIdResponseBody
from openapi_server.models.get_tracking_log_from_label_response_body import GetTrackingLogFromLabelResponseBody
from openapi_server.models.label_download_type import LabelDownloadType
from openapi_server.models.label_status import LabelStatus
from openapi_server.models.list_labels_response_body import ListLabelsResponseBody
from openapi_server.models.sort_dir import SortDir
from openapi_server.models.void_label_response_body import VoidLabelResponseBody


pytestmark = pytest.mark.asyncio

async def test_create_label(client):
    """Test case for create_label

    Purchase Label
    """
    body = openapi_server.CreateLabelRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/labels',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_label_from_rate(client):
    """Test case for create_label_from_rate

    Purchase Label with Rate ID
    """
    body = openapi_server.CreateLabelFromRateRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/labels/rates/{rate_id}'.format(rate_id='rate_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_label_from_shipment(client):
    """Test case for create_label_from_shipment

    Purchase Label with Shipment ID
    """
    body = openapi_server.CreateLabelFromShipmentRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/labels/shipment/{shipment_id}'.format(shipment_id='shipment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_return_label(client):
    """Test case for create_return_label

    Create a return label
    """
    body = openapi_server.CreateReturnLabelRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/labels/{label_id}/return'.format(label_id='label_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_label_by_external_shipment_id(client):
    """Test case for get_label_by_external_shipment_id

    Get Label By External Shipment ID
    """
    params = [('label_download_type', openapi_server.LabelDownloadType())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/labels/external_shipment_id/{external_shipment_id}'.format(external_shipment_id='0bcb569d-1727-4ff9-ab49-b2fec0cee5ae'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_label_by_id(client):
    """Test case for get_label_by_id

    Get Label By ID
    """
    params = [('label_download_type', openapi_server.LabelDownloadType())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/labels/{label_id}'.format(label_id='label_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tracking_log_from_label(client):
    """Test case for get_tracking_log_from_label

    Get Label Tracking Information
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/labels/{label_id}/track'.format(label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_labels(client):
    """Test case for list_labels

    List labels
    """
    params = [('label_status', openapi_server.LabelStatus()),
                    ('service_code', 'usps_first_class_mail'),
                    ('carrier_id', 'carrier_id_example'),
                    ('tracking_number', '9405511899223197428490'),
                    ('batch_id', 'batch_id_example'),
                    ('rate_id', 'rate_id_example'),
                    ('shipment_id', 'shipment_id_example'),
                    ('warehouse_id', 'warehouse_id_example'),
                    ('created_at_start', '2019-03-12T19:24:13.657Z'),
                    ('created_at_end', '2019-03-12T19:24:13.657Z'),
                    ('page', 1),
                    ('page_size', 25),
                    ('sort_dir', openapi_server.SortDir()),
                    ('sort_by', created_at)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/labels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_void_label(client):
    """Test case for void_label

    Void a Label By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/labels/{label_id}/void'.format(label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

