

# Provider

Provider indicates the owner who provides the connectors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**description** | **String** | Output only. Description of the resource. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Display name. |  [optional] [readonly] |
|**documentationUri** | **String** | Output only. Link to documentation page. |  [optional] [readonly] |
|**externalUri** | **String** | Output only. Link to external page. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] [readonly] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Output only. Flag to mark the version indicating the launch stage. |  [optional] [readonly] |
|**name** | **String** | Output only. Resource name of the Provider. Format: projects/{project}/locations/{location}/providers/{provider} Only global location is supported for Provider resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |
|**webAssetsLocation** | **String** | Output only. Cloud storage location of icons etc consumed by UI. |  [optional] [readonly] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| PREVIEW | &quot;PREVIEW&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| PRIVATE_PREVIEW | &quot;PRIVATE_PREVIEW&quot; |



