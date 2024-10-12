

# GoogleDevtoolsRemotebuildbotCommandEvents

CommandEvents contains counters for the number of warnings and errors that occurred during the execution of a command.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cmUsage** | [**CmUsageEnum**](#CmUsageEnum) | Indicates if and how Container Manager is being used for task execution. |  [optional] |
|**dockerCacheHit** | **Boolean** | Indicates whether we are using a cached Docker image (true) or had to pull the Docker image (false) for this command. |  [optional] |
|**dockerImageName** | **String** | Docker Image name. |  [optional] |
|**inputCacheMissBytes** | **Float** | The input cache miss rate as a fraction of the total size of input files. |  [optional] |
|**inputCacheMissFiles** | **Float** | The input cache miss rate as a fraction of the number of input files. |  [optional] |
|**numErrors** | **String** | The number of errors reported. |  [optional] |
|**numWarnings** | **String** | The number of warnings reported. |  [optional] |
|**outputLocation** | [**OutputLocationEnum**](#OutputLocationEnum) | Indicates whether output files and/or output directories were found relative to the execution root or to the user provided work directory or both or none. |  [optional] |
|**usedAsyncContainer** | **Boolean** | Indicates whether an asynchronous container was used for execution. |  [optional] |



## Enum: CmUsageEnum

| Name | Value |
|---- | -----|
| NONE | &quot;CONFIG_NONE&quot; |
| MATCH | &quot;CONFIG_MATCH&quot; |
| MISMATCH | &quot;CONFIG_MISMATCH&quot; |



## Enum: OutputLocationEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;LOCATION_UNDEFINED&quot; |
| NONE | &quot;LOCATION_NONE&quot; |
| EXEC_ROOT_RELATIVE | &quot;LOCATION_EXEC_ROOT_RELATIVE&quot; |
| WORKING_DIR_RELATIVE | &quot;LOCATION_WORKING_DIR_RELATIVE&quot; |
| EXEC_ROOT_AND_WORKING_DIR_RELATIVE | &quot;LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE&quot; |
| EXEC_ROOT_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR | &quot;LOCATION_EXEC_ROOT_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR&quot; |
| EXEC_ROOT_AND_WORKING_DIR_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR | &quot;LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR&quot; |



