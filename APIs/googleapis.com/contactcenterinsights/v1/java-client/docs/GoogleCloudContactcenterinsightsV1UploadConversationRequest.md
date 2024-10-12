

# GoogleCloudContactcenterinsightsV1UploadConversationRequest

Request to upload a conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversation** | [**GoogleCloudContactcenterinsightsV1Conversation**](GoogleCloudContactcenterinsightsV1Conversation.md) |  |  [optional] |
|**conversationId** | **String** | Optional. A unique ID for the new conversation. This ID will become the final component of the conversation&#39;s resource name. If no ID is specified, a server-generated ID will be used. This value should be 4-64 characters and must match the regular expression &#x60;^[a-z0-9-]{4,64}$&#x60;. Valid characters are &#x60;a-z-&#x60; |  [optional] |
|**parent** | **String** | Required. The parent resource of the conversation. |  [optional] |
|**redactionConfig** | [**GoogleCloudContactcenterinsightsV1RedactionConfig**](GoogleCloudContactcenterinsightsV1RedactionConfig.md) |  |  [optional] |
|**speechConfig** | [**GoogleCloudContactcenterinsightsV1SpeechConfig**](GoogleCloudContactcenterinsightsV1SpeechConfig.md) |  |  [optional] |



