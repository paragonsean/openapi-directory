

# GoogleCloudAiplatformV1beta1SuggestTrialsResponse

Response message for VizierService.SuggestTrials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time at which operation processing completed. |  [optional] |
|**startTime** | **String** | The time at which the operation was started. |  [optional] |
|**studyState** | [**StudyStateEnum**](#StudyStateEnum) | The state of the Study. |  [optional] |
|**trials** | [**List&lt;GoogleCloudAiplatformV1beta1Trial&gt;**](GoogleCloudAiplatformV1beta1Trial.md) | A list of Trials. |  [optional] |



## Enum: StudyStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



