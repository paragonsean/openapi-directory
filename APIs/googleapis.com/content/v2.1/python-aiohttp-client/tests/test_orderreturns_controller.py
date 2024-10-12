# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_order_return import MerchantOrderReturn
from openapi_server.models.orderreturns_acknowledge_request import OrderreturnsAcknowledgeRequest
from openapi_server.models.orderreturns_acknowledge_response import OrderreturnsAcknowledgeResponse
from openapi_server.models.orderreturns_create_order_return_request import OrderreturnsCreateOrderReturnRequest
from openapi_server.models.orderreturns_create_order_return_response import OrderreturnsCreateOrderReturnResponse
from openapi_server.models.orderreturns_list_response import OrderreturnsListResponse
from openapi_server.models.orderreturns_process_request import OrderreturnsProcessRequest
from openapi_server.models.orderreturns_process_response import OrderreturnsProcessResponse
from openapi_server.models.return_shipping_label import ReturnShippingLabel


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_acknowledge(client):
    """Test case for content_orderreturns_acknowledge

    
    """
    body = {"operationId":"operationId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/orderreturns/{return_id}/acknowledge'.format(merchant_id='merchant_id_example', return_id='return_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_createorderreturn(client):
    """Test case for content_orderreturns_createorderreturn

    
    """
    body = {"lineItems":[{"quantity":0,"productId":"productId","lineItemId":"lineItemId"},{"quantity":0,"productId":"productId","lineItemId":"lineItemId"}],"orderId":"orderId","operationId":"operationId","returnMethodType":"returnMethodType"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/orderreturns/createOrderReturn'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_get(client):
    """Test case for content_orderreturns_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/orderreturns/{return_id}'.format(merchant_id='merchant_id_example', return_id='return_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_labels_create(client):
    """Test case for content_orderreturns_labels_create

    
    """
    body = {"carrier":"carrier","labelUri":"labelUri","trackingId":"trackingId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/orderreturns/{return_id}/labels'.format(merchant_id='merchant_id_example', return_id='return_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_list(client):
    """Test case for content_orderreturns_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('acknowledged', True),
                    ('createdEndDate', 'created_end_date_example'),
                    ('createdStartDate', 'created_start_date_example'),
                    ('googleOrderIds', ['google_order_ids_example']),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('shipmentStates', ['shipment_states_example']),
                    ('shipmentStatus', ['shipment_status_example']),
                    ('shipmentTrackingNumbers', ['shipment_tracking_numbers_example']),
                    ('shipmentTypes', ['shipment_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/orderreturns'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orderreturns_process(client):
    """Test case for content_orderreturns_process

    
    """
    body = {"refundShippingFee":{"fullRefund":True,"reasonText":"reasonText","partialRefund":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"returnRefundReason":"returnRefundReason","paymentType":"paymentType"},"returnItems":[{"returnItemId":"returnItemId","reject":{"reason":"reason","reasonText":"reasonText"},"refund":{"fullRefund":True,"reasonText":"reasonText","partialRefund":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"returnRefundReason":"returnRefundReason","paymentType":"paymentType"}},{"returnItemId":"returnItemId","reject":{"reason":"reason","reasonText":"reasonText"},"refund":{"fullRefund":True,"reasonText":"reasonText","partialRefund":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"returnRefundReason":"returnRefundReason","paymentType":"paymentType"}}],"fullChargeReturnShippingCost":True,"operationId":"operationId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/content/v2.1/{merchant_id}/orderreturns/{return_id}/process'.format(merchant_id='merchant_id_example', return_id='return_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

