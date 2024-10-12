

# RemoteModelInfo

Remote Model Info

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connection** | **String** | Output only. Fully qualified name of the user-provided connection object of the remote model. Format: &#x60;&#x60;&#x60;\&quot;projects/{project_id}/locations/{location_id}/connections/{connection_id}\&quot;&#x60;&#x60;&#x60; |  [optional] [readonly] |
|**endpoint** | **String** | Output only. The endpoint for remote model. |  [optional] [readonly] |
|**maxBatchingRows** | **String** | Output only. Max number of rows in each batch sent to the remote service. If unset, the number of rows in each batch is set dynamically. |  [optional] [readonly] |
|**remoteModelVersion** | **String** | Output only. The model version for LLM. |  [optional] [readonly] |
|**remoteServiceType** | [**RemoteServiceTypeEnum**](#RemoteServiceTypeEnum) | Output only. The remote service type for remote model. |  [optional] [readonly] |
|**speechRecognizer** | **String** | Output only. The name of the speech recognizer to use for speech recognition. The expected format is &#x60;projects/{project}/locations/{location}/recognizers/{recognizer}&#x60;. Customers can specify this field at model creation. If not specified, a default recognizer &#x60;projects/{model project}/locations/global/recognizers/_&#x60; will be used. See more details at [recognizers](https://cloud.google.com/speech-to-text/v2/docs/reference/rest/v2/projects.locations.recognizers) |  [optional] [readonly] |



## Enum: RemoteServiceTypeEnum

| Name | Value |
|---- | -----|
| REMOTE_SERVICE_TYPE_UNSPECIFIED | &quot;REMOTE_SERVICE_TYPE_UNSPECIFIED&quot; |
| CLOUD_AI_TRANSLATE_V3 | &quot;CLOUD_AI_TRANSLATE_V3&quot; |
| CLOUD_AI_VISION_V1 | &quot;CLOUD_AI_VISION_V1&quot; |
| CLOUD_AI_NATURAL_LANGUAGE_V1 | &quot;CLOUD_AI_NATURAL_LANGUAGE_V1&quot; |
| CLOUD_AI_SPEECH_TO_TEXT_V2 | &quot;CLOUD_AI_SPEECH_TO_TEXT_V2&quot; |



