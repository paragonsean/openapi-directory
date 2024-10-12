

# DeployJobRun

DeployJobRun contains information specific to a deploy `JobRun`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifact** | [**DeployArtifact**](DeployArtifact.md) |  |  [optional] |
|**build** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to deploy. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. |  [optional] [readonly] |
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | Output only. The reason the deploy failed. This will always be unspecified while the deploy is in progress or if it succeeded. |  [optional] [readonly] |
|**failureMessage** | **String** | Output only. Additional information about the deploy failure, if available. |  [optional] [readonly] |
|**metadata** | [**DeployJobRunMetadata**](DeployJobRunMetadata.md) |  |  [optional] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| FAILURE_CAUSE_UNSPECIFIED | &quot;FAILURE_CAUSE_UNSPECIFIED&quot; |
| CLOUD_BUILD_UNAVAILABLE | &quot;CLOUD_BUILD_UNAVAILABLE&quot; |
| EXECUTION_FAILED | &quot;EXECUTION_FAILED&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| MISSING_RESOURCES_FOR_CANARY | &quot;MISSING_RESOURCES_FOR_CANARY&quot; |
| CLOUD_BUILD_REQUEST_FAILED | &quot;CLOUD_BUILD_REQUEST_FAILED&quot; |
| DEPLOY_FEATURE_NOT_SUPPORTED | &quot;DEPLOY_FEATURE_NOT_SUPPORTED&quot; |



