

# PredeployJobRun

PredeployJobRun contains information specific to a predeploy `JobRun`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**build** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to execute the custom actions associated with the predeploy Job. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. |  [optional] [readonly] |
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | Output only. The reason the predeploy failed. This will always be unspecified while the predeploy is in progress or if it succeeded. |  [optional] [readonly] |
|**failureMessage** | **String** | Output only. Additional information about the predeploy failure, if available. |  [optional] [readonly] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| FAILURE_CAUSE_UNSPECIFIED | &quot;FAILURE_CAUSE_UNSPECIFIED&quot; |
| CLOUD_BUILD_UNAVAILABLE | &quot;CLOUD_BUILD_UNAVAILABLE&quot; |
| EXECUTION_FAILED | &quot;EXECUTION_FAILED&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| CLOUD_BUILD_REQUEST_FAILED | &quot;CLOUD_BUILD_REQUEST_FAILED&quot; |



