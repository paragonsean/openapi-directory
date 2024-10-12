# StorSimpleManagementClient.AlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertType** | **String** | Type of the alert | 
**appearedAtSourceTime** | **Date** | UTC time at which the alert appeared on the source | 
**appearedAtTime** | **Date** | UTC time at which the alert appeared | 
**clearedAtSourceTime** | **Date** | UTC time at which the alert was cleared on the source | [optional] 
**clearedAtTime** | **Date** | UTC time at which the alert got cleared | [optional] 
**detailedInformation** | **{String: String}** | Other information about the alert | [optional] 
**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  | [optional] 
**recommendation** | **String** | Recommendation for acting on the alert | [optional] 
**resolutionReason** | **String** | Reason for resolving the alert | [optional] 
**scope** | **String** | Device or Resource alert | 
**severity** | **String** | Severity of the alert | 
**source** | [**AlertSource**](AlertSource.md) |  | 
**status** | **String** | Current status of the alert | 
**title** | **String** | Title of the alert | 



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




