# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.model_response_order_abandoned_list import ModelResponseOrderAbandonedList
from openapi_server.models.model_response_order_list import ModelResponseOrderList
from openapi_server.models.model_response_order_preestimate_shipping_list import ModelResponseOrderPreestimateShippingList
from openapi_server.models.model_response_order_shipment_list import ModelResponseOrderShipmentList
from openapi_server.models.model_response_order_transaction_list import ModelResponseOrderTransactionList
from openapi_server.models.order_add import OrderAdd
from openapi_server.models.order_add200_response import OrderAdd200Response
from openapi_server.models.order_count200_response import OrderCount200Response
from openapi_server.models.order_financial_status_list200_response import OrderFinancialStatusList200Response
from openapi_server.models.order_find200_response import OrderFind200Response
from openapi_server.models.order_fulfillment_status_list200_response import OrderFulfillmentStatusList200Response
from openapi_server.models.order_info200_response import OrderInfo200Response
from openapi_server.models.order_preestimate_shipping_list import OrderPreestimateShippingList
from openapi_server.models.order_refund_add import OrderRefundAdd
from openapi_server.models.order_refund_add200_response import OrderRefundAdd200Response
from openapi_server.models.order_shipment_add import OrderShipmentAdd
from openapi_server.models.order_shipment_add200_response import OrderShipmentAdd200Response
from openapi_server.models.order_shipment_delete200_response import OrderShipmentDelete200Response
from openapi_server.models.order_shipment_tracking_add import OrderShipmentTrackingAdd
from openapi_server.models.order_shipment_tracking_add200_response import OrderShipmentTrackingAdd200Response
from openapi_server.models.order_shipment_update import OrderShipmentUpdate
from openapi_server.models.order_status_list200_response import OrderStatusList200Response


pytestmark = pytest.mark.asyncio

