# GitHubV3RestApi.OrgsCreateWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to true]
**config** | [**OrgsCreateWebhookRequestConfig**](OrgsCreateWebhookRequestConfig.md) |  | 
**events** | **[String]** | Determines what [events](https://docs.github.com/enterprise-server@2.21/webhooks/event-payloads) the hook is triggered for. | [optional] 
**name** | **String** | Must be passed as \&quot;web\&quot;. | 


