# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3ReviewDocumentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcsDestination** | **String** | The Cloud Storage uri for the human reviewed document if the review is succeeded. | [optional] 
**rejectionReason** | **String** | The reason why the review is rejected by reviewer. | [optional] 
**state** | **String** | The state of the review operation. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `REJECTED` (value: `"REJECTED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)




