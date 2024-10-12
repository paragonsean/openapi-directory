

# TargetRender

Details of rendering for a single target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | Output only. Reason this render failed. This will always be unspecified while the render in progress. |  [optional] [readonly] |
|**failureMessage** | **String** | Output only. Additional information about the render failure, if available. |  [optional] [readonly] |
|**metadata** | [**RenderMetadata**](RenderMetadata.md) |  |  [optional] |
|**renderingBuild** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to render the manifest for this target. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. |  [optional] [readonly] |
|**renderingState** | [**RenderingStateEnum**](#RenderingStateEnum) | Output only. Current state of the render operation for this Target. |  [optional] [readonly] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| FAILURE_CAUSE_UNSPECIFIED | &quot;FAILURE_CAUSE_UNSPECIFIED&quot; |
| CLOUD_BUILD_UNAVAILABLE | &quot;CLOUD_BUILD_UNAVAILABLE&quot; |
| EXECUTION_FAILED | &quot;EXECUTION_FAILED&quot; |
| CLOUD_BUILD_REQUEST_FAILED | &quot;CLOUD_BUILD_REQUEST_FAILED&quot; |
| VERIFICATION_CONFIG_NOT_FOUND | &quot;VERIFICATION_CONFIG_NOT_FOUND&quot; |
| CUSTOM_ACTION_NOT_FOUND | &quot;CUSTOM_ACTION_NOT_FOUND&quot; |
| DEPLOYMENT_STRATEGY_NOT_SUPPORTED | &quot;DEPLOYMENT_STRATEGY_NOT_SUPPORTED&quot; |
| RENDER_FEATURE_NOT_SUPPORTED | &quot;RENDER_FEATURE_NOT_SUPPORTED&quot; |



## Enum: RenderingStateEnum

| Name | Value |
|---- | -----|
| TARGET_RENDER_STATE_UNSPECIFIED | &quot;TARGET_RENDER_STATE_UNSPECIFIED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |



