

# EnvironmentSettingProperties

Properties of an environment setting

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationState** | [**ConfigurationStateEnum**](#ConfigurationStateEnum) | Describes the user&#39;s progress in configuring their environment setting |  [optional] |
|**description** | **String** | Describes the environment and its resource settings |  [optional] |
|**lastChanged** | **OffsetDateTime** | Time when the template VM was last changed. |  [optional] [readonly] |
|**lastPublished** | **OffsetDateTime** | Time when the template VM was last sent for publishing. |  [optional] [readonly] |
|**latestOperationResult** | [**LatestOperationResult**](LatestOperationResult.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**publishingState** | [**PublishingStateEnum**](#PublishingStateEnum) | Describes the readiness of this environment setting |  [optional] [readonly] |
|**resourceSettings** | [**ResourceSettings**](ResourceSettings.md) |  |  |
|**title** | **String** | Brief title describing the environment and its resource settings |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |



## Enum: ConfigurationStateEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| COMPLETED | &quot;Completed&quot; |



## Enum: PublishingStateEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;Draft&quot; |
| PUBLISHING | &quot;Publishing&quot; |
| PUBLISHED | &quot;Published&quot; |
| PUBLISH_FAILED | &quot;PublishFailed&quot; |
| SCALING | &quot;Scaling&quot; |



