# CloudDeployApi.TargetRender

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureCause** | **String** | Output only. Reason this render failed. This will always be unspecified while the render in progress. | [optional] [readonly] 
**failureMessage** | **String** | Output only. Additional information about the render failure, if available. | [optional] [readonly] 
**metadata** | [**RenderMetadata**](RenderMetadata.md) |  | [optional] 
**renderingBuild** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to render the manifest for this target. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. | [optional] [readonly] 
**renderingState** | **String** | Output only. Current state of the render operation for this Target. | [optional] [readonly] 



## Enum: FailureCauseEnum


* `FAILURE_CAUSE_UNSPECIFIED` (value: `"FAILURE_CAUSE_UNSPECIFIED"`)

* `CLOUD_BUILD_UNAVAILABLE` (value: `"CLOUD_BUILD_UNAVAILABLE"`)

* `EXECUTION_FAILED` (value: `"EXECUTION_FAILED"`)

* `CLOUD_BUILD_REQUEST_FAILED` (value: `"CLOUD_BUILD_REQUEST_FAILED"`)

* `VERIFICATION_CONFIG_NOT_FOUND` (value: `"VERIFICATION_CONFIG_NOT_FOUND"`)

* `CUSTOM_ACTION_NOT_FOUND` (value: `"CUSTOM_ACTION_NOT_FOUND"`)

* `DEPLOYMENT_STRATEGY_NOT_SUPPORTED` (value: `"DEPLOYMENT_STRATEGY_NOT_SUPPORTED"`)

* `RENDER_FEATURE_NOT_SUPPORTED` (value: `"RENDER_FEATURE_NOT_SUPPORTED"`)





## Enum: RenderingStateEnum


* `TARGET_RENDER_STATE_UNSPECIFIED` (value: `"TARGET_RENDER_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)




