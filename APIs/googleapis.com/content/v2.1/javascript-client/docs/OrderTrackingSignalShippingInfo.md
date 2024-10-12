# ContentApiForShopping.OrderTrackingSignalShippingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualDeliveryTime** | **Date** |  | [optional] 
**carrierName** | **String** | The name of the shipping carrier for the delivery. This field is required if one of the following fields is absent: earliest_delivery_promise_time, latest_delivery_promise_time, and actual_delivery_time. | [optional] 
**carrierServiceName** | **String** | The service type for fulfillment, e.g., GROUND, FIRST_CLASS, etc. | [optional] 
**earliestDeliveryPromiseTime** | **Date** |  | [optional] 
**latestDeliveryPromiseTime** | **Date** |  | [optional] 
**originPostalCode** | **String** | The origin postal code, as a continuous string without spaces or dashes, e.g. \&quot;95016\&quot;. This field will be anonymized in returned OrderTrackingSignal creation response. | [optional] 
**originRegionCode** | **String** | The [CLDR territory code] (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for the shipping origin. | [optional] 
**shipmentId** | **String** | Required. The shipment ID. This field will be hashed in returned OrderTrackingSignal creation response. | [optional] 
**shippedTime** | **Date** |  | [optional] 
**shippingStatus** | **String** | The status of the shipment. | [optional] 
**trackingId** | **String** | The tracking ID of the shipment. This field is required if one of the following fields is absent: earliest_delivery_promise_time, latest_delivery_promise_time, and actual_delivery_time. | [optional] 



## Enum: ShippingStatusEnum


* `SHIPPING_STATE_UNSPECIFIED` (value: `"SHIPPING_STATE_UNSPECIFIED"`)

* `SHIPPED` (value: `"SHIPPED"`)

* `DELIVERED` (value: `"DELIVERED"`)




