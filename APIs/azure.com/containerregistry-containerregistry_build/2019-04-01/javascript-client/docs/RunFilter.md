# ContainerRegistryManagementClient.RunFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **Date** | The create time for a run. | [optional] 
**finishTime** | **Date** | The time the run finished. | [optional] 
**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. | [optional] 
**outputImageManifests** | **String** | The list of comma-separated image manifests that were generated from the run. This is applicable if the run is of  build type. | [optional] 
**runId** | **String** | The unique identifier for the run. | [optional] 
**runType** | **String** | The type of run. | [optional] 
**status** | **String** | The current status of the run. | [optional] 
**taskName** | **String** | The name of the task that the run corresponds to. | [optional] 



## Enum: RunTypeEnum


* `QuickBuild` (value: `"QuickBuild"`)

* `QuickRun` (value: `"QuickRun"`)

* `AutoBuild` (value: `"AutoBuild"`)

* `AutoRun` (value: `"AutoRun"`)





## Enum: StatusEnum


* `Queued` (value: `"Queued"`)

* `Started` (value: `"Started"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Error` (value: `"Error"`)

* `Timeout` (value: `"Timeout"`)




