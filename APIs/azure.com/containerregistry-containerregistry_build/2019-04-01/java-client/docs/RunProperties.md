

# RunProperties

The properties for a run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  |  [optional] |
|**createTime** | **OffsetDateTime** | The time the run was scheduled. |  [optional] |
|**customRegistries** | **List&lt;String&gt;** | The list of custom registries that were logged in during this run. |  [optional] |
|**finishTime** | **OffsetDateTime** | The time the run finished. |  [optional] |
|**imageUpdateTrigger** | [**ImageUpdateTrigger**](ImageUpdateTrigger.md) |  |  [optional] |
|**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | The last updated time for the run. |  [optional] |
|**outputImages** | [**List&lt;ImageDescriptor&gt;**](ImageDescriptor.md) | The list of all images that were generated from the run. This is applicable if the run generates base image dependencies. |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of a run. |  [optional] |
|**runErrorMessage** | **String** | The error message received from backend systems after the run is scheduled. |  [optional] [readonly] |
|**runId** | **String** | The unique identifier for the run. |  [optional] |
|**runType** | [**RunTypeEnum**](#RunTypeEnum) | The type of run. |  [optional] |
|**sourceRegistryAuth** | **String** | The scope of the credentials that were used to login to the source registry during this run. |  [optional] |
|**sourceTrigger** | [**SourceTriggerDescriptor**](SourceTriggerDescriptor.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The time the run started. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the run. |  [optional] |
|**task** | **String** | The task against which run was scheduled. |  [optional] |
|**timerTrigger** | [**TimerTriggerDescriptor**](TimerTriggerDescriptor.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: RunTypeEnum

| Name | Value |
|---- | -----|
| QUICK_BUILD | &quot;QuickBuild&quot; |
| QUICK_RUN | &quot;QuickRun&quot; |
| AUTO_BUILD | &quot;AutoBuild&quot; |
| AUTO_RUN | &quot;AutoRun&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;Queued&quot; |
| STARTED | &quot;Started&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| ERROR | &quot;Error&quot; |
| TIMEOUT | &quot;Timeout&quot; |



