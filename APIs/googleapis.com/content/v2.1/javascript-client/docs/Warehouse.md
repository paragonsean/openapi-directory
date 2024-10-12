# ContentApiForShopping.Warehouse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessDayConfig** | [**BusinessDayConfig**](BusinessDayConfig.md) |  | [optional] 
**cutoffTime** | [**WarehouseCutoffTime**](WarehouseCutoffTime.md) |  | [optional] 
**handlingDays** | **String** | Required. The number of days it takes for this warehouse to pack up and ship an item. This is on the warehouse level, but can be overridden on the offer level based on the attributes of an item. | [optional] 
**name** | **String** | Required. The name of the warehouse. Must be unique within account. | [optional] 
**shippingAddress** | [**Address**](Address.md) |  | [optional] 


