# ContainerRegistryManagementClient.BuildFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildId** | **String** | The unique identifier for the build. | [optional] 
**buildTaskName** | **String** | The name of the build task that the build corresponds to. | [optional] 
**buildType** | **String** | The type of build. | [optional] 
**createTime** | **Date** | The create time for a build. | [optional] 
**finishTime** | **Date** | The time the build finished. | [optional] 
**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. | [optional] 
**outputImageManifests** | **String** | The list of comma-separated image manifests that were generated from the build. | [optional] 
**status** | **String** | The current status of the build. | [optional] 



## Enum: BuildTypeEnum


* `AutoBuild` (value: `"AutoBuild"`)

* `QuickBuild` (value: `"QuickBuild"`)





## Enum: StatusEnum


* `Queued` (value: `"Queued"`)

* `Started` (value: `"Started"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Error` (value: `"Error"`)

* `Timeout` (value: `"Timeout"`)




