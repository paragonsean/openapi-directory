

# GoogleCloudDialogflowV2ConversationModel

Represents a conversation model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**articleSuggestionModelMetadata** | [**GoogleCloudDialogflowV2ArticleSuggestionModelMetadata**](GoogleCloudDialogflowV2ArticleSuggestionModelMetadata.md) |  |  [optional] |
|**createTime** | **String** | Output only. Creation time of this model. |  [optional] [readonly] |
|**datasets** | [**List&lt;GoogleCloudDialogflowV2InputDataset&gt;**](GoogleCloudDialogflowV2InputDataset.md) | Required. Datasets used to create model. |  [optional] |
|**displayName** | **String** | Required. The display name of the model. At most 64 bytes long. |  [optional] |
|**languageCode** | **String** | Language code for the conversation model. If not specified, the language is en-US. Language at ConversationModel should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. |  [optional] |
|**name** | **String** | ConversationModel resource name. Format: &#x60;projects//conversationModels/&#x60; |  [optional] |
|**smartReplyModelMetadata** | [**GoogleCloudDialogflowV2SmartReplyModelMetadata**](GoogleCloudDialogflowV2SmartReplyModelMetadata.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the model. A model can only serve prediction requests after it gets deployed. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| UNDEPLOYED | &quot;UNDEPLOYED&quot; |
| DEPLOYING | &quot;DEPLOYING&quot; |
| DEPLOYED | &quot;DEPLOYED&quot; |
| UNDEPLOYING | &quot;UNDEPLOYING&quot; |
| DELETING | &quot;DELETING&quot; |
| FAILED | &quot;FAILED&quot; |
| PENDING | &quot;PENDING&quot; |



