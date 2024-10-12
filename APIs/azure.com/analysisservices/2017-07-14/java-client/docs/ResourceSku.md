

# ResourceSku

Represents the SKU name and Azure pricing tier for Analysis Services resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the SKU level. |  |
|**tier** | [**TierEnum**](#TierEnum) | The name of the Azure pricing tier to which the SKU applies. |  [optional] |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| DEVELOPMENT | &quot;Development&quot; |
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |



