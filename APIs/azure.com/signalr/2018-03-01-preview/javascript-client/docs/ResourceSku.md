# SignalRManagementClient.ResourceSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Number** | Optional, integer. If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not   possible for the resource this may be omitted. | [optional] 
**family** | **String** | Optional, string. If the service has different generations of hardware, for the same SKU, then that can be captured here. | [optional] 
**name** | **String** | The name of the SKU. This is typically a letter + number code, such as A0 or P3.  Required (if sku is specified) | 
**size** | **String** | Optional, string. When the name field is the combination of tier and some other value, this would be the standalone code. | [optional] 
**tier** | **String** | Optional tier of this particular SKU. &#x60;Basic&#x60; is deprecated, use &#x60;Standard&#x60; instead for Basic tier | [optional] 



## Enum: TierEnum


* `Free` (value: `"Free"`)

* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




