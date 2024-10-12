# VoodooManufacturing3DPrintApi.OrderCreatePost200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**deliveryDate** | **String** | The target delivery date for the shipping method. Formatted as a datetime string. | [optional] 
**notes** | **String** |  | [optional] 
**orderItems** | [**[Print]**](Print.md) |  | [optional] 
**quote** | [**Quote**](Quote.md) |  | [optional] 
**quoteId** | **String** | Unique identifier for confirming this order. Use this value with /order/confirm place the order. | [optional] 
**shippingService** | **String** | Service identifier string pulled from a specific rate returned by /order/shipping. | [optional] 


