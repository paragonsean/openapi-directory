

# BuildFilter

Properties that are enabled for Odata querying.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildId** | **String** | The unique identifier for the build. |  [optional] |
|**buildTaskName** | **String** | The name of the build task that the build corresponds to. |  [optional] |
|**buildType** | [**BuildTypeEnum**](#BuildTypeEnum) | The type of build. |  [optional] |
|**createTime** | **OffsetDateTime** | The create time for a build. |  [optional] |
|**finishTime** | **OffsetDateTime** | The time the build finished. |  [optional] |
|**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. |  [optional] |
|**outputImageManifests** | **String** | The list of comma-separated image manifests that were generated from the build. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the build. |  [optional] |



## Enum: BuildTypeEnum

| Name | Value |
|---- | -----|
| AUTO_BUILD | &quot;AutoBuild&quot; |
| QUICK_BUILD | &quot;QuickBuild&quot; |



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



