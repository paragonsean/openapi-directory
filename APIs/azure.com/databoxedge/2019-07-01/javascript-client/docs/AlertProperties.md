# DataBoxEdgeManagementClient.AlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertType** | **String** | Alert type. | [optional] [readonly] 
**appearedAtDateTime** | **Date** | UTC time when the alert appeared. | [optional] [readonly] 
**detailedInformation** | **{String: String}** | Alert details. | [optional] [readonly] 
**errorDetails** | [**AlertErrorDetails**](AlertErrorDetails.md) |  | [optional] 
**recommendation** | **String** | Alert recommendation. | [optional] [readonly] 
**severity** | **String** | Severity of the alert. | [optional] [readonly] 
**title** | **String** | Alert title. | [optional] [readonly] 



## Enum: SeverityEnum


* `Informational` (value: `"Informational"`)

* `Warning` (value: `"Warning"`)

* `Critical` (value: `"Critical"`)




