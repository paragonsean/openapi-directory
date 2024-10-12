# AzureDataMigrationServiceResourceProvider.ServicesCheckNameAvailability200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | The localized reason why the name is not available, if nameAvailable is false | [optional] 
**nameAvailable** | **Boolean** | If true, the name is valid and available. If false, &#39;reason&#39; describes why not. | [optional] 
**reason** | **String** | The reason why the name is not available, if nameAvailable is false | [optional] 



## Enum: ReasonEnum


* `AlreadyExists` (value: `"AlreadyExists"`)

* `Invalid` (value: `"Invalid"`)




