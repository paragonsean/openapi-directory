# ComputeManagementClient.ResourceSkuRestrictions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasonCode** | **String** | The reason for restriction. | [optional] [readonly] 
**restrictionInfo** | [**ResourceSkuRestrictionInfo**](ResourceSkuRestrictionInfo.md) |  | [optional] 
**type** | **String** | The type of restrictions. | [optional] [readonly] 
**values** | **[String]** | The value of restrictions. If the restriction type is set to location. This would be different locations where the SKU is restricted. | [optional] [readonly] 



## Enum: ReasonCodeEnum


* `QuotaId` (value: `"QuotaId"`)

* `NotAvailableForSubscription` (value: `"NotAvailableForSubscription"`)





## Enum: TypeEnum


* `Location` (value: `"Location"`)

* `Zone` (value: `"Zone"`)




