

# Sku

SKU parameters supplied to the create Redis operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4). |  |
|**family** | [**FamilyEnum**](#FamilyEnum) | The SKU family to use. Valid values: (C, P). (C &#x3D; Basic/Standard, P &#x3D; Premium). |  |
|**name** | [**NameEnum**](#NameEnum) | The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium) |  |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| C | &quot;C&quot; |
| P | &quot;P&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



