# CloudDeployApi.PredeployJobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to execute the custom actions associated with the predeploy Job. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. | [optional] [readonly] 
**failureCause** | **String** | Output only. The reason the predeploy failed. This will always be unspecified while the predeploy is in progress or if it succeeded. | [optional] [readonly] 
**failureMessage** | **String** | Output only. Additional information about the predeploy failure, if available. | [optional] [readonly] 



## Enum: FailureCauseEnum


* `FAILURE_CAUSE_UNSPECIFIED` (value: `"FAILURE_CAUSE_UNSPECIFIED"`)

* `CLOUD_BUILD_UNAVAILABLE` (value: `"CLOUD_BUILD_UNAVAILABLE"`)

* `EXECUTION_FAILED` (value: `"EXECUTION_FAILED"`)

* `DEADLINE_EXCEEDED` (value: `"DEADLINE_EXCEEDED"`)

* `CLOUD_BUILD_REQUEST_FAILED` (value: `"CLOUD_BUILD_REQUEST_FAILED"`)




