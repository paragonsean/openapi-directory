# ContainerRegistryManagementClient.BuildProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildId** | **String** | The unique identifier for the build. | [optional] 
**buildTask** | **String** | The build task with which the build was started. | [optional] 
**buildType** | **String** | The type of build. | [optional] 
**createTime** | **Date** | The time the build was created. | [optional] 
**finishTime** | **Date** | The time the build finished. | [optional] 
**gitCommitTrigger** | [**GitCommitTrigger**](GitCommitTrigger.md) |  | [optional] 
**imageUpdateTrigger** | [**ImageUpdateTrigger**](ImageUpdateTrigger.md) |  | [optional] 
**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. | [optional] [default to false]
**lastUpdatedTime** | **Date** | The last updated time for the build. | [optional] 
**outputImages** | [**[ImageDescriptor]**](ImageDescriptor.md) | The list of all images that were generated from the build. | [optional] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of a build. | [optional] 
**startTime** | **Date** | The time the build started. | [optional] 
**status** | **String** | The current status of the build. | [optional] 



## Enum: BuildTypeEnum


* `AutoBuild` (value: `"AutoBuild"`)

* `QuickBuild` (value: `"QuickBuild"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: StatusEnum


* `Queued` (value: `"Queued"`)

* `Started` (value: `"Started"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Error` (value: `"Error"`)

* `Timeout` (value: `"Timeout"`)




