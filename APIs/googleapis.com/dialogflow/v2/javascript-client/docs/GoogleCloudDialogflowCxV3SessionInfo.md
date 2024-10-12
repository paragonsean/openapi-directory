# DialogflowApi.GoogleCloudDialogflowCxV3SessionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **{String: Object}** | Optional for WebhookRequest. Optional for WebhookResponse. All parameters collected from forms and intents during the session. Parameters can be created, updated, or removed by the webhook. To remove a parameter from the session, the webhook should explicitly set the parameter value to null in WebhookResponse. The map is keyed by parameters&#39; display names. | [optional] 
**session** | **String** | Always present for WebhookRequest. Ignored for WebhookResponse. The unique identifier of the session. This field can be used by the webhook to identify a session. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60; if environment is specified. | [optional] 


