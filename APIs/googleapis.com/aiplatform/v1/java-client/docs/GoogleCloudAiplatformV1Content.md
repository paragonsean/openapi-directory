

# GoogleCloudAiplatformV1Content

The base structured datatype containing multi-part content of a message. A `Content` includes a `role` field designating the producer of the `Content` and a `parts` field containing multi-part data that contains the content of the message turn.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parts** | [**List&lt;GoogleCloudAiplatformV1Part&gt;**](GoogleCloudAiplatformV1Part.md) | Required. Ordered &#x60;Parts&#x60; that constitute a single message. Parts may have different IANA MIME types. |  [optional] |
|**role** | **String** | Optional. The producer of the content. Must be either &#39;user&#39; or &#39;model&#39;. Useful to set for multi-turn conversations, otherwise can be left blank or unset. |  [optional] |



