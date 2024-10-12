# AzureLogAnalytics.WorkspaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerId** | **String** | This is a read-only property. Represents the ID associated with the workspace. | [optional] [readonly] 
**portalUrl** | **String** | This is a legacy property and is not used anymore. Kept here for backward compatibility. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the workspace. | [optional] 
**retentionInDays** | **Number** | The workspace data retention in days. -1 means Unlimited retention for the Unlimited Sku. 730 days is the maximum allowed for all other Skus.  | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**source** | **String** | This is a read-only legacy property. It is always set to &#39;Azure&#39; by the service. Kept here for backward compatibility. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Deleting` (value: `"Deleting"`)

* `ProvisioningAccount` (value: `"ProvisioningAccount"`)




