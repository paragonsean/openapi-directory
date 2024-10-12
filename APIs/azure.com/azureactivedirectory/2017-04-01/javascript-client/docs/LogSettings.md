# Azureactivedirectory.LogSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Name of a Diagnostic Log category for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation. | [optional] 
**enabled** | **Boolean** | A value indicating whether this log is enabled. | 
**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  | [optional] 



## Enum: CategoryEnum


* `AuditLogs` (value: `"AuditLogs"`)

* `SignInLogs` (value: `"SignInLogs"`)




