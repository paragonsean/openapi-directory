

# GoogleCloudDocumentaiV1beta3HumanReviewStatus

The status of human review on a processed document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**humanReviewOperation** | **String** | The name of the operation triggered by the processed document. This field is populated only when the state is &#x60;HUMAN_REVIEW_IN_PROGRESS&#x60;. It has the same response type and metadata as the long-running operation returned by ReviewDocument. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of human review on the processing request. |  [optional] |
|**stateMessage** | **String** | A message providing more details about the human review state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| VALIDATION_PASSED | &quot;VALIDATION_PASSED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| ERROR | &quot;ERROR&quot; |



