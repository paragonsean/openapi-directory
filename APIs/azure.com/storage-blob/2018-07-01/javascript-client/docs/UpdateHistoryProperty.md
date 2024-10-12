# StorageManagementClient.UpdateHistoryProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**immutabilityPeriodSinceCreationInDays** | **Number** | The immutability period for the blobs in the container since the policy creation, in days. | [optional] [readonly] 
**objectIdentifier** | **String** | Returns the Object ID of the user who updated the ImmutabilityPolicy. | [optional] [readonly] 
**tenantId** | **String** | Returns the Tenant ID that issued the token for the user who updated the ImmutabilityPolicy. | [optional] [readonly] 
**timestamp** | **Date** | Returns the date and time the ImmutabilityPolicy was updated. | [optional] [readonly] 
**update** | **String** | The ImmutabilityPolicy update type of a blob container, possible values include: put, lock and extend. | [optional] [readonly] 
**upn** | **String** | Returns the User Principal Name of the user who updated the ImmutabilityPolicy. | [optional] [readonly] 



## Enum: UpdateEnum


* `put` (value: `"put"`)

* `lock` (value: `"lock"`)

* `extend` (value: `"extend"`)




