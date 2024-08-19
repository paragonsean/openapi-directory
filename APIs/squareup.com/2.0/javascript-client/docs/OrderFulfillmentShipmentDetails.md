# SquareConnectApi.OrderFulfillmentShipmentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelReason** | **String** | A description of why the shipment was canceled. | [optional] 
**canceledAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating the shipment was canceled. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**carrier** | **String** | The shipping carrier being used to ship this fulfillment (such as UPS, FedEx, or USPS). | [optional] 
**expectedShippedAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when the shipment is expected to be delivered to the shipping carrier. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**failedAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when the shipment failed to be completed. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**failureReason** | **String** | A description of why the shipment failed to be completed. | [optional] 
**inProgressAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when this fulfillment was moved to the &#x60;RESERVED&#x60; state, which  indicates that preparation of this shipment has begun. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**packagedAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when this fulfillment was moved to the &#x60;PREPARED&#x60; state, which indicates that the fulfillment is packaged. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**placedAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when the shipment was requested. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**recipient** | [**OrderFulfillmentRecipient**](OrderFulfillmentRecipient.md) |  | [optional] 
**shippedAt** | **String** | The [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) indicating when this fulfillment was moved to the &#x60;COMPLETED&#x60; state, which indicates that the fulfillment has been given to the shipping carrier. The timestamp must be in RFC 3339 format (for example, \&quot;2016-09-04T23:59:33.123Z\&quot;). | [optional] 
**shippingNote** | **String** | A note with additional information for the shipping carrier. | [optional] 
**shippingType** | **String** | A description of the type of shipping product purchased from the carrier (such as First Class, Priority, or Express). | [optional] 
**trackingNumber** | **String** | The reference number provided by the carrier to track the shipment&#39;s progress. | [optional] 
**trackingUrl** | **String** | A link to the tracking webpage on the carrier&#39;s website. | [optional] 


