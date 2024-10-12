

# VerifyJobRun

VerifyJobRun contains information specific to a verify `JobRun`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactUri** | **String** | Output only. URI of a directory containing the verify artifacts. This contains the Skaffold event log. |  [optional] [readonly] |
|**build** | **String** | Output only. The resource name of the Cloud Build &#x60;Build&#x60; object that is used to verify. Format is &#x60;projects/{project}/locations/{location}/builds/{build}&#x60;. |  [optional] [readonly] |
|**eventLogPath** | **String** | Output only. File path of the Skaffold event log relative to the artifact URI. |  [optional] [readonly] |
|**failureCause** | [**FailureCauseEnum**](#FailureCauseEnum) | Output only. The reason the verify failed. This will always be unspecified while the verify is in progress or if it succeeded. |  [optional] [readonly] |
|**failureMessage** | **String** | Output only. Additional information about the verify failure, if available. |  [optional] [readonly] |



## Enum: FailureCauseEnum

| Name | Value |
|---- | -----|
| FAILURE_CAUSE_UNSPECIFIED | &quot;FAILURE_CAUSE_UNSPECIFIED&quot; |
| CLOUD_BUILD_UNAVAILABLE | &quot;CLOUD_BUILD_UNAVAILABLE&quot; |
| EXECUTION_FAILED | &quot;EXECUTION_FAILED&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| VERIFICATION_CONFIG_NOT_FOUND | &quot;VERIFICATION_CONFIG_NOT_FOUND&quot; |
| CLOUD_BUILD_REQUEST_FAILED | &quot;CLOUD_BUILD_REQUEST_FAILED&quot; |



