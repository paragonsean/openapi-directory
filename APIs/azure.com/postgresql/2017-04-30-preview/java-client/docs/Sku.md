

# Sku

Billing information related properties of a server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The scale up/out capacity, representing server&#39;s compute units. |  [optional] |
|**family** | **String** | The family of hardware. |  [optional] |
|**name** | **String** | The name of the sku, typically, a letter + Number code, e.g. P3. |  [optional] |
|**size** | **String** | The size code, to be interpreted by resource as appropriate. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the particular SKU, e.g. Basic. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |



