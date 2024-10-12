# SqlManagementClient.MaxSizeCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **Number** | The maximum size limit (see &#39;unit&#39; for the units). | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**unit** | **String** | The units that the limit is expressed in. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)





## Enum: UnitEnum


* `Megabytes` (value: `"Megabytes"`)

* `Gigabytes` (value: `"Gigabytes"`)

* `Terabytes` (value: `"Terabytes"`)

* `Petabytes` (value: `"Petabytes"`)




