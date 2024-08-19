# IncreaseApi.RoutingNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achTransfers** | **String** | This routing number&#39;s support for ACH Transfers. | 
**name** | **String** | The name of the financial institution belonging to a routing number. | 
**realTimePaymentsTransfers** | **String** | This routing number&#39;s support for Real Time Payments Transfers. | 
**routingNumber** | **String** | The nine digit routing number identifier. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;routing_number&#x60;. | 
**wireTransfers** | **String** | This routing number&#39;s support for Wire Transfers. | 



## Enum: AchTransfersEnum


* `supported` (value: `"supported"`)

* `not_supported` (value: `"not_supported"`)





## Enum: RealTimePaymentsTransfersEnum


* `supported` (value: `"supported"`)

* `not_supported` (value: `"not_supported"`)





## Enum: TypeEnum


* `routing_number` (value: `"routing_number"`)





## Enum: WireTransfersEnum


* `supported` (value: `"supported"`)

* `not_supported` (value: `"not_supported"`)




