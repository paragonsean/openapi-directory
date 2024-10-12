

# TriggerChangeDetectionParameters

The parameters used when calling trigger change detection action on cloud endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeDetectionMode** | [**ChangeDetectionModeEnum**](#ChangeDetectionModeEnum) | Change Detection Mode. Applies to a directory specified in directoryPath parameter. |  [optional] |
|**directoryPath** | **String** | Relative path to a directory Azure File share for which change detection is to be performed. |  [optional] |
|**paths** | **List&lt;String&gt;** | Array of relative paths on the Azure File share to be included in the change detection. Can be files and directories. |  [optional] |



## Enum: ChangeDetectionModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| RECURSIVE | &quot;Recursive&quot; |



