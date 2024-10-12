# DataShareManagementClient.ShareProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Time at which the share was created. | [optional] [readonly] 
**description** | **String** | Share description. | [optional] 
**provisioningState** | **String** | Gets or sets the provisioning state | [optional] [readonly] 
**shareKind** | **String** | Share kind. | [optional] 
**terms** | **String** | Share terms. | [optional] 
**userEmail** | **String** | Email of the user who created the resource | [optional] [readonly] 
**userName** | **String** | Name of the user who created the resource | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)

* `Failed` (value: `"Failed"`)





## Enum: ShareKindEnum


* `CopyBased` (value: `"CopyBased"`)

* `InPlace` (value: `"InPlace"`)




