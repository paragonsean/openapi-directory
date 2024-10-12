

# BuildProperties

The properties for a build.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildId** | **String** | The unique identifier for the build. |  [optional] |
|**buildTask** | **String** | The build task with which the build was started. |  [optional] |
|**buildType** | [**BuildTypeEnum**](#BuildTypeEnum) | The type of build. |  [optional] |
|**createTime** | **OffsetDateTime** | The time the build was created. |  [optional] |
|**finishTime** | **OffsetDateTime** | The time the build finished. |  [optional] |
|**gitCommitTrigger** | [**GitCommitTrigger**](GitCommitTrigger.md) |  |  [optional] |
|**imageUpdateTrigger** | [**ImageUpdateTrigger**](ImageUpdateTrigger.md) |  |  [optional] |
|**isArchiveEnabled** | **Boolean** | The value that indicates whether archiving is enabled or not. |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | The last updated time for the build. |  [optional] |
|**outputImages** | [**List&lt;ImageDescriptor&gt;**](ImageDescriptor.md) | The list of all images that were generated from the build. |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of a build. |  [optional] |
|**startTime** | **OffsetDateTime** | The time the build started. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the build. |  [optional] |



## Enum: BuildTypeEnum

| Name | Value |
|---- | -----|
| AUTO_BUILD | &quot;AutoBuild&quot; |
| QUICK_BUILD | &quot;QuickBuild&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



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



