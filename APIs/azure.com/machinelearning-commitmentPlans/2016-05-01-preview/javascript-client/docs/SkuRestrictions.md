# AzureMlCommitmentPlansManagementClient.SkuRestrictions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasonCode** | **String** | The reason for restriction. | [optional] [readonly] 
**type** | **String** | The type of restrictions. | [optional] [readonly] 
**values** | **[String]** | The value of restrictions. If the restriction type is set to location. This would be different locations where the SKU is restricted. | [optional] [readonly] 



## Enum: ReasonCodeEnum


* `QuotaId` (value: `"QuotaId"`)

* `NotAvailableForSubscription` (value: `"NotAvailableForSubscription"`)





## Enum: TypeEnum


* `location` (value: `"location"`)

* `zone` (value: `"zone"`)




