# ContainerRegistryManagementClient.RunProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  | [optional] 
**createTime** | **Date** | The time the run was scheduled. | [optional] 
**customRegistries** | **[String]** | The list of custom registries that were logged in during this run. | [optional] 
**finishTime** | **Date** | The time the run finished. | [optional] 
**imageUpdateTrigger** | [**ImageUpdateTrigger**](ImageUpdateTrigger.md) |  | [optional] 
**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. | [optional] [default to false]
**lastUpdatedTime** | **Date** | The last updated time for the run. | [optional] 
**outputImages** | [**[ImageDescriptor]**](ImageDescriptor.md) | The list of all images that were generated from the run. This is applicable if the run generates base image dependencies. | [optional] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | [optional] 
**provisioningState** | **String** | The provisioning state of a run. | [optional] 
**runErrorMessage** | **String** | The error message received from backend systems after the run is scheduled. | [optional] [readonly] 
**runId** | **String** | The unique identifier for the run. | [optional] 
**runType** | **String** | The type of run. | [optional] 
**sourceRegistryAuth** | **String** | The scope of the credentials that were used to login to the source registry during this run. | [optional] 
**sourceTrigger** | [**SourceTriggerDescriptor**](SourceTriggerDescriptor.md) |  | [optional] 
**startTime** | **Date** | The time the run started. | [optional] 
**status** | **String** | The current status of the run. | [optional] 
**task** | **String** | The task against which run was scheduled. | [optional] 
**timerTrigger** | [**TimerTriggerDescriptor**](TimerTriggerDescriptor.md) |  | [optional] 
**updateTriggerToken** | **String** | The update trigger token passed for the Run. | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





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




