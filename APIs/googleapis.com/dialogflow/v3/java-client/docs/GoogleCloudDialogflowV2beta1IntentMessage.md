

# GoogleCloudDialogflowV2beta1IntentMessage

Corresponds to the `Response` field in the Dialogflow console.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicCard** | [**GoogleCloudDialogflowV2beta1IntentMessageBasicCard**](GoogleCloudDialogflowV2beta1IntentMessageBasicCard.md) |  |  [optional] |
|**browseCarouselCard** | [**GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard**](GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard.md) |  |  [optional] |
|**card** | [**GoogleCloudDialogflowV2beta1IntentMessageCard**](GoogleCloudDialogflowV2beta1IntentMessageCard.md) |  |  [optional] |
|**carouselSelect** | [**GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect**](GoogleCloudDialogflowV2beta1IntentMessageCarouselSelect.md) |  |  [optional] |
|**image** | [**GoogleCloudDialogflowV2beta1IntentMessageImage**](GoogleCloudDialogflowV2beta1IntentMessageImage.md) |  |  [optional] |
|**linkOutSuggestion** | [**GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion**](GoogleCloudDialogflowV2beta1IntentMessageLinkOutSuggestion.md) |  |  [optional] |
|**listSelect** | [**GoogleCloudDialogflowV2beta1IntentMessageListSelect**](GoogleCloudDialogflowV2beta1IntentMessageListSelect.md) |  |  [optional] |
|**mediaContent** | [**GoogleCloudDialogflowV2beta1IntentMessageMediaContent**](GoogleCloudDialogflowV2beta1IntentMessageMediaContent.md) |  |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | A custom platform-specific response. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Optional. The platform that this message is intended for. |  [optional] |
|**quickReplies** | [**GoogleCloudDialogflowV2beta1IntentMessageQuickReplies**](GoogleCloudDialogflowV2beta1IntentMessageQuickReplies.md) |  |  [optional] |
|**rbmCarouselRichCard** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard**](GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard.md) |  |  [optional] |
|**rbmStandaloneRichCard** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard**](GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard.md) |  |  [optional] |
|**rbmText** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmText**](GoogleCloudDialogflowV2beta1IntentMessageRbmText.md) |  |  [optional] |
|**simpleResponses** | [**GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses**](GoogleCloudDialogflowV2beta1IntentMessageSimpleResponses.md) |  |  [optional] |
|**suggestions** | [**GoogleCloudDialogflowV2beta1IntentMessageSuggestions**](GoogleCloudDialogflowV2beta1IntentMessageSuggestions.md) |  |  [optional] |
|**tableCard** | [**GoogleCloudDialogflowV2beta1IntentMessageTableCard**](GoogleCloudDialogflowV2beta1IntentMessageTableCard.md) |  |  [optional] |
|**telephonyPlayAudio** | [**GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio**](GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio.md) |  |  [optional] |
|**telephonySynthesizeSpeech** | [**GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech**](GoogleCloudDialogflowV2beta1IntentMessageTelephonySynthesizeSpeech.md) |  |  [optional] |
|**telephonyTransferCall** | [**GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall**](GoogleCloudDialogflowV2beta1IntentMessageTelephonyTransferCall.md) |  |  [optional] |
|**text** | [**GoogleCloudDialogflowV2beta1IntentMessageText**](GoogleCloudDialogflowV2beta1IntentMessageText.md) |  |  [optional] |



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
| TELEPHONY | &quot;TELEPHONY&quot; |
| GOOGLE_HANGOUTS | &quot;GOOGLE_HANGOUTS&quot; |



