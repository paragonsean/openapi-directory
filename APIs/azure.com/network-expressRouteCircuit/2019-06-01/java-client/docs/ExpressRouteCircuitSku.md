

# ExpressRouteCircuitSku

Contains SKU in an ExpressRouteCircuit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**family** | [**FamilyEnum**](#FamilyEnum) | The family of the SKU. |  [optional] |
|**name** | **String** | The name of the SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the SKU. |  [optional] |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| UNLIMITED_DATA | &quot;UnlimitedData&quot; |
| METERED_DATA | &quot;MeteredData&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| BASIC | &quot;Basic&quot; |
| LOCAL | &quot;Local&quot; |



