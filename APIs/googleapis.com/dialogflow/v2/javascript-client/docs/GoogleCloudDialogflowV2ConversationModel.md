# DialogflowApi.GoogleCloudDialogflowV2ConversationModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**articleSuggestionModelMetadata** | [**GoogleCloudDialogflowV2ArticleSuggestionModelMetadata**](GoogleCloudDialogflowV2ArticleSuggestionModelMetadata.md) |  | [optional] 
**createTime** | **String** | Output only. Creation time of this model. | [optional] [readonly] 
**datasets** | [**[GoogleCloudDialogflowV2InputDataset]**](GoogleCloudDialogflowV2InputDataset.md) | Required. Datasets used to create model. | [optional] 
**displayName** | **String** | Required. The display name of the model. At most 64 bytes long. | [optional] 
**languageCode** | **String** | Language code for the conversation model. If not specified, the language is en-US. Language at ConversationModel should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. | [optional] 
**name** | **String** | ConversationModel resource name. Format: &#x60;projects//conversationModels/&#x60; | [optional] 
**smartReplyModelMetadata** | [**GoogleCloudDialogflowV2SmartReplyModelMetadata**](GoogleCloudDialogflowV2SmartReplyModelMetadata.md) |  | [optional] 
**state** | **String** | Output only. State of the model. A model can only serve prediction requests after it gets deployed. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `UNDEPLOYED` (value: `"UNDEPLOYED"`)

* `DEPLOYING` (value: `"DEPLOYING"`)

* `DEPLOYED` (value: `"DEPLOYED"`)

* `UNDEPLOYING` (value: `"UNDEPLOYING"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED` (value: `"FAILED"`)

* `PENDING` (value: `"PENDING"`)




