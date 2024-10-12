# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaConversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Output only. The time the conversation finished. | [optional] [readonly] 
**messages** | [**[GoogleCloudDiscoveryengineV1alphaConversationMessage]**](GoogleCloudDiscoveryengineV1alphaConversationMessage.md) | Conversation messages. | [optional] 
**name** | **String** | Immutable. Fully qualified name &#x60;project/_*_/locations/global/collections/{collection}/dataStore/_*_/conversations/_*&#x60; or &#x60;project/_*_/locations/global/collections/{collection}/engines/_*_/conversations/_*&#x60;. | [optional] 
**startTime** | **String** | Output only. The time the conversation started. | [optional] [readonly] 
**state** | **String** | The state of the Conversation. | [optional] 
**userPseudoId** | **String** | A unique identifier for tracking users. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `COMPLETED` (value: `"COMPLETED"`)




