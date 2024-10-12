# DevTestLabsClient.LabAnnouncementProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **String** | Is the lab announcement active/enabled at this time? | [optional] 
**expirationDate** | **Date** | The time at which the announcement expires (null for never) | [optional] 
**expired** | **Boolean** | Has this announcement expired? | [optional] 
**markdown** | **String** | The markdown text (if any) that this lab displays in the UI. If left empty/null, nothing will be shown. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] [readonly] 
**title** | **String** | The plain text title for the lab announcement | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] [readonly] 



## Enum: EnabledEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




