

# GoogleCloudDiscoveryengineV1alphaConversation

External conversation proto definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Output only. The time the conversation finished. |  [optional] [readonly] |
|**messages** | [**List&lt;GoogleCloudDiscoveryengineV1alphaConversationMessage&gt;**](GoogleCloudDiscoveryengineV1alphaConversationMessage.md) | Conversation messages. |  [optional] |
|**name** | **String** | Immutable. Fully qualified name &#x60;project/_*_/locations/global/collections/{collection}/dataStore/_*_/conversations/_*&#x60; or &#x60;project/_*_/locations/global/collections/{collection}/engines/_*_/conversations/_*&#x60;. |  [optional] |
|**startTime** | **String** | Output only. The time the conversation started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the Conversation. |  [optional] |
|**userPseudoId** | **String** | A unique identifier for tracking users. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



