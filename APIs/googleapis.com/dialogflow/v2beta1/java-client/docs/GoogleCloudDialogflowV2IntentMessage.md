

# GoogleCloudDialogflowV2IntentMessage

A rich response message. Corresponds to the intent `Response` field in the Dialogflow console. For more information, see [Rich response messages](https://cloud.google.com/dialogflow/docs/intents-rich-messages).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicCard** | [**GoogleCloudDialogflowV2IntentMessageBasicCard**](GoogleCloudDialogflowV2IntentMessageBasicCard.md) |  |  [optional] |
|**browseCarouselCard** | [**GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard**](GoogleCloudDialogflowV2IntentMessageBrowseCarouselCard.md) |  |  [optional] |
|**card** | [**GoogleCloudDialogflowV2IntentMessageCard**](GoogleCloudDialogflowV2IntentMessageCard.md) |  |  [optional] |
|**carouselSelect** | [**GoogleCloudDialogflowV2IntentMessageCarouselSelect**](GoogleCloudDialogflowV2IntentMessageCarouselSelect.md) |  |  [optional] |
|**image** | [**GoogleCloudDialogflowV2IntentMessageImage**](GoogleCloudDialogflowV2IntentMessageImage.md) |  |  [optional] |
|**linkOutSuggestion** | [**GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion**](GoogleCloudDialogflowV2IntentMessageLinkOutSuggestion.md) |  |  [optional] |
|**listSelect** | [**GoogleCloudDialogflowV2IntentMessageListSelect**](GoogleCloudDialogflowV2IntentMessageListSelect.md) |  |  [optional] |
|**mediaContent** | [**GoogleCloudDialogflowV2IntentMessageMediaContent**](GoogleCloudDialogflowV2IntentMessageMediaContent.md) |  |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | A custom platform-specific response. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Optional. The platform that this message is intended for. |  [optional] |
|**quickReplies** | [**GoogleCloudDialogflowV2IntentMessageQuickReplies**](GoogleCloudDialogflowV2IntentMessageQuickReplies.md) |  |  [optional] |
|**simpleResponses** | [**GoogleCloudDialogflowV2IntentMessageSimpleResponses**](GoogleCloudDialogflowV2IntentMessageSimpleResponses.md) |  |  [optional] |
|**suggestions** | [**GoogleCloudDialogflowV2IntentMessageSuggestions**](GoogleCloudDialogflowV2IntentMessageSuggestions.md) |  |  [optional] |
|**tableCard** | [**GoogleCloudDialogflowV2IntentMessageTableCard**](GoogleCloudDialogflowV2IntentMessageTableCard.md) |  |  [optional] |
|**text** | [**GoogleCloudDialogflowV2IntentMessageText**](GoogleCloudDialogflowV2IntentMessageText.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| FACEBOOK | &quot;FACEBOOK&quot; |
| SLACK | &quot;SLACK&quot; |
| TELEGRAM | &quot;TELEGRAM&quot; |
| KIK | &quot;KIK&quot; |
| SKYPE | &quot;SKYPE&quot; |
| LINE | &quot;LINE&quot; |
| VIBER | &quot;VIBER&quot; |
| ACTIONS_ON_GOOGLE | &quot;ACTIONS_ON_GOOGLE&quot; |
| GOOGLE_HANGOUTS | &quot;GOOGLE_HANGOUTS&quot; |



