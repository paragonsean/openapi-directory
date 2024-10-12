

# ResourceTypeSku

SkuInformation object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersions** | **List&lt;String&gt;** | The API versions in which SKU is available |  [optional] [readonly] |
|**costs** | [**List&lt;SkuCost&gt;**](SkuCost.md) | The pricing info of the Sku. |  [optional] [readonly] |
|**family** | **String** | The Sku family |  [optional] [readonly] |
|**kind** | **String** | The Sku kind |  [optional] [readonly] |
|**locationInfo** | [**List&lt;SkuLocationInfo&gt;**](SkuLocationInfo.md) | Availability of the SKU for the location/zone |  [optional] [readonly] |
|**locations** | **List&lt;String&gt;** | Availability of the SKU for the region |  [optional] [readonly] |
|**name** | [**NameEnum**](#NameEnum) | The Sku name |  [optional] [readonly] |
|**resourceType** | **String** | The type of the resource |  [optional] [readonly] |
|**restrictions** | [**List&lt;SkuRestriction&gt;**](SkuRestriction.md) | Restrictions of the SKU availability. |  [optional] [readonly] |
|**tier** | [**TierEnum**](#TierEnum) | The Sku tier |  [optional] [readonly] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| GATEWAY | &quot;Gateway&quot; |
| EDGE | &quot;Edge&quot; |
| TEA_1_NODE | &quot;TEA_1Node&quot; |
| TEA_1_NODE_UPS | &quot;TEA_1Node_UPS&quot; |
| TEA_1_NODE_HEATER | &quot;TEA_1Node_Heater&quot; |
| TEA_1_NODE_UPS_HEATER | &quot;TEA_1Node_UPS_Heater&quot; |
| TEA_4_NODE_HEATER | &quot;TEA_4Node_Heater&quot; |
| TEA_4_NODE_UPS_HEATER | &quot;TEA_4Node_UPS_Heater&quot; |
| TMA | &quot;TMA&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |



