

# ExpressRouteCircuitSku

Contains SKU in an ExpressRouteCircuit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**family** | [**FamilyEnum**](#FamilyEnum) | The family of the SKU. Possible values are: &#39;UnlimitedData&#39; and &#39;MeteredData&#39;. |  [optional] |
|**name** | **String** | The name of the SKU. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the SKU. Possible values are &#39;Standard&#39; and &#39;Premium&#39;. |  [optional] |



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



