# PostgreSqlManagementClient.Sku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Number** | The scale up/out capacity, representing server&#39;s compute units. | [optional] 
**family** | **String** | The family of hardware. | [optional] 
**name** | **String** | The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8. | [optional] 
**size** | **String** | The size code, to be interpreted by resource as appropriate. | [optional] 
**tier** | **String** | The tier of the particular SKU, e.g. Basic. | [optional] 



## Enum: TierEnum


* `Basic` (value: `"Basic"`)

* `GeneralPurpose` (value: `"GeneralPurpose"`)

* `MemoryOptimized` (value: `"MemoryOptimized"`)




