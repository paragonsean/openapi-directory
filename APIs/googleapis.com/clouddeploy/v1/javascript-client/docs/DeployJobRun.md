# CloudDeployApi.DeployJobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | [**DeployArtifact**](DeployArtifact.md) |  | [optional] 
**build** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to deploy. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. | [optional] [readonly] 
**failureCause** | **String** | Output only. The reason the deploy failed. This will always be unspecified while the deploy is in progress or if it succeeded. | [optional] [readonly] 
**failureMessage** | **String** | Output only. Additional information about the deploy failure, if available. | [optional] [readonly] 
**metadata** | [**DeployJobRunMetadata**](DeployJobRunMetadata.md) |  | [optional] 



## Enum: FailureCauseEnum


* `FAILURE_CAUSE_UNSPECIFIED` (value: `"FAILURE_CAUSE_UNSPECIFIED"`)

* `CLOUD_BUILD_UNAVAILABLE` (value: `"CLOUD_BUILD_UNAVAILABLE"`)

* `EXECUTION_FAILED` (value: `"EXECUTION_FAILED"`)

* `DEADLINE_EXCEEDED` (value: `"DEADLINE_EXCEEDED"`)

* `MISSING_RESOURCES_FOR_CANARY` (value: `"MISSING_RESOURCES_FOR_CANARY"`)

* `CLOUD_BUILD_REQUEST_FAILED` (value: `"CLOUD_BUILD_REQUEST_FAILED"`)

* `DEPLOY_FEATURE_NOT_SUPPORTED` (value: `"DEPLOY_FEATURE_NOT_SUPPORTED"`)




