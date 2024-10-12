

# GoogleCloudAiplatformV1beta1NearestNeighborSearchOperationMetadataRecordError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embeddingId** | **String** | Empty if the embedding id is failed to parse. |  [optional] |
|**errorMessage** | **String** | A human-readable message that is shown to the user to help them fix the error. Note that this message may change from time to time, your code should check against error_type as the source of truth. |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) | The error type of this record. |  [optional] |
|**rawRecord** | **String** | The original content of this record. |  [optional] |
|**sourceGcsUri** | **String** | Cloud Storage URI pointing to the original file in user&#39;s bucket. |  [optional] |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| ERROR_TYPE_UNSPECIFIED | &quot;ERROR_TYPE_UNSPECIFIED&quot; |
| EMPTY_LINE | &quot;EMPTY_LINE&quot; |
| INVALID_JSON_SYNTAX | &quot;INVALID_JSON_SYNTAX&quot; |
| INVALID_CSV_SYNTAX | &quot;INVALID_CSV_SYNTAX&quot; |
| INVALID_AVRO_SYNTAX | &quot;INVALID_AVRO_SYNTAX&quot; |
| INVALID_EMBEDDING_ID | &quot;INVALID_EMBEDDING_ID&quot; |
| EMBEDDING_SIZE_MISMATCH | &quot;EMBEDDING_SIZE_MISMATCH&quot; |
| NAMESPACE_MISSING | &quot;NAMESPACE_MISSING&quot; |
| PARSING_ERROR | &quot;PARSING_ERROR&quot; |
| DUPLICATE_NAMESPACE | &quot;DUPLICATE_NAMESPACE&quot; |
| OP_IN_DATAPOINT | &quot;OP_IN_DATAPOINT&quot; |
| MULTIPLE_VALUES | &quot;MULTIPLE_VALUES&quot; |
| INVALID_NUMERIC_VALUE | &quot;INVALID_NUMERIC_VALUE&quot; |
| INVALID_ENCODING | &quot;INVALID_ENCODING&quot; |



