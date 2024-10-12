

# GoogleCloudDialogflowCxV3beta1Webhook

Webhooks host the developer's business logic. During a session, webhooks allow the developer to use the data extracted by Dialogflow's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabled** | **Boolean** | Indicates whether the webhook is disabled. |  [optional] |
|**displayName** | **String** | Required. The human-readable name of the webhook, unique within the agent. |  [optional] |
|**genericWebService** | [**GoogleCloudDialogflowCxV3beta1WebhookGenericWebService**](GoogleCloudDialogflowCxV3beta1WebhookGenericWebService.md) |  |  [optional] |
|**name** | **String** | The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: &#x60;projects//locations//agents//webhooks/&#x60;. |  [optional] |
|**serviceDirectory** | [**GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig**](GoogleCloudDialogflowCxV3beta1WebhookServiceDirectoryConfig.md) |  |  [optional] |
|**timeout** | **String** | Webhook execution timeout. Execution is considered failed if Dialogflow doesn&#39;t receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds. |  [optional] |



