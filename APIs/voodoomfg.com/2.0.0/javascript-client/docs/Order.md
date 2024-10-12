# VoodooManufacturing3DPrintApi.Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerContactEmail** | **String** | Customer&#39;s email address. | [optional] 
**customerName** | **String** | Customer&#39;s name. | [optional] 
**id** | **Number** | Unique identifier for this order. Reference should be displayed and used for lookups instead of this field. | [optional] 
**notes** | **String** | The notes field that was submitted with this order. | [optional] 
**prints** | [**[OrderPrint]**](OrderPrint.md) |  | [optional] 
**reference** | **String** | Unique identifier for this order. Used to retrieve info for a specific order from /order/{order_id}. | [optional] 
**shipBy** | **String** | Planned ship date for this order. | [optional] 
**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 


