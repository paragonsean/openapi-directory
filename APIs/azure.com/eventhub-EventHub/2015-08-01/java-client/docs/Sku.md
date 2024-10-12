

# Sku

SKU parameters supplied to the create Namespace operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The Event Hubs throughput units. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | Name of this SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The billing tier of this particular SKU. |  |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



