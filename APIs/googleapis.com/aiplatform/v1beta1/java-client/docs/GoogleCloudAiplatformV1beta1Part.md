

# GoogleCloudAiplatformV1beta1Part

A datatype containing media that is part of a multi-part `Content` message. A `Part` consists of data which has an associated datatype. A `Part` can only contain one of the accepted types in `Part.data`. A `Part` must have a fixed IANA MIME type identifying the type and subtype of the media if `inline_data` or `file_data` field is filled with raw bytes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileData** | [**GoogleCloudAiplatformV1beta1FileData**](GoogleCloudAiplatformV1beta1FileData.md) |  |  [optional] |
|**functionCall** | [**GoogleCloudAiplatformV1beta1FunctionCall**](GoogleCloudAiplatformV1beta1FunctionCall.md) |  |  [optional] |
|**functionResponse** | [**GoogleCloudAiplatformV1beta1FunctionResponse**](GoogleCloudAiplatformV1beta1FunctionResponse.md) |  |  [optional] |
|**inlineData** | [**GoogleCloudAiplatformV1beta1Blob**](GoogleCloudAiplatformV1beta1Blob.md) |  |  [optional] |
|**text** | **String** | Optional. Text part (can be code). |  [optional] |
|**videoMetadata** | [**GoogleCloudAiplatformV1beta1VideoMetadata**](GoogleCloudAiplatformV1beta1VideoMetadata.md) |  |  [optional] |



