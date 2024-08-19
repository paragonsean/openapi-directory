# VertexAiApi.GoogleCloudAiplatformV1NearestNeighborSearchOperationMetadataRecordError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddingId** | **String** | Empty if the embedding id is failed to parse. | [optional] 
**errorMessage** | **String** | A human-readable message that is shown to the user to help them fix the error. Note that this message may change from time to time, your code should check against error_type as the source of truth. | [optional] 
**errorType** | **String** | The error type of this record. | [optional] 
**rawRecord** | **String** | The original content of this record. | [optional] 
**sourceGcsUri** | **String** | Cloud Storage URI pointing to the original file in user&#39;s bucket. | [optional] 



## Enum: ErrorTypeEnum


* `ERROR_TYPE_UNSPECIFIED` (value: `"ERROR_TYPE_UNSPECIFIED"`)

* `EMPTY_LINE` (value: `"EMPTY_LINE"`)

* `INVALID_JSON_SYNTAX` (value: `"INVALID_JSON_SYNTAX"`)

* `INVALID_CSV_SYNTAX` (value: `"INVALID_CSV_SYNTAX"`)

* `INVALID_AVRO_SYNTAX` (value: `"INVALID_AVRO_SYNTAX"`)

* `INVALID_EMBEDDING_ID` (value: `"INVALID_EMBEDDING_ID"`)

* `EMBEDDING_SIZE_MISMATCH` (value: `"EMBEDDING_SIZE_MISMATCH"`)

* `NAMESPACE_MISSING` (value: `"NAMESPACE_MISSING"`)

* `PARSING_ERROR` (value: `"PARSING_ERROR"`)

* `DUPLICATE_NAMESPACE` (value: `"DUPLICATE_NAMESPACE"`)

* `OP_IN_DATAPOINT` (value: `"OP_IN_DATAPOINT"`)

* `MULTIPLE_VALUES` (value: `"MULTIPLE_VALUES"`)

* `INVALID_NUMERIC_VALUE` (value: `"INVALID_NUMERIC_VALUE"`)

* `INVALID_ENCODING` (value: `"INVALID_ENCODING"`)