async def test_order_abandoned_list(client):
    """Test case for order_abandoned_list

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('customer_email', 'customer_email_example'),
                    ('created_to', 'created_to_example'),
                    ('created_from', 'created_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('skip_empty_email', False),
                    ('store_id', 'store_id_example'),
                    ('page_cursor', 'page_cursor_example'),
                    ('count', 10),
                    ('start', 0),
                    ('params', 'customer,totals,items'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.abandoned.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_add(client):
    """Test case for order_add

    
    """
    body = {"admin_private_comment":"admin_private_comment","date":"date","fulfillment_status":"fulfillment_status","bill_first_name":"bill_first_name","shipp_country":"shipp_country","discount":6.027456183070403,"tax_price":1.2315135367772556,"bill_last_name":"bill_last_name","bill_country":"bill_country","shipp_fax":"shipp_fax","order_status":"order_status","clear_cache":True,"customer_fax":"customer_fax","coupons":["coupons","coupons"],"total_paid":1.0246457001441578,"id":"id","bill_address_2":"bill_address_2","bill_address_1":"bill_address_1","transaction_id":"transaction_id","shipping_price":2.027123023002322,"subtotal_price":7.386281948385884,"shipp_last_name":"shipp_last_name","bill_company":"bill_company","customer_first_name":"customer_first_name","inventory_behaviour":"bypass","customer_phone":"customer_phone","bill_state":"bill_state","tags":"tags","date_finished":"date_finished","customer_email":"customer_email","note_attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"channel_id":"channel_id","order_id":"order_id","coupon_discount":0.8008281904610115,"bill_city":"bill_city","bill_postcode":"bill_postcode","admin_comment":"admin_comment","shipp_address_1":"shipp_address_1","shipp_postcode":"shipp_postcode","shipp_address_2":"shipp_address_2","customer_birthday":"customer_birthday","shipp_state":"shipp_state","total_weight":6,"customer_last_name":"customer_last_name","shipp_first_name":"shipp_first_name","order_payment_method":"order_payment_method","currency":"currency","external_source":"external_source","shipping_tax":4.145608029883936,"store_id":"store_id","create_invoice":False,"total_price":1.4894159098541704,"send_notifications":False,"send_admin_notifications":False,"order_shipping_method":"order_shipping_method","prices_inc_tax":False,"bill_fax":"bill_fax","shipp_company":"shipp_company","bill_phone":"bill_phone","gift_certificate_discount":1.4658129805029452,"date_modified":"date_modified","order_item":[{"order_item_property":[{"order_item_property_value":"order_item_property_value","order_item_property_name":"order_item_property_name"},{"order_item_property_value":"order_item_property_value","order_item_property_name":"order_item_property_name"}],"order_item_tax":9.301444243932576,"order_item_parent":5,"order_item_name":"order_item_name","order_item_allow_refund_items_separately":True,"order_item_parent_option_name":"order_item_parent_option_name","order_item_price_includes_tax":False,"order_item_quantity":7,"order_item_variant_id":"order_item_variant_id","order_item_id":"order_item_id","order_item_price":2.3021358869347655,"order_item_allow_ship_items_separately":True,"order_item_option":[{"order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name","order_item_option_price":5.962133916683182},{"order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name","order_item_option_price":5.962133916683182}],"order_item_model":"order_item_model","order_item_weight":3.616076749251911},{"order_item_property":[{"order_item_property_value":"order_item_property_value","order_item_property_name":"order_item_property_name"},{"order_item_property_value":"order_item_property_value","order_item_property_name":"order_item_property_name"}],"order_item_tax":9.301444243932576,"order_item_parent":5,"order_item_name":"order_item_name","order_item_allow_refund_items_separately":True,"order_item_parent_option_name":"order_item_parent_option_name","order_item_price_includes_tax":False,"order_item_quantity":7,"order_item_variant_id":"order_item_variant_id","order_item_id":"order_item_id","order_item_price":2.3021358869347655,"order_item_allow_ship_items_separately":True,"order_item_option":[{"order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name","order_item_option_price":5.962133916683182},{"order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name","order_item_option_price":5.962133916683182}],"order_item_model":"order_item_model","order_item_weight":3.616076749251911}],"financial_status":"financial_status","comment":"comment","shipp_phone":"shipp_phone","shipp_city":"shipp_city"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/order.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_count(client):
    """Test case for order_count

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('customer_email', 'customer_email_example'),
                    ('order_status', 'order_status_example'),
                    ('order_status_ids', ['order_status_ids_example']),
                    ('created_to', 'created_to_example'),
                    ('created_from', 'created_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('store_id', 'store_id_example'),
                    ('ids', 'ids_example'),
                    ('order_ids', 'order_ids_example'),
                    ('ebay_order_status', 'ebay_order_status_example'),
                    ('financial_status', 'financial_status_example'),
                    ('fulfillment_status', 'fulfillment_status_example'),
                    ('shipping_method', 'shipping_method_example'),
                    ('delivery_method', 'delivery_method_example'),
                    ('ship_node_type', 'ship_node_type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_financial_status_list(client):
    """Test case for order_financial_status_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.financial_status.list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_find(client):
    """Test case for order_find

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('customer_email', 'customer_email_example'),
                    ('order_status', 'order_status_example'),
                    ('start', 0),
                    ('count', 10),
                    ('params', 'order_id,customer,totals,address,items,bundles,status'),
                    ('exclude', 'exclude_example'),
                    ('created_to', 'created_to_example'),
                    ('created_from', 'created_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('financial_status', 'financial_status_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.find.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_fulfillment_status_list(client):
    """Test case for order_fulfillment_status_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.fulfillment_status.list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_info(client):
    """Test case for order_info

    
    """
    params = [('order_id', 'order_id_example'),
                    ('id', 'id_example'),
                    ('params', 'order_id,customer,totals,address,items,bundles,status'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example'),
                    ('enable_cache', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_list(client):
    """Test case for order_list

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('customer_email', 'customer_email_example'),
                    ('phone', 'phone_example'),
                    ('order_status', 'order_status_example'),
                    ('order_status_ids', ['order_status_ids_example']),
                    ('start', 0),
                    ('count', 10),
                    ('page_cursor', 'page_cursor_example'),
                    ('sort_by', 'order_id'),
                    ('sort_direction', 'asc'),
                    ('params', 'order_id,customer,totals,address,items,bundles,status'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('created_to', 'created_to_example'),
                    ('created_from', 'created_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('store_id', 'store_id_example'),
                    ('ids', 'ids_example'),
                    ('order_ids', 'order_ids_example'),
                    ('ebay_order_status', 'ebay_order_status_example'),
                    ('basket_id', 'basket_id_example'),
                    ('financial_status', 'financial_status_example'),
                    ('fulfillment_status', 'fulfillment_status_example'),
                    ('shipping_method', 'shipping_method_example'),
                    ('skip_order_ids', 'skip_order_ids_example'),
                    ('since_id', 56),
                    ('is_deleted', True),
                    ('shipping_country_iso3', 'shipping_country_iso3_example'),
                    ('enable_cache', False),
                    ('delivery_method', 'delivery_method_example'),
                    ('ship_node_type', 'ship_node_type_example'),
                    ('currency_id', 'currency_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_preestimate_shipping_list(client):
    """Test case for order_preestimate_shipping_list

    
    """
    body = {"store_id":"store_id","order_item":[{"order_item_id":"order_item_id","order_item_option":[{"order_item_option_id":"order_item_option_id","order_item_option_used_in_combinations":True,"order_item_option_value_id":"order_item_option_value_id","order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name"},{"order_item_option_id":"order_item_option_id","order_item_option_used_in_combinations":True,"order_item_option_value_id":"order_item_option_value_id","order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name"}],"order_item_model":"order_item_model","order_item_quantity":0,"order_item_variant_id":"order_item_variant_id","order_item_weight":6.027456183070403},{"order_item_id":"order_item_id","order_item_option":[{"order_item_option_id":"order_item_option_id","order_item_option_used_in_combinations":True,"order_item_option_value_id":"order_item_option_value_id","order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name"},{"order_item_option_id":"order_item_option_id","order_item_option_used_in_combinations":True,"order_item_option_value_id":"order_item_option_value_id","order_item_option_value":"order_item_option_value","order_item_option_name":"order_item_option_name"}],"order_item_model":"order_item_model","order_item_quantity":0,"order_item_variant_id":"order_item_variant_id","order_item_weight":6.027456183070403}],"shipp_country":"shipp_country","customer_email":"customer_email","exclude":"exclude","shipp_address_1":"shipp_address_1","shipp_postcode":"shipp_postcode","customer_id":"customer_id","params":"force_all","shipp_city":"shipp_city","shipp_state":"shipp_state","warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/order.preestimate_shipping.list.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_refund_add(client):
    """Test case for order_refund_add

    
    """
    body = {"date":"date","shipping_price":5.962133916683182,"item_restock":False,"total_price":5.637376656633329,"send_notifications":False,"is_online":False,"fee_price":0.8008281904610115,"message":"message","items":[{"order_product_id":"order_product_id","quantity":1,"price":6.027456183070403},{"order_product_id":"order_product_id","quantity":1,"price":6.027456183070403}],"order_id":"order_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/order.refund.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_add(client):
    """Test case for order_shipment_add

    
    """
    body = {"adjust_stock":False,"store_id":"store_id","is_shipped":True,"enable_cache":False,"send_notifications":False,"shipping_method":"shipping_method","shipment_provider":"shipment_provider","tracking_numbers":[{"carrier_id":"carrier_id","tracking_number":"tracking_number"},{"carrier_id":"carrier_id","tracking_number":"tracking_number"}],"items":[{"order_product_id":"order_product_id","quantity":0.8008281904610115},{"order_product_id":"order_product_id","quantity":0.8008281904610115}],"order_id":"order_id","tracking_link":"tracking_link","warehouse_id":"warehouse_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/order.shipment.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_delete(client):
    """Test case for order_shipment_delete

    
    """
    params = [('shipment_id', 'shipment_id_example'),
                    ('order_id', 'order_id_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/order.shipment.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_info(client):
    """Test case for order_shipment_info

    
    """
    params = [('id', 'id_example'),
                    ('order_id', 'order_id_example'),
                    ('start', 0),
                    ('params', 'id,order_id,items,tracking_numbers'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.shipment.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_list(client):
    """Test case for order_shipment_list

    
    """
    params = [('order_id', 'order_id_example'),
                    ('page_cursor', 'page_cursor_example'),
                    ('start', 0),
                    ('count', 10),
                    ('params', 'id,order_id,items,tracking_numbers'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('created_from', 'created_from_example'),
                    ('created_to', 'created_to_example'),
                    ('modified_from', 'modified_from_example'),
                    ('modified_to', 'modified_to_example'),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.shipment.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_tracking_add(client):
    """Test case for order_shipment_tracking_add

    
    """
    body = {"carrier_id":"carrier_id","store_id":"store_id","send_notifications":False,"tracking_number":"tracking_number","tracking_provider":"tracking_provider","shipment_id":"shipment_id","order_id":"order_id","tracking_link":"tracking_link"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/order.shipment.tracking.add.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_shipment_update(client):
    """Test case for order_shipment_update

    
    """
    body = {"store_id":"store_id","is_shipped":True,"replace":True,"tracking_numbers":[{"carrier_id":"carrier_id","tracking_number":"tracking_number"},{"carrier_id":"carrier_id","tracking_number":"tracking_number"}],"shipment_id":"shipment_id","order_id":"order_id","tracking_link":"tracking_link"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/order.shipment.update.json',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_status_list(client):
    """Test case for order_status_list

    
    """
    params = [('store_id', 'store_id_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.status.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_transaction_list(client):
    """Test case for order_transaction_list

    
    """
    params = [('count', 10),
                    ('order_ids', 'order_ids_example'),
                    ('store_id', 'store_id_example'),
                    ('params', 'id,order_id,amount,description'),
                    ('response_fields', 'response_fields_example'),
                    ('exclude', 'exclude_example'),
                    ('page_cursor', 'page_cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/order.transaction.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_update(client):
    """Test case for order_update

    
    """
    params = [('order_id', 'order_id_example'),
                    ('store_id', 'store_id_example'),
                    ('order_status', 'order_status_example'),
                    ('comment', 'comment_example'),
                    ('admin_comment', 'admin_comment_example'),
                    ('admin_private_comment', 'admin_private_comment_example'),
                    ('date_modified', 'date_modified_example'),
                    ('date_finished', 'date_finished_example'),
                    ('financial_status', 'financial_status_example'),
                    ('fulfillment_status', 'fulfillment_status_example'),
                    ('order_payment_method', 'order_payment_method_example'),
                    ('send_notifications', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/order.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

