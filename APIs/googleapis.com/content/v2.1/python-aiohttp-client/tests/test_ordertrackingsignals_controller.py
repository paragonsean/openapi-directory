# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.order_tracking_signal import OrderTrackingSignal


pytestmark = pytest.mark.asyncio

async def test_content_ordertrackingsignals_create(client):
    """Test case for content_ordertrackingsignals_create

    
    """
    body = {"lineItems":[{"productTitle":"productTitle","gtin":"gtin","quantity":"quantity","productId":"productId","lineItemId":"lineItemId","upc":"upc","mpn":"mpn","sku":"sku","brand":"brand","productDescription":"productDescription"},{"productTitle":"productTitle","gtin":"gtin","quantity":"quantity","productId":"productId","lineItemId":"lineItemId","upc":"upc","mpn":"mpn","sku":"sku","brand":"brand","productDescription":"productDescription"}],"merchantId":"merchantId","orderId":"orderId","customerShippingFee":{"currency":"currency","value":"value"},"deliveryPostalCode":"deliveryPostalCode","orderTrackingSignalId":"orderTrackingSignalId","shippingInfo":[{"earliestDeliveryPromiseTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"shippingStatus":"SHIPPING_STATE_UNSPECIFIED","shippedTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"carrierName":"carrierName","carrierServiceName":"carrierServiceName","latestDeliveryPromiseTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"shipmentId":"shipmentId","actualDeliveryTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"originPostalCode":"originPostalCode","originRegionCode":"originRegionCode","trackingId":"trackingId"},{"earliestDeliveryPromiseTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"shippingStatus":"SHIPPING_STATE_UNSPECIFIED","shippedTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"carrierName":"carrierName","carrierServiceName":"carrierServiceName","latestDeliveryPromiseTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"shipmentId":"shipmentId","actualDeliveryTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0},"originPostalCode":"originPostalCode","originRegionCode":"originRegionCode","trackingId":"trackingId"}],"deliveryRegionCode":"deliveryRegionCode","shipmentLineItemMapping":[{"quantity":"quantity","lineItemId":"lineItemId","shipmentId":"shipmentId"},{"quantity":"quantity","lineItemId":"lineItemId","shipmentId":"shipmentId"}],"orderCreatedTime":{"hours":6,"seconds":2,"utcOffset":"utcOffset","month":5,"nanos":5,"year":7,"minutes":1,"timeZone":{"id":"id","version":"version"},"day":0}}
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
        path='/content/v2.1/{merchant_id}/ordertrackingsignals'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

