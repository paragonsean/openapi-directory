# StorSimple8000SeriesManagementClient.AlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertType** | **String** | The type of the alert | 
**appearedAtSourceTime** | **Date** | The source time at which the alert was raised | 
**appearedAtTime** | **Date** | The UTC time at which the alert was raised | 
**clearedAtSourceTime** | **Date** | The source time at which the alert was cleared | [optional] 
**clearedAtTime** | **Date** | The UTC time at which the alert was cleared | [optional] 
**detailedInformation** | **{String: String}** | More details about the alert | [optional] 
**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  | [optional] 
**recommendation** | **String** | The recommended action for the issue raised in the alert | [optional] 
**resolutionReason** | **String** | The reason for resolving the alert | [optional] 
**scope** | **String** | The scope of the alert | 
**severity** | **String** | The severity of the alert | 
**source** | [**AlertSource**](AlertSource.md) |  | 
**status** | **String** | The current status of the alert | 
**title** | **String** | The title of the alert | 



## Enum: ScopeEnum


* `Resource` (value: `"Resource"`)

* `Device` (value: `"Device"`)





## Enum: SeverityEnum


* `Informational` (value: `"Informational"`)

* `Warning` (value: `"Warning"`)

* `Critical` (value: `"Critical"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Cleared` (value: `"Cleared"`)




