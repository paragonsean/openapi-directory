# CloudLoggingApi.DefaultSinkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**[LogExclusion]**](LogExclusion.md) | Optional. Specifies the set of exclusions to be added to the _Default sink in newly created resource containers. | [optional] 
**filter** | **String** | Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter.For example:logName&#x3D;\&quot;projects/[PROJECT_ID]/logs/[LOG_ID]\&quot; AND severity&gt;&#x3D;ERRORTo match all logs, don&#39;t add exclusions and use the following line as the value of filter:logName:*Cannot be empty or unset when the value of mode is OVERWRITE. | [optional] 
**mode** | **String** | Required. Determines the behavior to apply to the built-in _Default sink inclusion filter.Exclusions are always appended, as built-in _Default sinks have no exclusions. | [optional] 



## Enum: ModeEnum


* `FILTER_WRITE_MODE_UNSPECIFIED` (value: `"FILTER_WRITE_MODE_UNSPECIFIED"`)

* `APPEND` (value: `"APPEND"`)

* `OVERWRITE` (value: `"OVERWRITE"`)




