# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capture_order_response import CaptureOrderResponse
from openapi_server.models.order import Order
from openapi_server.models.orders_acknowledge_request import OrdersAcknowledgeRequest
from openapi_server.models.orders_acknowledge_response import OrdersAcknowledgeResponse
from openapi_server.models.orders_advance_test_order_response import OrdersAdvanceTestOrderResponse
from openapi_server.models.orders_cancel_line_item_request import OrdersCancelLineItemRequest
from openapi_server.models.orders_cancel_line_item_response import OrdersCancelLineItemResponse
from openapi_server.models.orders_cancel_request import OrdersCancelRequest
from openapi_server.models.orders_cancel_response import OrdersCancelResponse
from openapi_server.models.orders_cancel_test_order_by_customer_request import OrdersCancelTestOrderByCustomerRequest
from openapi_server.models.orders_cancel_test_order_by_customer_response import OrdersCancelTestOrderByCustomerResponse
from openapi_server.models.orders_create_test_order_request import OrdersCreateTestOrderRequest
from openapi_server.models.orders_create_test_order_response import OrdersCreateTestOrderResponse
from openapi_server.models.orders_create_test_return_request import OrdersCreateTestReturnRequest
from openapi_server.models.orders_create_test_return_response import OrdersCreateTestReturnResponse
from openapi_server.models.orders_get_by_merchant_order_id_response import OrdersGetByMerchantOrderIdResponse
from openapi_server.models.orders_get_test_order_template_response import OrdersGetTestOrderTemplateResponse
from openapi_server.models.orders_in_store_refund_line_item_request import OrdersInStoreRefundLineItemRequest
from openapi_server.models.orders_in_store_refund_line_item_response import OrdersInStoreRefundLineItemResponse
from openapi_server.models.orders_list_response import OrdersListResponse
from openapi_server.models.orders_refund_item_request import OrdersRefundItemRequest
from openapi_server.models.orders_refund_item_response import OrdersRefundItemResponse
from openapi_server.models.orders_refund_order_request import OrdersRefundOrderRequest
from openapi_server.models.orders_refund_order_response import OrdersRefundOrderResponse
from openapi_server.models.orders_reject_return_line_item_request import OrdersRejectReturnLineItemRequest
from openapi_server.models.orders_reject_return_line_item_response import OrdersRejectReturnLineItemResponse
from openapi_server.models.orders_return_refund_line_item_request import OrdersReturnRefundLineItemRequest
from openapi_server.models.orders_return_refund_line_item_response import OrdersReturnRefundLineItemResponse
from openapi_server.models.orders_set_line_item_metadata_request import OrdersSetLineItemMetadataRequest
from openapi_server.models.orders_set_line_item_metadata_response import OrdersSetLineItemMetadataResponse
from openapi_server.models.orders_ship_line_items_request import OrdersShipLineItemsRequest
from openapi_server.models.orders_ship_line_items_response import OrdersShipLineItemsResponse
from openapi_server.models.orders_update_line_item_shipping_details_request import OrdersUpdateLineItemShippingDetailsRequest
from openapi_server.models.orders_update_line_item_shipping_details_response import OrdersUpdateLineItemShippingDetailsResponse
from openapi_server.models.orders_update_merchant_order_id_request import OrdersUpdateMerchantOrderIdRequest
from openapi_server.models.orders_update_merchant_order_id_response import OrdersUpdateMerchantOrderIdResponse
from openapi_server.models.orders_update_shipment_request import OrdersUpdateShipmentRequest
from openapi_server.models.orders_update_shipment_response import OrdersUpdateShipmentResponse


pytestmark = pytest.mark.asyncio

