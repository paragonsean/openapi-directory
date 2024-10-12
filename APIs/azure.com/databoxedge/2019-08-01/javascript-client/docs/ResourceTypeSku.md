# DataBoxEdgeManagementClient.ResourceTypeSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersions** | **[String]** | The API versions in which SKU is available | [optional] [readonly] 
**costs** | [**[SkuCost]**](SkuCost.md) | The pricing info of the Sku. | [optional] [readonly] 
**family** | **String** | The Sku family | [optional] [readonly] 
**kind** | **String** | The Sku kind | [optional] [readonly] 
**locationInfo** | [**[SkuLocationInfo]**](SkuLocationInfo.md) | Availability of the SKU for the location/zone | [optional] [readonly] 
**locations** | **[String]** | Availability of the SKU for the region | [optional] [readonly] 
**name** | **String** | The Sku name | [optional] [readonly] 
**resourceType** | **String** | The type of the resource | [optional] [readonly] 
**restrictions** | [**[SkuRestriction]**](SkuRestriction.md) | Restrictions of the SKU availability. | [optional] [readonly] 
**tier** | **String** | The Sku tier | [optional] [readonly] 



## Enum: NameEnum


* `Gateway` (value: `"Gateway"`)

* `Edge` (value: `"Edge"`)

* `TEA_1Node` (value: `"TEA_1Node"`)

* `TEA_1Node_UPS` (value: `"TEA_1Node_UPS"`)

* `TEA_1Node_Heater` (value: `"TEA_1Node_Heater"`)

* `TEA_1Node_UPS_Heater` (value: `"TEA_1Node_UPS_Heater"`)

* `TEA_4Node_Heater` (value: `"TEA_4Node_Heater"`)

* `TEA_4Node_UPS_Heater` (value: `"TEA_4Node_UPS_Heater"`)

* `TMA` (value: `"TMA"`)





## Enum: TierEnum


* `Standard` (value: `"Standard"`)




