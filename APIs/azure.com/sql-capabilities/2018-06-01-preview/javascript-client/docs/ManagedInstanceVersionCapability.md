# SqlManagementClient.ManagedInstanceVersionCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The server version name. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedEditions** | [**[ManagedInstanceEditionCapability]**](ManagedInstanceEditionCapability.md) | The list of supported managed instance editions. | [optional] [readonly] 
**supportedInstancePoolEditions** | [**[InstancePoolEditionCapability]**](InstancePoolEditionCapability.md) | The list of supported instance pool editions. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