async def test_content_orders_acknowledge(client):
    """Test case for content_orders_acknowledge

    
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/acknowledge'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_advancetestorder(client):
    """Test case for content_orders_advancetestorder

    
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
        method='POST',
        path='/content/v2.1/{merchant_id}/testorders/{order_id}/advance'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_cancel(client):
    """Test case for content_orders_cancel

    
    """
    body = {"reason":"reason","reasonText":"reasonText","operationId":"operationId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/cancel'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_cancellineitem(client):
    """Test case for content_orders_cancellineitem

    
    """
    body = {"reason":"reason","quantity":0,"reasonText":"reasonText","productId":"productId","lineItemId":"lineItemId","operationId":"operationId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/cancelLineItem'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_canceltestorderbycustomer(client):
    """Test case for content_orders_canceltestorderbycustomer

    
    """
    body = {"reason":"reason"}
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
        path='/content/v2.1/{merchant_id}/testorders/{order_id}/cancelByCustomer'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_capture_order(client):
    """Test case for content_orders_capture_order

    
    """
    body = None
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/captureOrder'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_createtestorder(client):
    """Test case for content_orders_createtestorder

    
    """
    body = {"country":"country","templateName":"templateName","testOrder":{"enableOrderinvoices":True,"shippingCost":{"currency":"currency","value":"value"},"notificationMode":"notificationMode","predefinedPickupDetails":"predefinedPickupDetails","kind":"kind","pickupDetails":{"pickupLocationType":"pickupLocationType","pickupLocationAddress":{"country":"country","streetAddress":["streetAddress","streetAddress"],"postalCode":"postalCode","fullAddress":["fullAddress","fullAddress"],"isPostOfficeBox":True,"locality":"locality","recipientName":"recipientName","region":"region"},"pickupPersons":[{"phoneNumber":"phoneNumber","name":"name"},{"phoneNumber":"phoneNumber","name":"name"}],"locationCode":"locationCode"},"shippingOption":"shippingOption","lineItems":[{"returnInfo":{"isReturnable":True,"policyUrl":"policyUrl","daysToReturn":2},"product":{"fees":[{"amount":{"currency":"currency","value":"value"},"name":"name"},{"amount":{"currency":"currency","value":"value"},"name":"name"}],"gtin":"gtin","variantAttributes":[{"dimension":"dimension","value":"value"},{"dimension":"dimension","value":"value"}],"mpn":"mpn","title":"title","itemGroupId":"itemGroupId","targetCountry":"targetCountry","imageLink":"imageLink","condition":"condition","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","offerId":"offerId","brand":"brand"},"shippingDetails":{"method":{"carrier":"carrier","minDaysInTransit":1,"methodName":"methodName","maxDaysInTransit":7},"shipByDate":"shipByDate","deliverByDate":"deliverByDate","pickupPromiseInMinutes":1,"type":"type"},"quantityOrdered":0},{"returnInfo":{"isReturnable":True,"policyUrl":"policyUrl","daysToReturn":2},"product":{"fees":[{"amount":{"currency":"currency","value":"value"},"name":"name"},{"amount":{"currency":"currency","value":"value"},"name":"name"}],"gtin":"gtin","variantAttributes":[{"dimension":"dimension","value":"value"},{"dimension":"dimension","value":"value"}],"mpn":"mpn","title":"title","itemGroupId":"itemGroupId","targetCountry":"targetCountry","imageLink":"imageLink","condition":"condition","price":{"currency":"currency","value":"value"},"contentLanguage":"contentLanguage","offerId":"offerId","brand":"brand"},"shippingDetails":{"method":{"carrier":"carrier","minDaysInTransit":1,"methodName":"methodName","maxDaysInTransit":7},"shipByDate":"shipByDate","deliverByDate":"deliverByDate","pickupPromiseInMinutes":1,"type":"type"},"quantityOrdered":0}],"promotions":[{"funder":"funder","subtype":"subtype","taxValue":{"currency":"currency","value":"value"},"priceValue":{"currency":"currency","value":"value"},"startTime":"startTime","applicableItems":[{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"},{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"}],"endTime":"endTime","shortTitle":"shortTitle","title":"title","type":"type","appliedItems":[{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"},{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"}],"merchantPromotionId":"merchantPromotionId"},{"funder":"funder","subtype":"subtype","taxValue":{"currency":"currency","value":"value"},"priceValue":{"currency":"currency","value":"value"},"startTime":"startTime","applicableItems":[{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"},{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"}],"endTime":"endTime","shortTitle":"shortTitle","title":"title","type":"type","appliedItems":[{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"},{"quantity":1,"productId":"productId","lineItemId":"lineItemId","offerId":"offerId"}],"merchantPromotionId":"merchantPromotionId"}],"predefinedDeliveryAddress":"predefinedDeliveryAddress","predefinedEmail":"predefinedEmail","deliveryDetails":{"address":{"country":"country","streetAddress":["streetAddress","streetAddress"],"postalCode":"postalCode","fullAddress":["fullAddress","fullAddress"],"isPostOfficeBox":True,"locality":"locality","recipientName":"recipientName","region":"region"},"phoneNumber":"phoneNumber","isScheduledDelivery":True},"predefinedBillingAddress":"predefinedBillingAddress"}}
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
        path='/content/v2.1/{merchant_id}/testorders'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_createtestreturn(client):
    """Test case for content_orders_createtestreturn

    
    """
    body = {"items":[{"quantity":0,"lineItemId":"lineItemId"},{"quantity":0,"lineItemId":"lineItemId"}]}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/testreturn'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_get(client):
    """Test case for content_orders_get

    
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_getbymerchantorderid(client):
    """Test case for content_orders_getbymerchantorderid

    
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
        path='/content/v2.1/{merchant_id}/ordersbymerchantid/{merchant_order_id}'.format(merchant_id='merchant_id_example', merchant_order_id='merchant_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_gettestordertemplate(client):
    """Test case for content_orders_gettestordertemplate

    
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
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/testordertemplates/{template_name}'.format(merchant_id='merchant_id_example', template_name='template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_instorerefundlineitem(client):
    """Test case for content_orders_instorerefundlineitem

    
    """
    body = {"reason":"reason","quantity":0,"reasonText":"reasonText","productId":"productId","lineItemId":"lineItemId","operationId":"operationId","priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/inStoreRefundLineItem'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_list(client):
    """Test case for content_orders_list

    
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
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('placedDateEnd', 'placed_date_end_example'),
                    ('placedDateStart', 'placed_date_start_example'),
                    ('statuses', ['statuses_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/content/v2.1/{merchant_id}/orders'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_refunditem(client):
    """Test case for content_orders_refunditem

    
    """
    body = {"reason":"reason","reasonText":"reasonText","shipping":{"fullRefund":True,"amount":{"currency":"currency","value":"value"}},"operationId":"operationId","items":[{"fullRefund":True,"amount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"quantity":0,"productId":"productId","lineItemId":"lineItemId"},{"fullRefund":True,"amount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"quantity":0,"productId":"productId","lineItemId":"lineItemId"}]}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/refunditem'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_refundorder(client):
    """Test case for content_orders_refundorder

    
    """
    body = {"fullRefund":True,"reason":"reason","amount":{"priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}},"reasonText":"reasonText","operationId":"operationId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/refundorder'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_rejectreturnlineitem(client):
    """Test case for content_orders_rejectreturnlineitem

    
    """
    body = {"reason":"reason","quantity":0,"reasonText":"reasonText","productId":"productId","lineItemId":"lineItemId","operationId":"operationId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/rejectReturnLineItem'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_returnrefundlineitem(client):
    """Test case for content_orders_returnrefundlineitem

    
    """
    body = {"reason":"reason","quantity":0,"reasonText":"reasonText","productId":"productId","lineItemId":"lineItemId","operationId":"operationId","priceAmount":{"currency":"currency","value":"value"},"taxAmount":{"currency":"currency","value":"value"}}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/returnRefundLineItem'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_setlineitemmetadata(client):
    """Test case for content_orders_setlineitemmetadata

    
    """
    body = {"productId":"productId","lineItemId":"lineItemId","annotations":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"operationId":"operationId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/setLineItemMetadata'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_shiplineitems(client):
    """Test case for content_orders_shiplineitems

    
    """
    body = {"lineItems":[{"quantity":6,"productId":"productId","lineItemId":"lineItemId"},{"quantity":6,"productId":"productId","lineItemId":"lineItemId"}],"shipmentGroupId":"shipmentGroupId","operationId":"operationId","shipmentInfos":[{"carrier":"carrier","shipmentId":"shipmentId","trackingId":"trackingId"},{"carrier":"carrier","shipmentId":"shipmentId","trackingId":"trackingId"}]}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/shipLineItems'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_updatelineitemshippingdetails(client):
    """Test case for content_orders_updatelineitemshippingdetails

    
    """
    body = {"productId":"productId","lineItemId":"lineItemId","shipByDate":"shipByDate","operationId":"operationId","deliverByDate":"deliverByDate"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/updateLineItemShippingDetails'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_updatemerchantorderid(client):
    """Test case for content_orders_updatemerchantorderid

    
    """
    body = {"operationId":"operationId","merchantOrderId":"merchantOrderId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/updateMerchantOrderId'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_orders_updateshipment(client):
    """Test case for content_orders_updateshipment

    
    """
    body = {"carrier":"carrier","readyPickupDate":"readyPickupDate","shipmentId":"shipmentId","operationId":"operationId","scheduledDeliveryDetails":{"scheduledDate":"scheduledDate","carrierPhoneNumber":"carrierPhoneNumber"},"lastPickupDate":"lastPickupDate","deliveryDate":"deliveryDate","undeliveredDate":"undeliveredDate","status":"status","trackingId":"trackingId"}
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
        path='/content/v2.1/{merchant_id}/orders/{order_id}/updateShipment'.format(merchant_id='merchant_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

