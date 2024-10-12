

# Sku

Billing information related properties of a server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The scale up/out capacity, representing server&#39;s compute units. |  [optional] |
|**family** | **String** | The family of hardware. |  [optional] |
|**name** | **String** | The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8. |  [optional] |
|**size** | **String** | The size code, to be interpreted by resource as appropriate. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the particular SKU, e.g. Basic. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| GENERAL_PURPOSE | &quot;GeneralPurpose&quot; |
| MEMORY_OPTIMIZED | &quot;MemoryOptimized&quot; |



