# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildbotCommandEvents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmUsage** | **String** | Indicates if and how Container Manager is being used for task execution. | [optional] 
**dockerCacheHit** | **Boolean** | Indicates whether we are using a cached Docker image (true) or had to pull the Docker image (false) for this command. | [optional] 
**dockerImageName** | **String** | Docker Image name. | [optional] 
**inputCacheMissBytes** | **Number** | The input cache miss rate as a fraction of the total size of input files. | [optional] 
**inputCacheMissFiles** | **Number** | The input cache miss rate as a fraction of the number of input files. | [optional] 
**numErrors** | **String** | The number of errors reported. | [optional] 
**numWarnings** | **String** | The number of warnings reported. | [optional] 
**outputLocation** | **String** | Indicates whether output files and/or output directories were found relative to the execution root or to the user provided work directory or both or none. | [optional] 
**usedAsyncContainer** | **Boolean** | Indicates whether an asynchronous container was used for execution. | [optional] 



## Enum: CmUsageEnum


* `NONE` (value: `"CONFIG_NONE"`)

* `MATCH` (value: `"CONFIG_MATCH"`)

* `MISMATCH` (value: `"CONFIG_MISMATCH"`)





## Enum: OutputLocationEnum


* `UNDEFINED` (value: `"LOCATION_UNDEFINED"`)

* `NONE` (value: `"LOCATION_NONE"`)

* `EXEC_ROOT_RELATIVE` (value: `"LOCATION_EXEC_ROOT_RELATIVE"`)

* `WORKING_DIR_RELATIVE` (value: `"LOCATION_WORKING_DIR_RELATIVE"`)

* `EXEC_ROOT_AND_WORKING_DIR_RELATIVE` (value: `"LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE"`)

* `EXEC_ROOT_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR` (value: `"LOCATION_EXEC_ROOT_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR"`)

* `EXEC_ROOT_AND_WORKING_DIR_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR` (value: `"LOCATION_EXEC_ROOT_AND_WORKING_DIR_RELATIVE_OUTPUT_OUTSIDE_WORKING_DIR"`)




