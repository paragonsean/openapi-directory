

# Sku

SKU parameters supplied to the create Redis operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | What size of Redis cache to deploy. Valid values: for C family (0, 1, 2, 3, 4, 5, 6), for P family (1, 2, 3, 4). |  |
|**family** | [**FamilyEnum**](#FamilyEnum) | Which family to use. Valid values: (C, P). |  |
|**name** | [**NameEnum**](#NameEnum) | What type of Redis cache to deploy. Valid values: (Basic, Standard, Premium). |  |



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



