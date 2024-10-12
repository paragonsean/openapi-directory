# ServiceConsumerManagementApi.ClientLibrarySettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cppSettings** | [**CppSettings**](CppSettings.md) |  | [optional] 
**dotnetSettings** | [**DotnetSettings**](DotnetSettings.md) |  | [optional] 
**goSettings** | [**GoSettings**](GoSettings.md) |  | [optional] 
**javaSettings** | [**JavaSettings**](JavaSettings.md) |  | [optional] 
**launchStage** | **String** | Launch stage of this version of the API. | [optional] 
**nodeSettings** | [**NodeSettings**](NodeSettings.md) |  | [optional] 
**phpSettings** | [**PhpSettings**](PhpSettings.md) |  | [optional] 
**pythonSettings** | [**PythonSettings**](PythonSettings.md) |  | [optional] 
**restNumericEnums** | **Boolean** | When using transport&#x3D;rest, the client request will encode enums as numbers rather than strings. | [optional] 
**rubySettings** | [**RubySettings**](RubySettings.md) |  | [optional] 
**version** | **String** | Version of the API to apply these settings to. This is the full protobuf package for the API, ending in the version element. Examples: \&quot;google.cloud.speech.v1\&quot; and \&quot;google.spanner.admin.database.v1\&quot;. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




