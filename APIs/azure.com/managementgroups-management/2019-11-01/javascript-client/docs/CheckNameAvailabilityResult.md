# ManagementGroups.CheckNameAvailabilityResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Required if nameAvailable &#x3D;&#x3D; false. Localized. If reason &#x3D;&#x3D; invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason &#x3D;&#x3D; AlreadyExists, explain that is already in use, and direct them to select a different name. | [optional] [readonly] 
**nameAvailable** | **Boolean** | Required. True indicates name is valid and available. False indicates the name is invalid, unavailable, or both. | [optional] [readonly] 
**reason** | **String** | Required if nameAvailable &#x3D;&#x3D; false. Invalid indicates the name provided does not match the resource provider&#39;s naming requirements (incorrect length, unsupported characters, etc.) AlreadyExists indicates that the name is already in use and is therefore unavailable. | [optional] [readonly] 



## Enum: ReasonEnum


* `Invalid` (value: `"Invalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




