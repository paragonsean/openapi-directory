

# GoogleCloudMlV1SuggestTrialsResponse

This message will be placed in the response field of a completed google.longrunning.Operation associated with a SuggestTrials request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time at which operation processing completed. |  [optional] |
|**startTime** | **String** | The time at which the operation was started. |  [optional] |
|**studyState** | [**StudyStateEnum**](#StudyStateEnum) | The state of the study. |  [optional] |
|**trials** | [**List&lt;GoogleCloudMlV1Trial&gt;**](GoogleCloudMlV1Trial.md) | A list of trials. |  [optional] |



## Enum: StudyStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



