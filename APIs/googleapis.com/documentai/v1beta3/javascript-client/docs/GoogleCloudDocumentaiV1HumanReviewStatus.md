# CloudDocumentAiApi.GoogleCloudDocumentaiV1HumanReviewStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**humanReviewOperation** | **String** | The name of the operation triggered by the processed document. This field is populated only when the state is &#x60;HUMAN_REVIEW_IN_PROGRESS&#x60;. It has the same response type and metadata as the long-running operation returned by ReviewDocument. | [optional] 
**state** | **String** | The state of human review on the processing request. | [optional] 
**stateMessage** | **String** | A message providing more details about the human review state. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `VALIDATION_PASSED` (value: `"VALIDATION_PASSED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `ERROR` (value: `"ERROR"`)




