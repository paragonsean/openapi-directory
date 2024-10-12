

# GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedAction

Rich Business Messaging (RBM) suggested client-side action that the user can choose from the card.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dial** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial**](GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionDial.md) |  |  [optional] |
|**openUrl** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri**](GoogleCloudDialogflowV2beta1IntentMessageRbmSuggestedActionRbmSuggestedActionOpenUri.md) |  |  [optional] |
|**postbackData** | **String** | Opaque payload that the Dialogflow receives in a user event when the user taps the suggested action. This data will be also forwarded to webhook to allow performing custom business logic. |  [optional] |
|**shareLocation** | **Object** | Opens the device&#39;s location chooser so the user can pick a location to send back to the agent. |  [optional] |
|**text** | **String** | Text to display alongside the action. |  [optional] |



