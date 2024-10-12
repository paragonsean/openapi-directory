

# GoogleCloudAiplatformV1beta1SchemaPredictionResult

Represents a line of JSONL in the batch prediction output file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**GoogleCloudAiplatformV1beta1SchemaPredictionResultError**](GoogleCloudAiplatformV1beta1SchemaPredictionResultError.md) |  |  [optional] |
|**instance** | **Map&lt;String, Object&gt;** | User&#39;s input instance. Struct is used here instead of Any so that JsonFormat does not append an extra \&quot;@type\&quot; field when we convert the proto to JSON. |  [optional] |
|**key** | **String** | Optional user-provided key from the input instance. |  [optional] |
|**prediction** | **Object** | The prediction result. Value is used here instead of Any so that JsonFormat does not append an extra \&quot;@type\&quot; field when we convert the proto to JSON and so we can represent array of objects. Do not set error if this is set. |  [optional] |



