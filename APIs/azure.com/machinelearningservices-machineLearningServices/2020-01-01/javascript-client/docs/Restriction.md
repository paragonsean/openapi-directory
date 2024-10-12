# AzureMachineLearningWorkspaces.Restriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasonCode** | **String** | The reason for the restriction. | [optional] 
**type** | **String** | The type of restrictions. As of now only possible value for this is location. | [optional] [readonly] 
**values** | **[String]** | The value of restrictions. If the restriction type is set to location. This would be different locations where the SKU is restricted. | [optional] [readonly] 



## Enum: ReasonCodeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `NotAvailableForRegion` (value: `"NotAvailableForRegion"`)

* `NotAvailableForSubscription` (value: `"NotAvailableForSubscription"`)




