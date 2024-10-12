

# GoogleCloudDocumentaiV1ReviewDocumentResponse

Response message for the ReviewDocument method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsDestination** | **String** | The Cloud Storage uri for the human reviewed document if the review is succeeded. |  [optional] |
|**rejectionReason** | **String** | The reason why the review is rejected by reviewer. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the review operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |



