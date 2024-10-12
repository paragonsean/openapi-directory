# SqlManagementClient.LocationCapabilities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The location name. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedServerVersions** | [**[ServerVersionCapability]**](ServerVersionCapability.md) | The list of supported server versions. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




