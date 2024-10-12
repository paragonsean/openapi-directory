# SqlManagementClient.ServerVersionCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The server version name. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedEditions** | [**[EditionCapability]**](EditionCapability.md) | The list of supported database editions. | [optional] [readonly] 
**supportedElasticPoolEditions** | [**[ElasticPoolEditionCapability]**](ElasticPoolEditionCapability.md) | The list of supported elastic pool editions. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




