# DataShareManagementClient.ShareSubscriptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Time at which the share subscription was created. | [optional] [readonly] 
**invitationId** | **String** | The invitation id. | 
**providerEmail** | **String** | Email of the provider who created the resource | [optional] [readonly] 
**providerName** | **String** | Name of the provider who created the resource | [optional] [readonly] 
**providerTenantName** | **String** | Tenant name of the provider who created the resource | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the share subscription | [optional] [readonly] 
**shareDescription** | **String** | Description of share | [optional] [readonly] 
**shareKind** | **String** | Kind of share | [optional] [readonly] 
**shareName** | **String** | Name of the share | [optional] [readonly] 
**shareSubscriptionStatus** | **String** | Gets the current status of share subscription. | [optional] [readonly] 
**shareTerms** | **String** | Terms of a share | [optional] [readonly] 
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





## Enum: ShareSubscriptionStatusEnum


* `Active` (value: `"Active"`)

* `Revoked` (value: `"Revoked"`)

* `SourceDeleted` (value: `"SourceDeleted"`)

* `Revoking` (value: `"Revoking"`)




