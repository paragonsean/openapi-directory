

# RunFilter

Properties that are enabled for Odata querying on runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **OffsetDateTime** | The create time for a run. |  [optional] |
|**finishTime** | **OffsetDateTime** | The time the run finished. |  [optional] |
|**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. |  [optional] |
|**outputImageManifests** | **String** | The list of comma-separated image manifests that were generated from the run. This is applicable if the run is of  build type. |  [optional] |
|**runId** | **String** | The unique identifier for the run. |  [optional] |
|**runType** | [**RunTypeEnum**](#RunTypeEnum) | The type of run. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the run. |  [optional] |
|**taskName** | **String** | The name of the task that the run corresponds to. |  [optional] |



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



