

# EntryPoint

A configuration that defines how a deployment is accessed externally.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addOn** | [**GoogleAppsScriptTypeAddOnEntryPoint**](GoogleAppsScriptTypeAddOnEntryPoint.md) |  |  [optional] |
|**entryPointType** | [**EntryPointTypeEnum**](#EntryPointTypeEnum) | The type of the entry point. |  [optional] |
|**executionApi** | [**GoogleAppsScriptTypeExecutionApiEntryPoint**](GoogleAppsScriptTypeExecutionApiEntryPoint.md) |  |  [optional] |
|**webApp** | [**GoogleAppsScriptTypeWebAppEntryPoint**](GoogleAppsScriptTypeWebAppEntryPoint.md) |  |  [optional] |



## Enum: EntryPointTypeEnum

| Name | Value |
|---- | -----|
| ENTRY_POINT_TYPE_UNSPECIFIED | &quot;ENTRY_POINT_TYPE_UNSPECIFIED&quot; |
| WEB_APP | &quot;WEB_APP&quot; |
| EXECUTION_API | &quot;EXECUTION_API&quot; |
| ADD_ON | &quot;ADD_ON&quot; |



